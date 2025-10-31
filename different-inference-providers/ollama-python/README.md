# Ollama Python SDK Example

Learn how to use Ollama for local model inference with the Python SDK. Ollama makes running LLMs locally as easy as using Docker.

## Environment Variables

No API keys required! Ollama runs completely locally.

## Dependencies

### 1. Install Ollama

**macOS:**
```bash
# Download from https://ollama.ai
# Or use Homebrew
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:** Download from https://ollama.ai/download/windows

### 2. Start Ollama Service

```bash
ollama serve
```

### 3. Pull a Model

```bash
# Small, fast, modern models (good for testing)
ollama pull qwen2.5:3b

# Alternative models
ollama pull phi4
ollama pull llama3.2:3b
```

### 4. Install Python SDK

```bash
pip install ollama
# Or
pip install -r ../requirements.txt
```

## Running the Example

```bash
python main.py
```

Make sure Ollama is running (`ollama serve`) before running the example.

## What You'll Learn

This example demonstrates:

1. **Basic Chat Completion** - Simple chat interface with system and user messages
2. **Custom Options** - Temperature, top-k, top-p, repeat penalty
3. **Streaming Response** - Real-time token streaming

## Available Models

| Model | Size | RAM | Description |
|-------|------|-----|-------------|
| `qwen2.5:3b` | 3B | 6GB | Latest Qwen, excellent quality (recommended) |
| `phi4` | 14B | 8GB | Microsoft's latest, highly efficient |
| `llama3.2:3b` | 3B | 6GB | Balanced speed/quality |
| `qwen2.5:7b` | 7B | 12GB | Larger Qwen for better performance |
| `llama3.1:8b` | 8B | 12GB | High quality |
| `mistral` | 7B | 12GB | Excellent general purpose |

See all models: https://ollama.ai/library

## Key Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `temperature` | float | 0.8 | Randomness (0.0-2.0) |
| `top_k` | int | 40 | Number of top tokens to consider |
| `top_p` | float | 0.9 | Nucleus sampling threshold |
| `repeat_penalty` | float | 1.1 | Penalty for repeating tokens |
| `num_predict` | int | 128 | Max tokens to generate |
| `stop` | list | [] | Stop sequences |
| `seed` | int | - | Random seed for reproducibility |

## Why Ollama?

**Advantages:**
- Simplicity - one command to download and run models
- Performance - optimized inference with quantization
- Privacy - everything runs locally
- No API costs - free after installation
- Easy management - simple CLI for models
- GPU support - automatically uses available GPUs

**Disadvantages:**
- Limited to Ollama model library
- Requires local hardware resources
- Quality depends on model size
- No training/fine-tuning support

## Model Management

```bash
# List installed models
ollama list

# Remove a model
ollama rm mistral

# Pull specific version
ollama pull llama3.1:8b-q4_0
```

## Performance Tips

1. **Use GPU**: Ollama automatically uses NVIDIA, AMD, or Apple Silicon GPUs
2. **Choose right model size**: 1B-3B for development, 7B-13B for production
3. **Quantization**: Models are pre-quantized (Q4_0, Q4_K_M, Q5_K_M)
4. **Context size**: Adjust `num_ctx` for longer conversations

## Further Reading

- [Ollama Website](https://ollama.ai)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [Python SDK Documentation](https://github.com/ollama/ollama-python)
- [Model Library](https://ollama.ai/library)
