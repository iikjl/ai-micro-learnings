#!/bin/bash
# llama.cpp Server Setup and Run Script
#
# This script helps set up and run a llama.cpp server for local inference.
# llama.cpp is a high-performance C++ inference engine for LLMs.

set -e  # Exit on error

echo "llama.cpp Server Setup"
echo "======================"
echo

# Configuration
LLAMA_CPP_DIR="${LLAMA_CPP_DIR:-$HOME/llama.cpp}"
MODEL_DIR="${MODEL_DIR:-./models}"
MODEL_NAME="${MODEL_NAME:-Qwen2.5-3B-Instruct-Q4_K_M.gguf}"
MODEL_URL="${MODEL_URL:-https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf}"
PORT="${PORT:-8080}"
CONTEXT_SIZE="${CONTEXT_SIZE:-2048}"
N_GPU_LAYERS="${N_GPU_LAYERS:-0}"  # 0 = CPU only, -1 = all layers on GPU

# Function to check if llama.cpp is installed
check_llama_cpp() {
    if [ -d "$LLAMA_CPP_DIR" ]; then
        echo "✓ llama.cpp found at: $LLAMA_CPP_DIR"
        return 0
    else
        echo "✗ llama.cpp not found at: $LLAMA_CPP_DIR"
        return 1
    fi
}

# Function to install llama.cpp
install_llama_cpp() {
    echo "Installing llama.cpp..."
    echo

    # Clone repository
    git clone https://github.com/ggerganov/llama.cpp "$LLAMA_CPP_DIR"
    cd "$LLAMA_CPP_DIR"

    # Build
    echo "Building llama.cpp..."
    make

    # Build with CUDA support (optional, requires NVIDIA GPU and CUDA toolkit)
    # make LLAMA_CUDA=1

    # Build with Metal support (macOS, automatic GPU acceleration)
    # Already enabled by default on macOS

    echo "✓ llama.cpp installed successfully"
    cd -
}

# Function to download model
download_model() {
    mkdir -p "$MODEL_DIR"

    if [ -f "$MODEL_DIR/$MODEL_NAME" ]; then
        echo "✓ Model already downloaded: $MODEL_DIR/$MODEL_NAME"
        return 0
    fi

    echo "Downloading model: $MODEL_NAME"
    echo "This may take a while (model is ~2-3GB for 3B models)..."
    echo

    # Download using wget or curl
    if command -v wget &> /dev/null; then
        wget -O "$MODEL_DIR/$MODEL_NAME" "$MODEL_URL"
    elif command -v curl &> /dev/null; then
        curl -L -o "$MODEL_DIR/$MODEL_NAME" "$MODEL_URL"
    else
        echo "Error: Neither wget nor curl found. Please install one of them."
        exit 1
    fi

    echo "✓ Model downloaded successfully"
}

# Function to start server
start_server() {
    local model_path="$MODEL_DIR/$MODEL_NAME"

    # Get the absolute path to the model before changing directories
    # Save current directory
    local original_dir="$PWD"

    # Convert model path to absolute if it's relative
    if [[ "$model_path" != /* ]]; then
        model_path="$original_dir/$model_path"
    fi

    echo
    echo "Starting llama.cpp server..."
    echo "Configuration:"
    echo "  Model: $model_path"
    echo "  Port: $PORT"
    echo "  Context Size: $CONTEXT_SIZE"
    echo "  GPU Layers: $N_GPU_LAYERS"
    echo

    cd "$LLAMA_CPP_DIR"

    # Check for server executable (newer versions use llama-server in build/bin/)
    if [ -f "./build/bin/llama-server" ]; then
        SERVER_BIN="./build/bin/llama-server"
    elif [ -f "./llama-server" ]; then
        SERVER_BIN="./llama-server"
    elif [ -f "./server" ]; then
        SERVER_BIN="./server"
    else
        echo "Error: Server executable not found!"
        echo "Please rebuild llama.cpp:"
        echo "  cd $LLAMA_CPP_DIR"
        echo "  make clean && make"
        exit 1
    fi

    echo "Using server executable: $SERVER_BIN"
    echo

    # Start server with specified parameters
    "$SERVER_BIN" \
        -m "$model_path" \
        --port "$PORT" \
        --host 0.0.0.0 \
        --ctx-size "$CONTEXT_SIZE" \
        -ngl "$N_GPU_LAYERS" \
        --log-disable

    # Additional useful parameters:
    # -ngl N              : Number of GPU layers (use -1 for all, 0 for CPU only)
    # --threads N         : Number of threads to use
    # --n-predict N       : Max tokens to predict (default: 128)
    # --temp N            : Temperature (default: 0.8)
    # --top-k N           : Top-k sampling (default: 40)
    # --top-p N           : Top-p sampling (default: 0.9)
    # --repeat-penalty N  : Repeat penalty (default: 1.1)
}

# Main script
main() {
    # Check if llama.cpp is installed
    if ! check_llama_cpp; then
        echo
        read -p "Would you like to install llama.cpp? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            install_llama_cpp
        else
            echo "Please install llama.cpp manually from: https://github.com/ggerganov/llama.cpp"
            exit 1
        fi
    fi

    # Check if model exists
    if [ ! -f "$MODEL_DIR/$MODEL_NAME" ]; then
        echo
        read -p "Would you like to download the model? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            download_model
        else
            echo "Please download a GGUF model manually."
            echo "Place it in: $MODEL_DIR/$MODEL_NAME"
            exit 1
        fi
    fi

    # Start server
    start_server
}

# Help message
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    cat << EOF
Usage: $0 [options]

Environment Variables:
  LLAMA_CPP_DIR     Directory where llama.cpp is installed (default: ~/llama.cpp)
  MODEL_DIR         Directory for models (default: ./models)
  MODEL_NAME        Name of the model file (default: Qwen2.5-3B-Instruct-Q4_K_M.gguf)
  MODEL_URL         URL to download model from (default: Qwen2.5-3B-Instruct GGUF)
  PORT              Server port (default: 8080)
  CONTEXT_SIZE      Context window size (default: 2048)
  N_GPU_LAYERS      Number of GPU layers, -1 for all, 0 for CPU (default: 0)

Examples:
  # Run with defaults (CPU only)
  $0

  # Run with GPU acceleration (all layers)
  N_GPU_LAYERS=-1 $0

  # Use custom port
  PORT=8000 $0

  # Use different model (Qwen2.5 7B)
  MODEL_NAME=qwen2.5-7b-instruct-q4_k_m.gguf \\
  MODEL_URL=https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-GGUF/resolve/main/qwen2.5-7b-instruct-q4_k_m.gguf \\
  $0

EOF
    exit 0
fi

# Run main
main
