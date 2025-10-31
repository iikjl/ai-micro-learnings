# Google Gemini API Example

Learn how to use Google's Gemini API via the GenAI SDK with examples covering basic chat, custom parameters, and advanced thinking mode.

## Environment Variables

Add to your root `.env` file:
```bash
GOOGLE_CLOUD_API_KEY=your-api-key-here
```

Get your API key at: https://aistudio.google.com/apikey

## Dependencies

This example uses [uv](https://github.com/astral-sh/uv) with inline script metadata (PEP 723). Dependencies are declared in the script and automatically managed.

Required dependencies (auto-installed by uv):
- `google-genai>=0.2.0`
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

1. **Basic Chat Completion** - Simple request using structured Content API
2. **Custom Generation Parameters** - Temperature, max tokens, top-p, top-k, safety settings
3. **Streaming with Thinking Mode** - Real-time reasoning with Gemini 2.0 Flash Thinking

## Key Configuration Options

| Parameter | Range | Description |
|-----------|-------|-------------|
| `model` | - | `gemini-2.0-flash-exp`, `gemini-1.5-pro`, etc. |
| `temperature` | 0.0-2.0 | Randomness (0=deterministic, 2=creative) |
| `max_output_tokens` | 1-8192 | Maximum tokens to generate |
| `top_p` | 0.0-1.0 | Nucleus sampling threshold |
| `top_k` | 1-40 | Number of top tokens to consider |
| `stop_sequences` | - | Strings that stop generation |
| `safety_settings` | - | Content filtering controls |

## Unique Features

- **Massive Context Windows**: Up to 2M tokens (Gemini 1.5 Pro)
- **Multimodal Support**: Text, images, video, and audio
- **Thinking Mode**: Extended reasoning capabilities (Gemini 2.0 Flash Thinking)
- **Function Calling**: Built-in tool use support
- **Enterprise Features**: VPC, audit logs, data residency

## Further Reading

- [Google GenAI SDK](https://googleapis.github.io/python-genai/)
- [Gemini Models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
- [Pricing](https://cloud.google.com/vertex-ai/pricing)
