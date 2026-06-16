---
artifact-version: "1.0"
id: dp-2026-06-14-vllm-vs-ollama-decision
type: specification
status: draft
tags: [usage-trace, designed-prompt, decision-brief, model-serving, agentic]
created: 2026-06-14
author: claude-sonnet-4-6
---

# Decision Brief: vLLM vs Ollama — Model Serving Runtime for Torres-Core

## Decision to Make

Choose the local LLM inference runtime that will serve as the model-serving substrate for the Torres-Core agentic stack. This decision gates the substrate deploy session and all downstream agentic work (LiteLLM gateway, HermesAgent, Life Flow agent, OpenWebUI maturity).

---

## Context Snapshot

### Hardware (as of 2026-06-14)
- **GPU**: RTX 4060 — 8 GB VRAM — on **proxmox-mf** (same node as Frigate CT205)
  - Frigate uses TensorRT for object detection; the GPU is shared
  - GPU passthrough to a VM is needed for inference workloads
- **CPU/RAM**: Proxmox-mf specs (check `/proc/cpuinfo` + `free -h` before sizing)
- **Storage**: datapool NFS available; model weights will be large (4–70 GB each)

### What the inference layer must serve
| Consumer | Concurrency pattern | Latency expectation |
|---|---|---|
| OpenWebUI (interactive chat) | 1–3 concurrent users | ~1–5 s/response acceptable |
| Life Flow agent (Phase A) | 1 request at dawn, scheduled | Batch-tolerant |
| HermesAgent tasks | Multiple tool-call loops, potentially parallel | Medium; <10 s per tool call |
| MCP gateway tools | On-demand, bursty | Same as HermesAgent |
| Council forum (Phase C, future) | Multiple agents simultaneously | High concurrency; future concern |

### Architecture constraint
LiteLLM sits in front as the API gateway. The inference runtime is a LiteLLM *backend*, not directly consumer-facing. Both vLLM and Ollama expose an OpenAI-compatible `/v1/completions` + `/v1/chat/completions` endpoint, so LiteLLM compatibility is **not** a differentiator — both work.

---

## The Two Options

### Option A: Ollama

**What it is**: llama.cpp-based server wrapped in a friendly CLI. Runs GGUF quantized models (Q4_K_M, Q5_K_M, Q8_0, etc.). CPU+GPU hybrid — can offload layers to RAM when VRAM is full.

**Strengths for Torres-Core**
- Fastest path from zero to running model: `ollama pull llama3:8b` → serving in minutes
- GGUF quantization is VRAM-friendly: Llama 3.1 8B at Q4_K_M ≈ 4.7 GB → fits RTX 4060 with headroom
- CPU offload means you can run 13B+ models by spilling layers to RAM (slower but functional)
- Model management via CLI (`ollama list`, `ollama pull`, `ollama rm`) — no Python ops
- Single static binary; easy container or bare-metal deploy
- Very active homelab community; lots of runbooks
- Low operational overhead — right size for a solo operator

**Weaknesses**
- Single-request throughput: Ollama queues concurrent requests rather than batching them
  - If 3 agents fire simultaneously, they queue; request 3 waits for requests 1+2 to finish
  - Acceptable for Phase A (Life Flow only); may become a bottleneck at Phase C (Council)
- No PagedAttention: KV-cache is not shared across requests; each context window is independent
- Less configurable for production tuning (context window, batch size, quantization at serve time)

**Deploy sketch**
```
VM on proxmox-mf (or LXC with GPU passthrough)
→ ollama serve
→ LiteLLM points to http://ollama-host:11434
→ OpenWebUI + agents hit LiteLLM
```

---

### Option B: vLLM

**What it is**: Production-grade inference server from Berkeley. Uses PagedAttention for high-throughput concurrent serving. Runs safetensor / HuggingFace format models; also supports GGUF via llama.cpp backend (recent versions). GPU-first.

**Strengths for Torres-Core**
- PagedAttention: KV-cache paged across requests → much higher throughput under concurrent load
- Continuous batching: multiple in-flight requests processed together per GPU tick
- Better for Phase C (Council forum) and beyond where concurrency matters
- Production-quality: token streaming, logprobs, structured outputs, speculative decoding
- AWQ/GPTQ quantization for HuggingFace models: 8B models at 4-bit ≈ 4–5 GB VRAM

**Weaknesses for Torres-Core**
- Higher setup complexity: Python venv or Docker, CUDA toolkit, model downloads from HF
- Model format mismatch: HuggingFace safetensors, not GGUF; separate model library from Ollama
  - You can't reuse Ollama-pulled models in vLLM (different format)
- VRAM footprint: vLLM's PagedAttention reserves a memory pool at startup (configurable but tricky)
  - With 8 GB VRAM shared with Frigate TensorRT, this requires careful tuning
  - `--gpu-memory-utilization 0.7` or similar to avoid OOM with Frigate co-tenant
