#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests>=2.31.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
llama.cpp Client Example

Demonstrates how to interact with a llama.cpp server using HTTP requests.
The server must be running before executing this script.
"""

import json
import os

import requests
from dotenv import load_dotenv


def main():
    # Load environment variables
    load_dotenv()

    # Get server URL
    server_url = os.getenv("LLAMA_CPP_SERVER_URL", "http://localhost:8080")

    print("llama.cpp Client Example\n")
    print("=" * 60 + "\n")
    print(f"Server URL: {server_url}\n")

    # Check if server is running
    try:
        health_check(server_url)
        print("✓ Server is running\n")
    except Exception as e:
        print(f"✗ Cannot connect to server: {e}")
        print("\nPlease start the llama.cpp server first:")
        print("  ./run-server.sh")
        return

    # Example 1: Basic completion
    print("Example 1: Basic Text Completion")
    print("-" * 60)
    basic_completion(server_url)

    print("\n")

    # Example 2: Chat-style completion
    print("Example 2: Chat Completion")
    print("-" * 60)
    chat_completion(server_url)

    print("\n")

    # Example 3: Streaming response
    print("Example 3: Streaming Response")
    print("-" * 60)
    streaming_completion(server_url)


def health_check(server_url: str):
    """Check if server is running."""
    response = requests.get(f"{server_url}/health")
    response.raise_for_status()


def basic_completion(server_url: str):
    """Basic text completion."""
    prompt = "The capital of France is"

    print(f"Prompt: {prompt}")
    print("Generating...\n")

    data = {
        "prompt": prompt,
        "n_predict": 50,
        "temperature": 0.7,
        "stop": ["\n"],
        "stream": False,
    }

    response = requests.post(f"{server_url}/completion", json=data)
    response.raise_for_status()

    result = response.json()
    generated_text = result["content"]

    print(f"Generated: {prompt}{generated_text}")

    # Show token counts
    if "tokens_predicted" in result:
        print(f"\nTokens generated: {result['tokens_predicted']}")
    if "tokens_evaluated" in result:
        print(f"Prompt tokens: {result['tokens_evaluated']}")


def chat_completion(server_url: str):
    """Chat-style completion with proper formatting."""
    print("Request Parameters:")
    print("  Temperature: 0.8")
    print("  Max Tokens: 100")
    print("  Top K: 40")
    print("  Top P: 0.9")
    print()

    # Llama 2 chat format
    system_prompt = "You are a helpful assistant."
    user_message = "Tell me a very short story about a robot in one sentence."

    # Format prompt in Llama 2 chat format
    prompt = f"""[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_message} [/INST]"""

    data = {
        "prompt": prompt,
        "n_predict": 100,
        "temperature": 0.8,
        "top_k": 40,
        "top_p": 0.9,
        "repeat_penalty": 1.1,
        "stream": False,
    }

    response = requests.post(f"{server_url}/completion", json=data)
    response.raise_for_status()

    result = response.json()
    print(f"Assistant: {result['content'].strip()}")

    if "tokens_predicted" in result:
        print(f"\nTokens generated: {result['tokens_predicted']}")


def streaming_completion(server_url: str):
    """Streaming completion for real-time output."""
    print("Streaming response (Assistant): ", end="", flush=True)

    prompt = "Count from 1 to 5 with a word after each number."

    data = {
        "prompt": prompt,
        "n_predict": 100,
        "temperature": 0.7,
        "stream": True,
    }

    response = requests.post(
        f"{server_url}/completion", json=data, stream=True, timeout=30
    )
    response.raise_for_status()

    # Process streaming response
    for line in response.iter_lines():
        if line:
            # Server sends "data: {json}" format
            line_text = line.decode("utf-8")
            if line_text.startswith("data: "):
                json_str = line_text[6:]  # Remove "data: " prefix
                try:
                    chunk = json.loads(json_str)
                    if "content" in chunk:
                        print(chunk["content"], end="", flush=True)

                    # Check if generation is complete
                    if chunk.get("stop", False):
                        break
                except json.JSONDecodeError:
                    continue

    print("\n\nStreaming complete!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
