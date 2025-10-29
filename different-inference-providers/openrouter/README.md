# OpenRouter Example (JavaScript/Node.js)

Learn how to use OpenRouter to access 100+ AI models from multiple providers through a unified API. Perfect for experimenting with different models.

## Environment Variables

Add to your root `.env` file:
```bash
OPENROUTER_API_KEY=sk-or-...your-key-here...
```

Get your API key at: https://openrouter.ai (free signup available)

## Dependencies

Install Node.js dependencies from the parent directory:
```bash
# From different-inference-providers directory
npm install
```

Dependencies (defined in `package.json`):
- `openai` - OpenAI SDK (compatible with OpenRouter)
- `dotenv` - Environment variable loading

## Running the Example

```bash
# From this directory
node main.js

# Or from parent directory
npm run openrouter
```

## What You'll Learn

This example demonstrates:

1. **Basic Chat Completion** - Using OpenRouter with OpenAI SDK
2. **Comparing Different Models** - Easy model switching with one parameter
3. **Streaming Response** - Real-time token streaming

## Key Configuration Options

| Parameter | Description |
|-----------|-------------|
| `model` | Choose from 100+ models (see https://openrouter.ai/models) |
| `temperature` | 0.0-2.0 - Randomness control |
| `max_tokens` | Maximum response length |
| `top_p` | Nucleus sampling threshold |
| `route` | `fallback`, `fastest`, or `cheapest` for automatic routing |

## Popular Models

**Free Models (Great for Development):**
- `z-ai/glm-4.5-air:free` - Reasoning model with thinking process
- `meta-llama/llama-3.1-8b-instruct:free` - Fast, capable
- `mistralai/mistral-7b-instruct:free` - Good for general tasks

**Paid Models (Production Quality):**
- `openai/gpt-4-turbo` - Most capable
- `anthropic/claude-3-sonnet` - Excellent reasoning
- `google/gemini-pro-1.5` - Large context (2M tokens)

## Why OpenRouter?

**Advantages:**
- Access 100+ models through one API
- Switch models by changing one parameter
- Free models for development
- Unified billing across providers
- Automatic fallback options

**Disadvantages:**
- Small additional latency
- Limited provider-specific features
- Depends on OpenRouter service

## Further Reading

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Model List](https://openrouter.ai/models)
- [Pricing](https://openrouter.ai/docs/pricing)
