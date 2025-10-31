# OpenAI SDK Python Example

Learn how to use the official OpenAI Python SDK for chat completions with examples covering basic chat, custom parameters, streaming, and prompt caching.

## Environment Variables

Add to your root `.env` file:
```bash
OPENAI_API_KEY=sk-...your-key-here...
```

Get your API key at: https://platform.openai.com/api-keys

## Dependencies

This example uses [uv](https://github.com/astral-sh/uv) with inline script metadata (PEP 723). Dependencies are declared in the script and automatically managed.

Required dependencies (auto-installed by uv):
- `openai>=1.0.0`
- `python-dotenv>=1.0.0`

### Alternative: Traditional pip
```bash
pip install -r ../requirements.txt
```

## Running the Example

```bash
# Run with uv (automatically installs dependencies)
uv run main.py

# Or with traditional Python
python main.py
```

## What You'll Learn

This example demonstrates:

1. **Basic Chat Completion** - Simple request with system and user messages
2. **Custom Parameters** - Control temperature, max tokens, top-p, and penalties
3. **Streaming Response** - Real-time token-by-token output
4. **Prompt Caching** - Reduce costs (~50%) and latency for repeated contexts

## Key Configuration Options

| Parameter | Range | Description |
|-----------|-------|-------------|
| `model` | - | `gpt-4`, `gpt-4-turbo`, `gpt-3.5-turbo` |
| `temperature` | 0.0-2.0 | Randomness (0=deterministic, 2=very creative) |
| `max_tokens` | 1-4096+ | Maximum tokens to generate |
| `top_p` | 0.0-1.0 | Nucleus sampling threshold |
| `frequency_penalty` | -2.0 to 2.0 | Reduce repetition |
| `presence_penalty` | -2.0 to 2.0 | Encourage new topics |
| `stream` | boolean | Enable streaming responses |

## Further Reading

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [API Reference](https://platform.openai.com/docs/api-reference)
- [Pricing](https://openai.com/pricing)