- Less forgiving if you hit OOM: crashes rather than graceful CPU fallback
- Heavier operational overhead: Python deps, CUDA version pinning, HF token for gated models

**Deploy sketch**
```
VM on proxmox-mf (with GPU passthrough, dedicated VRAM slice)
→ vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --quantization awq \
     --gpu-memory-utilization 0.7
→ LiteLLM points to http://vllm-host:8000
→ OpenWebUI + agents hit LiteLLM
```

---

## Key Tensions

| Tension | Ollama | vLLM |
|---|---|---|
| Time to first inference | Minutes | Hours (model download + setup) |
| 8 GB VRAM w/ Frigate co-tenant | Safe (CPU spillover) | Risky without careful tuning |
| Concurrent agents (Phase C+) | Queued (bottleneck) | Batched (efficient) |
| Operational complexity | Low | Medium-high |
| Model ecosystem | GGUF (llama.cpp community) | HuggingFace (bleeding edge) |
| Homelab runbooks | Abundant | Sparse for homelab configs |
| CPU fallback | Yes (graceful) | No (OOM crash) |

---

## A Third Path: Staged Migration

Start with **Ollama** for the substrate deploy session (Phase A + initial agentic work). Migrate to **vLLM** when concurrency becomes the actual bottleneck (Phase C or when you observe queue latency in LiteLLM metrics).

Why this is viable: LiteLLM abstracts the backend. Switching from Ollama to vLLM is a one-line config change in LiteLLM. No consumer code changes.

Why it might be wrong: You build runbooks and Hermes tool calls against Ollama's behavior (context limits, streaming quirks). Migrating later means re-testing. If you know you want vLLM eventually, starting there avoids regression work.

---

## Questions to Resolve Before Deciding

1. **Frigate GPU sharing**: Does Frigate release the GPU between detections (allowing inference), or does it hold a continuous CUDA context? This determines whether Ollama's CPU fallback is the safety net you need or whether vLLM's reserved pool creates a conflict.

2. **Phase C timeline**: Is Council forum (multiple concurrent agents) a 2026 goal or 2027+? If 2027+, Ollama's queue model is fine for 12+ months.

3. **Model size appetite**: Are you planning to run 70B models (requires multi-GPU or heavy quantization), 13B (tight on 8 GB), or 7–8B (fits comfortably)? Ollama handles 7–8B well; vLLM's advantage is larger.

4. **GPU passthrough dedication**: Will the inference VM get a dedicated GPU (Frigate on CPU or a second GPU), or are they truly sharing the RTX 4060?

---

## Claude's Lean (as of this brief)

**Start with Ollama. Plan the migration path to vLLM at Phase C.**

Rationale: The RTX 4060 VRAM constraint + Frigate co-tenancy + solo-operator overhead all favor Ollama now. The substrate deploy session is already complex (LiteLLM + HermesAgent + MCP gateway + VM provisioning). Adding vLLM's CUDA tuning to that session increases failure surface. LiteLLM's abstraction makes the migration cheap later.

The decision is reversible. The substrate deploy session is not.

---

## Prompt for Local Model Session

> You are helping me choose between two LLM inference runtimes for a homelab AI stack.
>
> **My setup**: Proxmox cluster. One node (proxmox-mf) has an RTX 4060 (8 GB VRAM). It currently runs Frigate (video surveillance, uses TensorRT). I want to add local LLM inference on the same node. LiteLLM will sit in front as an API gateway. Consumers: OpenWebUI (interactive), one scheduled morning agent, and eventually 3–5 concurrent AI agents.
>
> **Option A: Ollama** — llama.cpp, GGUF format, CPU spillover, simple ops, sequential request queuing.
> **Option B: vLLM** — PagedAttention, HuggingFace format, concurrent batching, higher ops overhead, no CPU fallback.
>
> Key unknowns I need your help thinking through:
> 1. Does Frigate's TensorRT hold a persistent CUDA context, or does it release between frames? Does this affect whether vLLM or Ollama is safer to co-run?
> 2. For 3–5 concurrent agents, does Ollama's queue model introduce unacceptable latency at 7–8B model size on an RTX 4060?
> 3. Is there a VRAM partitioning approach (e.g., MIG, CUDA MPS) that would let both Frigate and vLLM share the GPU cleanly?
> 4. Given a solo operator with a homelab, does the staged migration path (Ollama now → vLLM later via LiteLLM config swap) make sense, or does the re-testing cost argue for starting with vLLM?
>
> Please surface the key tradeoffs I'm missing and give me a recommendation with reasoning.

---

## Connection Notes

- Gates: `projects/agentic/CONTEXT.md` → substrate deploy session → HermesAgent / LiteLLM / MCP gateway v1
- Related: `review/board.md` card "vLLM vs Ollama decision" (currently Next Up)
- Output of this decision feeds: LiteLLM backend config, HermesAgent VM specs, proxmox-mf GPU passthrough design
