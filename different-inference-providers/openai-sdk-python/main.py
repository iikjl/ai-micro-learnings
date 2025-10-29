#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "openai>=1.0.0",
#     "python-dotenv>=1.0.0",
# ]
# ///
"""
OpenAI SDK Python Example

Demonstrates how to use the official OpenAI Python SDK for chat completions.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    # Load environment variables
    load_dotenv()

    # Initialize OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable not set. "
            "Please set it in your .env file."
        )

    client = OpenAI(api_key=api_key)

    print("OpenAI SDK Python Example\n")
    print("=" * 50 + "\n")

    # Example 1: Basic chat completion
    print("Example 1: Basic Chat Completion")
    print("-" * 50)
    basic_chat_completion(client)

    print("\n")

    # Example 2: Chat with custom parameters
    print("Example 2: Custom Parameters")
    print("-" * 50)
    custom_parameters(client)

    print("\n")

    # Example 3: Streaming response
    print("Example 3: Streaming Response")
    print("-" * 50)
    streaming_response(client)

    print("\n")

    # Example 4: Prompt caching
    print("Example 4: Prompt Caching")
    print("-" * 50)
    prompt_caching_example(client)


def basic_chat_completion(client: OpenAI):
    """Basic chat completion with default parameters."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"},
        ],
    )

    print(f"Response ID: {response.id}")
    print(f"Model: {response.model}")
    print(f"Assistant: {response.choices[0].message.content}")

    if response.usage:
        print("\nToken Usage:")
        print(f"  Prompt tokens: {response.usage.prompt_tokens}")
        print(f"  Completion tokens: {response.usage.completion_tokens}")
        print(f"  Total tokens: {response.usage.total_tokens}")


def custom_parameters(client: OpenAI):
    """Chat completion with various custom parameters."""
    print("Request Parameters:")
    print("  Model: gpt-3.5-turbo")
    print("  Temperature: 0.9 (high creativity)")
    print("  Max Tokens: 150")
    print("  Top P: 0.95 (nucleus sampling)")
    print("  Frequency Penalty: 0.5 (reduce repetition)")
    print("  Presence Penalty: 0.3 (encourage new topics)")
    print()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": "Tell me a very short story about a robot."},
        ],
        temperature=0.9,
        max_tokens=150,
        top_p=0.95,
        frequency_penalty=0.5,
        presence_penalty=0.3,
    )

    print(f"Assistant: {response.choices[0].message.content}")
    print(f"\nFinish Reason: {response.choices[0].finish_reason}")

    if response.usage:
        print(f"Total Tokens: {response.usage.total_tokens}")


def streaming_response(client: OpenAI):
    """Demonstrate streaming responses for real-time output."""
    print("Streaming response (Assistant): ", end="", flush=True)

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Count from 1 to 5 with a word after each number.",
            },
        ],
        max_tokens=100,
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print("\n\nStreaming complete!")


