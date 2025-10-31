# OpenAI Raw HTTP Example (Rust)

Learn how to interact with the OpenAI API using raw HTTP requests in Rust. This approach gives you complete control over requests and deep understanding of the API structure.

## Environment Variables

Add to your root `.env` file:
```bash
OPENAI_API_KEY=sk-...your-key-here...
```

Get your API key at: https://platform.openai.com/api-keys

## Dependencies

Rust dependencies are managed by Cargo (defined in `Cargo.toml`):
- `reqwest` - HTTP client
- `tokio` - Async runtime
- `serde` / `serde_json` - JSON serialization
- `dotenv` - Environment variable loading

## Running the Example

```bash
# From this directory
cargo run

# Or from parent directory
cargo run -p openai-raw-http
```

## What You'll Learn

This example demonstrates:

1. **Basic Non-Streaming Request** - Simple chat with system and user messages
2. **Custom Parameters** - Temperature, max tokens, top-p, frequency/presence penalties

## Key API Details

**Endpoint:** `POST https://api.openai.com/v1/chat/completions`

**Headers:**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**Key Parameters:**

| Parameter | Range | Description |
|-----------|-------|-------------|
| `model` | - | `gpt-3.5-turbo`, `gpt-4`, etc. |
| `messages` | - | Array with roles: system, user, assistant |
| `temperature` | 0.0-2.0 | Randomness (0=deterministic, 2=creative) |
| `max_tokens` | 1-4096+ | Maximum tokens to generate |
| `top_p` | 0.0-1.0 | Nucleus sampling |
| `frequency_penalty` | -2.0 to 2.0 | Reduce repetition |
| `presence_penalty` | -2.0 to 2.0 | Encourage new topics |

## Why Raw HTTP?

**Advantages:**
- Complete control over requests
- No SDK dependencies
- Learn API structure deeply
- Easy debugging

**Disadvantages:**
- More boilerplate code
- Manual error handling and retries
- Must track API changes yourself

## Further Reading

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/chat)
- [Models Overview](https://platform.openai.com/docs/models)
