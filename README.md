# OpenSteva

Local-first AI code assistant. Fork of [OpenJarvis](https://github.com/open-jarvis/OpenJarvis), rebranded and specialized for coding tasks.

## What is this?

OpenSteva is an on-device AI code assistant that runs LLMs locally via Ollama (or vLLM/MLX/llama.cpp). No cloud APIs required. Your code never leaves your machine.

**Key features:**
- Code generation, debugging, and refactoring
- File read/write, shell execution, git operations
- MCP (Model Context Protocol) tool integration
- Local learning from your coding sessions
- Zero external telemetry — fully private

## Quick Start

```bash
# Prerequisites: Python 3.10+, Ollama installed
git clone git@github.com:subzone/OpenSteva.git
cd OpenSteva
uv sync
ollama pull qwen2.5-coder:7b

# Run the code assistant
uv run steva chat
```

## Configuration

Config lives at `~/.opensteva/config.toml` (created on first run) or `configs/opensteva/config.toml` in this repo.

Key settings:
```toml
[intelligence]
default_model = "qwen2.5-coder:7b"
preferred_engine = "ollama"

[agent]
default_agent = "code_assistant"

[analytics]
enabled = false  # No external telemetry
```

## Recommended Models

| Model | Size | Best for |
|---|---|---|
| qwen2.5-coder:7b | ~4GB | General coding, fast responses |
| qwen2.5-coder:32b | ~20GB | Complex reasoning, architecture |
| deepseek-coder-v2:16b | ~10GB | Multi-language, strong reasoning |
| codellama:13b | ~7GB | Python/C++/Java focused |

## Architecture

```
src/opensteva/
├── agents/          # Agent loops (code_assistant, react, openhands)
├── engine/          # Inference backends (Ollama, vLLM, MLX, llama.cpp)
├── tools/           # File I/O, shell, git, code interpreter, web search
├── mcp/             # Model Context Protocol server/client
├── learning/        # Local trace-based improvement
├── telemetry/       # Local GPU/energy metrics (never sent externally)
└── server/          # FastAPI server for UI/programmatic access
```

## Privacy & Compliance

- **No external analytics** — PostHog disabled, `posthog` removed from dependencies
- **No cloud calls by default** — inference runs locally via Ollama
- **Local traces only** — session data stored in `~/.opensteva/traces.db`
- **No PII collection** — the analytics module is a no-op

## License

Apache 2.0 — same as upstream OpenJarvis.

Original work: © Open Jarvis Contributors (Stanford Hazy Research / Scaling Intelligence Lab)
