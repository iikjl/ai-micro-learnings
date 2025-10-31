#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "google-genai>=0.2.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
Google Gemini API Example

Demonstrates how to use Google's Gemini API via the GenAI SDK for chat completions.
"""

import os

from dotenv import load_dotenv

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai package not installed.")
    print("Install it with: uv pip install google-genai")
    exit(1)


def main():
    # Load environment variables
    load_dotenv()

    # Get API key
    api_key = os.getenv("GOOGLE_CLOUD_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_CLOUD_API_KEY environment variable not set. "
            "Please set it in your .env file."
        )

    print("Google Gemini API Example\n")
    print("=" * 50 + "\n")

    # Initialize Gemini client with API key
    # Note: Use vertexai=False (or omit it) when using API keys
    # vertexai=True requires OAuth2/service account credentials
    client = genai.Client(
        api_key=api_key,
    )

    # Example 1: Basic chat completion
    print("Example 1: Basic Chat Completion")
    print("-" * 50)
    basic_chat_completion(client)

    print("\n")

    # Example 2: Custom generation parameters with safety settings
    print("Example 2: Custom Generation Parameters")
    print("-" * 50)
    custom_parameters(client)

    print("\n")

    # Example 3: Streaming response with thinking mode
    print("Example 3: Streaming Response with Thinking Mode")
    print("-" * 50)
    streaming_with_thinking(client)


def basic_chat_completion(client):
    """Basic chat completion with Gemini API using structured Content."""
    model = "gemini-2.0-flash-exp"

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text="What is the capital of France?")],
        ),
    ]

    config = types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=100,
        top_p=0.95,
    )

    print(f"Model: {model}\n")

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=config,
    )

    print(f"Assistant: {response.text}")

    # Gemini API provides usage metadata
    if hasattr(response, "usage_metadata"):
        print("\nToken Usage:")
        print(f"  Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"  Completion tokens: {response.usage_metadata.candidates_token_count}")
        print(f"  Total tokens: {response.usage_metadata.total_token_count}")


def custom_parameters(client):
    """Chat completion with custom generation parameters and safety settings."""
    model = "gemini-2.0-flash-exp"

    print("Request Parameters:")
    print(f"  Model: {model}")
    print("  Temperature: 1.0 (high creativity)")
    print("  Max Output Tokens: 500")
    print("  Top P: 0.95")
    print("  Seed: 0 (for reproducibility)")
    print("  Safety Settings: All OFF")
    print()

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="Tell me a very short story about a robot discovering emotions."
                )
            ],
        ),
    ]

    config = types.GenerateContentConfig(
        temperature=1.0,
        top_p=0.95,
        seed=0,
        max_output_tokens=500,
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"
            ),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
        ],
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=config,
    )

    print(f"Assistant: {response.text}")

    if hasattr(response, "usage_metadata"):
        print(f"\nTotal Tokens: {response.usage_metadata.total_token_count}")


def streaming_with_thinking(client):
    """Demonstrate streaming responses with thinking mode."""
    # Note: Thinking mode requires specific models that support it
    model = "gemini-2.0-flash-thinking-exp-01-21"

    print(f"Model: {model}")
    print("Streaming response with extended thinking...\n")
    print("Assistant: ", end="", flush=True)

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="Solve this problem step by step: If a train travels at 60 mph for 2.5 hours, how far does it travel?"
                )
            ],
        ),
    ]

    config = types.GenerateContentConfig(
        temperature=1.0,
        top_p=0.95,
        seed=0,
        max_output_tokens=8192,
        safety_settings=[
            types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"
            ),
            types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
        ],
        thinking_config=types.ThinkingConfig(
            thinking_budget=-1,  # Extended thinking
        ),
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=config,
    ):
        if chunk.text:
            print(chunk.text, end="", flush=True)

    print("\n\nStreaming complete!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        exit(1)