def prompt_caching_example(client: OpenAI):
    """Demonstrate prompt caching with a large context."""
    print("Prompt caching reduces costs and latency by reusing large contexts.")
    print("Requires: 1024+ token prefix that stays the same across requests\n")

    # Create a long context document (>1024 tokens)
    # This simulates a large knowledge base, documentation, or conversation history
    long_context = """
You are an AI assistant with detailed knowledge about Python programming.

Here is comprehensive documentation about Python:

Python is a high-level, interpreted programming language known for its simplicity
and readability. Created by Guido van Rossum and first released in 1991, Python
emphasizes code readability with its notable use of significant indentation.

KEY FEATURES:
1. Dynamic Typing: Variables don't need explicit type declarations
2. Automatic Memory Management: Built-in garbage collection
3. Extensive Standard Library: "Batteries included" philosophy
4. Multi-paradigm: Supports procedural, object-oriented, and functional programming
5. Cross-platform: Runs on Windows, macOS, Linux, and many other platforms

CORE CONCEPTS:

Variables and Data Types:
- Numbers: int, float, complex
- Sequences: list, tuple, range
- Text: str
- Mappings: dict
- Sets: set, frozenset
- Boolean: bool
- Binary: bytes, bytearray, memoryview

Control Flow:
- if/elif/else statements
- for loops (with iterable objects)
- while loops
- break and continue statements
- pass statement for empty blocks

Functions:
- Defined with 'def' keyword
- Support default arguments
- Support keyword arguments
- Support variable-length arguments (*args, **kwargs)
- First-class objects (can be passed around)
- Lambda functions for simple operations

Object-Oriented Programming:
- Classes defined with 'class' keyword
- Inheritance and multiple inheritance
- Special methods (__init__, __str__, __repr__, etc.)
- Properties and decorators
- Class and static methods

Exception Handling:
- try/except/else/finally blocks
- Multiple exception types
- Custom exceptions
- Context managers (with statement)

Common Built-in Functions:
- print(): Output to console
- len(): Get length of sequence
- range(): Generate number sequences
- enumerate(): Get index and value
- zip(): Combine iterables
- map(): Apply function to iterable
- filter(): Filter iterable by condition
- sorted(): Sort sequences
- sum(), min(), max(): Aggregate operations

Popular Libraries:
- NumPy: Numerical computing
- Pandas: Data analysis
- Matplotlib: Plotting and visualization
- Requests: HTTP library
- Flask/Django: Web frameworks
- TensorFlow/PyTorch: Machine learning
- Scikit-learn: Machine learning algorithms
- Beautiful Soup: Web scraping
- SQLAlchemy: Database ORM

Best Practices:
1. Follow PEP 8 style guide
2. Use meaningful variable names
3. Write docstrings for functions and classes
4. Handle exceptions appropriately
5. Use list comprehensions when appropriate
6. Avoid global variables
7. Use virtual environments
8. Write unit tests
9. Keep functions small and focused
10. Use type hints for better code clarity

File I/O:
- open() function with modes (r, w, a, rb, wb)
- Context managers for automatic file closing
- Reading: read(), readline(), readlines()
- Writing: write(), writelines()
- Working with CSV, JSON, XML files

Advanced Features:
- Generators and iterators
- Decorators for function modification
- Context managers (__enter__ and __exit__)
- Metaclasses for class customization
- Async/await for asynchronous programming
- Type hints and static type checking

Python 3 Improvements:
- Print is a function
- Integer division returns float
- Unicode strings by default
- Better exception handling
- Async/await syntax
- Type hints support
- F-strings for formatting
- Walrus operator (:=)
- Positional-only parameters
"""

    # First request - will cache the long context
    print("Making first request (will create cache)...")
    messages = [
        {"role": "system", "content": long_context},
        {"role": "user", "content": "What are the main data types in Python?"},
    ]

    response1 = client.chat.completions.create(
        model="gpt-4o-mini",  # gpt-4o models support prompt caching
        messages=messages,
    )

    print(f"Answer: {response1.choices[0].message.content[:100]}...\n")

    # Show token usage for first request
    if response1.usage:
        print("First Request Token Usage:")
        print(f"  Prompt tokens: {response1.usage.prompt_tokens}")
        print(f"  Completion tokens: {response1.usage.completion_tokens}")

        # Check for cached tokens in the response
        if hasattr(response1.usage, "prompt_tokens_details"):
            details = response1.usage.prompt_tokens_details
            if hasattr(details, "cached_tokens"):
                print(f"  Cached tokens: {details.cached_tokens}")
        print()

    # Second request - same context, different question (will use cache)
    print("Making second request with same context (should use cache)...")
    messages[1] = {
        "role": "user",
        "content": "What are some best practices for Python programming?",
    }

    response2 = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    print(f"Answer: {response2.choices[0].message.content[:100]}...\n")

    # Show token usage for second request (should show cache hit)
    if response2.usage:
        print("Second Request Token Usage:")
        print(f"  Prompt tokens: {response2.usage.prompt_tokens}")
        print(f"  Completion tokens: {response2.usage.completion_tokens}")

        # Check for cached tokens
        if hasattr(response2.usage, "prompt_tokens_details"):
            details = response2.usage.prompt_tokens_details
            if hasattr(details, "cached_tokens"):
                print(f"  Cached tokens: {details.cached_tokens}")
                if details.cached_tokens > 0:
                    print(
                        f"\n✓ Cache hit! Saved {details.cached_tokens} tokens from cache"
                    )
                    print("  This reduces both cost (~50% discount) and latency!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
