#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "transformers>=4.30.0",
#     "torch>=2.0.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
Hugging Face Transformers Example

Demonstrates local model inference using the transformers library.
This example downloads and runs models entirely on your local machine.
"""

from pathlib import Path

from dotenv import load_dotenv

try:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
except ImportError:
    print("Error: transformers and/or torch not installed.")
    print("Install with: uv pip install transformers torch")
    exit(1)


def is_model_cached(model_name: str) -> bool:
    """Check if a model is already cached locally."""
    cache_dir = Path.home() / ".cache" / "huggingface" / "hub"

    # Convert model name to cache format (e.g., "Qwen/Qwen2.5-3B-Instruct" -> "models--Qwen--Qwen2.5-3B-Instruct")
    cache_name = "models--" + model_name.replace("/", "--")
    model_cache_path = cache_dir / cache_name

    return model_cache_path.exists() and any(model_cache_path.iterdir())


def main():
    # Load environment variables
    load_dotenv()

    print("Hugging Face Transformers Local Inference Example\n")
    print("=" * 60 + "\n")

    # Check for GPU availability
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    if device == "cpu":
        print(
            "WARNING: No GPU detected. Inference will be slow.\n"
            "Consider using a GPU or smaller models.\n"
        )

    # Use a modern, efficient model for demonstration
    # Qwen2.5-3B-Instruct is a high-quality, efficient model with good performance
    # Alternative: microsoft/phi-3-mini-4k-instruct (3.8B parameters)
    model_name = "Qwen/Qwen2.5-3B-Instruct"
    print(f"Model: {model_name}")

    # Check if model is already cached
    if is_model_cached(model_name):
        print("✓ Model found in cache, will load from local storage.\n")
    else:
        print(
            "Note: Model not found in cache. First run will download ~6GB model.\n"
            "Subsequent runs will use cached model.\n"
        )

    print(
        "For faster testing, use: facebook/opt-125m\n"
        "For better quality, use: Qwen/Qwen2.5-7B-Instruct or microsoft/phi-4\n"
    )

    # Example 1: Basic text generation
    print("Example 1: Basic Text Generation")
    print("-" * 60)
    basic_generation(model_name, device)

    print("\n")

    # Example 2: Chat-style interaction
    print("Example 2: Pipeline API (Simpler Interface)")
    print("-" * 60)
    pipeline_generation(model_name, device)

    print("\n")

    # Example 3: Custom generation parameters
    print("Example 3: Custom Generation Parameters")
    print("-" * 60)
    custom_parameters_generation(model_name, device)


def basic_generation(model_name: str, device: str):
    """Basic text generation with explicit model/tokenizer loading."""
    if is_model_cached(model_name):
        print("Loading model and tokenizer from cache...")
    else:
        print("Downloading and loading model (this may take a while)...")

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    model.to(device)

    print("Model loaded successfully!\n")

    # Prepare input
    prompt = "The capital of France is"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    print(f"Prompt: {prompt}")
    print("Generating...\n")

    # Generate
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=50,
            do_sample=True,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
        )

    # Decode output
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Generated: {generated_text}")

    # Show token count
    print(f"\nInput tokens: {inputs['input_ids'].shape[1]}")
    print(f"Total output tokens: {outputs.shape[1]}")


def pipeline_generation(model_name: str, device: str):
    """Using the simpler pipeline API."""
    if is_model_cached(model_name):
        print("Creating text generation pipeline from cached model...")
    else:
        print("Creating text generation pipeline (downloading model if needed)...")

    # Create pipeline
    generator = pipeline(
        "text-generation",
        model=model_name,
        device=0 if device == "cuda" else -1,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    )

    print("Pipeline ready!\n")

    prompt = "In a world where robots have feelings,"
    print(f"Prompt: {prompt}")
    print("Generating...\n")

    # Generate
    outputs = generator(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.8,
        num_return_sequences=1,
    )

    print(f"Generated: {outputs[0]['generated_text']}")


def custom_parameters_generation(model_name: str, device: str):
    """Demonstrate various generation parameters."""
    if is_model_cached(model_name):
        print("Loading model with custom parameters from cache...\n")
    else:
        print("Loading model with custom parameters (downloading if needed)...\n")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    model.to(device)

    prompt = "Once upon a time"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    print("Generation Parameters:")
    print("  Temperature: 0.9 (high creativity)")
    print("  Top-k: 50 (consider top 50 tokens)")
    print("  Top-p: 0.95 (nucleus sampling)")
    print("  Repetition Penalty: 1.2 (discourage repetition)")
    print("  Max New Tokens: 100")
    print()

    print(f"Prompt: {prompt}")
    print("Generating...\n")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.9,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Generated: {generated_text}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        exit(0)
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        exit(1)
