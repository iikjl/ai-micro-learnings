#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "ollama>=0.1.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
Ollama Python SDK Example

Demonstrates how to use Ollama for local model inference with Python.
Ollama makes it easy to run and manage LLMs locally.
"""

import os

from dotenv import load_dotenv

try:
    import ollama
except ImportError:
    print("Error: ollama package not installed.")
    print("Install with: uv pip install ollama")
    exit(1)


def main():
    # Load environment variables
    load_dotenv()

    # Get Ollama host (defaults to localhost)
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    print("Ollama Python SDK Example\n")
    print("=" * 60 + "\n")
    print(f"Ollama Host: {host}\n")

    # Create client
    client = ollama.Client(host=host)

    # Check if Ollama is running and models are available
    try:
        models = client.list()
        if not models.get("models"):
            print("No models found! Please pull a model first:")
            print("  ollama pull qwen2.5:3b")
            print("  ollama pull phi4")
            exit(1)

        print("Available models:")
        model_names = [model["name"] for model in models["models"]]
        for name in model_names:
            print(f"  - {name}")
        print()
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
        print("\nMake sure Ollama is running:")
        print("  - Install from: https://ollama.ai")
        print("  - Run: ollama serve")
        exit(1)

    # Use a modern, efficient model for demonstration
    # Qwen2.5:3b is a newer, high-quality model with good performance
    model_name = "qwen2.5:3b"

    # Check if the specific model we want to use is available
    if model_name not in model_names:
        print(f"Warning: Model '{model_name}' not found locally.")
        print("To use this example, please pull the model first:")
        print(f"  ollama pull {model_name}")
        print("\nOr you can use one of the available models listed above.")
        exit(1)
    else:
        print(f"✓ Using model: {model_name} (already downloaded)\n")

    # Example 1: Basic chat completion
    print("Example 1: Basic Chat Completion")
    print("-" * 60)
    basic_chat(client, model_name)

    print("\n")

    # Example 2: Chat with custom options
    print("Example 2: Custom Options")
    print("-" * 60)
    custom_options(client, model_name)

    print("\n")

    # Example 3: Streaming response
    print("Example 3: Streaming Response")
    print("-" * 60)
    streaming_chat(client, model_name)


def basic_chat(client: ollama.Client, model: str):
    """Basic chat completion."""
    print(f"Using model: {model}\n")

    response = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"},
        ],
    )

    print(f"Assistant: {response['message']['content']}")

    # Show token counts if available
    if "eval_count" in response:
        print(f"\nTokens generated: {response['eval_count']}")
    if "prompt_eval_count" in response:
        print(f"Prompt tokens: {response['prompt_eval_count']}")


def custom_options(client: ollama.Client, model: str):
    """Chat with custom generation options."""
    print("Request Options:")
    print("  Temperature: 0.9 (high creativity)")
    print("  Top K: 50")
    print("  Top P: 0.95")
    print("  Repeat Penalty: 1.2")
    print()

    response = client.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {
                "role": "user",
                "content": "Tell me a very short story about a robot in one paragraph.",
            },
        ],
        options={
            "temperature": 0.9,
            "top_k": 50,
            "top_p": 0.95,
            "repeat_penalty": 1.2,
            "num_predict": 150,  # Max tokens to generate
        },
    )

    print(f"Assistant: {response['message']['content']}")

    if "eval_count" in response:
        print(f"\nTokens generated: {response['eval_count']}")


def streaming_chat(client: ollama.Client, model: str):
    """Demonstrate streaming responses."""
    print("Streaming response (Assistant): ", end="", flush=True)

    stream = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Count from 1 to 5 with a word after each number.",
            }
        ],
        stream=True,
        options={"num_predict": 100},
    )

    for chunk in stream:
        if "message" in chunk and "content" in chunk["message"]:
            print(chunk["message"]["content"], end="", flush=True)

    print("\n\nStreaming complete!")


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
