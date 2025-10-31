# llama.cpp Server and Client Example

Learn how to run a high-performance LLM inference server using llama.cpp. Built in C++ with extreme optimization for maximum speed and minimum memory usage.

## Environment Variables

No API keys required! llama.cpp runs completely locally.

Optional environment variables for server configuration:
```bash
export LLAMA_CPP_DIR="$HOME/llama.cpp"
export MODEL_DIR="./models"
export MODEL_NAME="Qwen2.5-3B-Instruct-Q4_K_M.gguf"
export PORT="8080"
export CONTEXT_SIZE="2048"
export N_GPU_LAYERS="0"  # -1 for all layers on GPU
```

## Dependencies

### System Requirements
- Bash shell (Linux, macOS, or WSL on Windows)
- C++ compiler (gcc, clang, or MSVC)
- Git
- 8GB+ RAM for 7B models (16GB+ recommended)
- (Optional) NVIDIA GPU with CUDA for GPU acceleration

### Python Client Dependencies
```bash
pip install requests python-dotenv
# Or
pip install -r ../requirements.txt
```

## Running the Examples

### 1. Start the Server (Terminal 1)

```bash
# Make script executable
chmod +x run-server.sh

# Run server (CPU-only mode)
./run-server.sh

# GPU mode (NVIDIA - offload all layers)
N_GPU_LAYERS=-1 ./run-server.sh

# Custom port
PORT=8000 ./run-server.sh
```

The script will:
- Download and compile llama.cpp
- Download a GGUF format model
- Start the HTTP server at `http://localhost:8080`

### 2. Run the Client (Terminal 2)

```bash
python client-example.py
```

## What You'll Learn

This example demonstrates:

1. **Server Setup** - Automatic llama.cpp installation, model downloading, server configuration
2. **HTTP Client** - Health checks, basic completion, chat-formatted requests
3. **Streaming** - Real-time token-by-token responses

## GGUF Model Format

llama.cpp uses GGUF (GPT-Generated Unified Format):
- Single-file format with weights and metadata
- Various quantization levels

### Quantization Levels

| Format | Size | Quality | Speed | Description |
|--------|------|---------|-------|-------------|
| Q4_K_M | ~4GB | Good | Fastest | Recommended starting point |
| Q5_K_M | ~5GB | Better | Fast | Better quality, slightly slower |
| Q6_K | ~6GB | Very Good | Medium | High quality |
| Q8_0 | ~8GB | Excellent | Slower | Near-perfect quality |
| F16 | ~14GB | Perfect | Slowest | Full precision |

### Recommended Models

**3-4B Models (~2-3GB with Q4 quantization):**
- Qwen2.5 3B Instruct (recommended)
- Phi-3.5 Mini 3.8B Instruct
- Llama 3.2 3B Instruct

**7B Models (~4GB with Q4 quantization):**
- Qwen2.5 7B Instruct
- Mistral 7B Instruct v0.2
- Llama 3.1 8B Instruct

Find more at: https://huggingface.co/models?library=gguf

## Key Configuration Options

### Server Parameters

```bash
./server \
    -m model.gguf \           # Model path
    --port 8080 \             # HTTP port
    --host 0.0.0.0 \          # Bind address
    --ctx-size 2048 \         # Context window
    -ngl 32 \                 # GPU layers (-1 = all)
    --threads 8 \             # CPU threads
```

### Client API Parameters

| Parameter | Description |
|-----------|-------------|
| `prompt` | Input text |
| `n_predict` | Max tokens to generate |
| `temperature` | Randomness (0.0-2.0) |
| `top_k` | Top-k sampling |
| `top_p` | Nucleus sampling |
| `repeat_penalty` | Discourage repetition |
| `stop` | Stop sequences |
| `stream` | Enable streaming |

## Why llama.cpp?

**Advantages:**
- Extremely fast - 2-4x faster than PyTorch
- Low memory - efficient quantization (4-bit to 16-bit)
- Cross-platform - CPU, NVIDIA (CUDA), AMD (ROCm), Apple Silicon (Metal)
- Production-ready - used in many commercial applications
- No Python overhead - pure C++ core

**Disadvantages:**
- Compilation required - not as simple as Ollama
- Manual model management - need to download GGUF files
- C++ knowledge helpful - for advanced usage
- Limited to inference - no training/fine-tuning

## Performance Optimization

### GPU Acceleration

**NVIDIA (CUDA):**
```bash
cd ~/llama.cpp
make clean
make LLAMA_CUDA=1

# Run with all layers on GPU
N_GPU_LAYERS=-1 ./run-server.sh
```

**Apple Silicon (Metal):**
Metal support is automatic on macOS:
```bash
N_GPU_LAYERS=-1 ./run-server.sh
```

### CPU Optimization

```bash
# Use all CPU cores
export OMP_NUM_THREADS=$(nproc)
./run-server.sh
```

## Memory Requirements

| Model Size | Q4_K_M | Q5_K_M | Q8_0 | F16 |
|------------|--------|--------|------|-----|
| 3B | 2GB | 2.5GB | 3.5GB | 6GB |
| 7B | 4GB | 5GB | 7GB | 14GB |
| 13B | 8GB | 10GB | 13GB | 26GB |
| 34B | 20GB | 25GB | 34GB | 68GB |
| 70B | 40GB | 50GB | 70GB | 140GB |

## Comparison with Other Solutions

### vs Ollama
- **llama.cpp**: More control, slightly better performance, manual setup
- **Ollama**: Easier setup, better model management, simpler API

### vs Transformers
- **llama.cpp**: 2-4x faster, much lower memory, better CPU performance
- **Transformers**: More features (training/fine-tuning), more models, Python ecosystem

## Further Reading

- [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp)
- [GGUF Format Specification](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)
- [TheBloke's GGUF Models](https://huggingface.co/TheBloke)
- [Server Documentation](https://github.com/ggerganov/llama.cpp/tree/master/examples/server)
