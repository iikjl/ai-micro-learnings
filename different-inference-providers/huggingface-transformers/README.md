# Hugging Face Transformers Local Inference

Learn how to run AI models entirely on your local machine using the Hugging Face Transformers library. Complete privacy, no API costs, offline capability.

## Environment Variables

Optional, for private models or increased rate limits:
```bash
HF_TOKEN=hf_...your-token-here...
```

Get token at: https://huggingface.co/settings/tokens

## Dependencies

### Install PyTorch

```bash
# CPU version
pip install torch

# OR for NVIDIA GPU (CUDA 11.8)
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Install Transformers

```bash
pip install transformers

# Or install all dependencies
pip install -r ../requirements.txt
```

## Running the Example

```bash
python main.py
```

**First run downloads the model** (~6GB for Qwen2.5-3B). Subsequent runs use cached model.

## What You'll Learn

This example demonstrates:

1. **Basic Text Generation** - Explicit model and tokenizer loading with GPU/CPU selection
2. **Pipeline API** - Simpler high-level interface for common tasks
3. **Custom Generation Parameters** - Temperature, top-k, top-p, repetition penalty

## Hardware Requirements

| Model Size | RAM | GPU VRAM | Inference Speed |
|------------|-----|----------|-----------------|
| Small (125M-1B) | 4GB | Optional | Fast on CPU |
| Medium (3B-7B) | 16GB | 8GB+ | GPU recommended |
| Large (13B-34B) | 32GB+ | 24GB+ | GPU required |
| Very Large (70B+) | 64GB+ | 80GB+ | Multi-GPU required |

## Key Configuration Options

| Parameter | Range | Description |
|-----------|-------|-------------|
| `model_name` | - | Any model from HuggingFace Hub |
| `temperature` | 0.0-2.0 | Randomness (0=deterministic, 2=creative) |
| `max_new_tokens` | 1-4096+ | Maximum tokens to generate |
| `top_k` | 1-100 | Top-k sampling (1=greedy, 50=balanced) |
| `top_p` | 0.0-1.0 | Nucleus sampling threshold |
| `repetition_penalty` | 1.0-2.0 | Discourage repetition (1.0=no penalty) |
| `do_sample` | boolean | Enable sampling vs greedy decoding |

## Recommended Models

| Model | Parameters | RAM | VRAM | Quality | License |
|-------|------------|-----|------|---------|---------|
| `Qwen/Qwen2.5-3B-Instruct` | 3B | 8GB | 4GB | Excellent | Apache 2.0 |
| `microsoft/phi-3-mini-4k-instruct` | 3.8B | 8GB | 4GB | Excellent | MIT |
| `microsoft/phi-4` | 14B | 16GB | 8GB | Excellent | MIT |
| `Qwen/Qwen2.5-7B-Instruct` | 7B | 16GB | 8GB | Excellent | Apache 2.0 |
| `mistralai/Mistral-7B-Instruct-v0.2` | 7B | 16GB | 8GB | Good | Apache 2.0 |
| `facebook/opt-125m` | 125M | 2GB | 1GB | Demo only | MIT |

## Quantization for Lower Memory

Reduce memory usage with quantization:

```python
from transformers import BitsAndBytesConfig

# 8-bit quantization (halves VRAM)
quantization_config = BitsAndBytesConfig(load_in_8bit=True)

# 4-bit quantization (quarters VRAM)
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)
```

## Why Local Inference?

**Advantages:**
- Complete privacy - data never leaves your machine
- No API costs - free after hardware investment
- Offline capability - works without internet
- No rate limits - hardware is the only limit
- Full control - customize everything

**Disadvantages:**
- Hardware cost - need powerful GPU
- Setup complexity - model management required
- Quality - open models may lag behind GPT-4
- Speed - slower than cloud inference
- Maintenance - keep models updated

## Performance Tips

1. **Use GPU**: 10-100x faster than CPU
2. **Half Precision (FP16)**: Halves memory usage with minimal quality loss
3. **Quantization**: Use 4-bit/8-bit for large models
4. **Smaller Models**: Start with 1B-3B for development

## Model Caching

Models are cached at:
- Linux/Mac: `~/.cache/huggingface/hub/`
- Windows: `C:\Users\{username}\.cache\huggingface\hub\`

## Further Reading

- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Model Hub](https://huggingface.co/models)
- [Generation Strategies](https://huggingface.co/docs/transformers/generation_strategies)
- [Quantization Guide](https://huggingface.co/docs/transformers/main_classes/quantization)
