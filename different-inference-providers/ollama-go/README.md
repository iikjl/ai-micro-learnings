# Ollama Go SDK Example

Learn how to use Ollama for local model inference with the Go SDK. Go is excellent for building production inference services with its speed and built-in concurrency.

## Environment Variables

No API keys required! Ollama runs completely locally.

## Dependencies

### 1. Install Ollama

See the Ollama Python example README or visit https://ollama.ai for installation instructions.

### 2. Start Ollama Service

```bash
ollama serve
```

### 3. Pull a Model

```bash
# Modern, efficient models
ollama pull qwen2.5:3b
# Or
ollama pull phi4
```

### 4. Go Dependencies

Go dependencies are managed by Go modules (defined in `go.mod`):
- `github.com/ollama/ollama/api` - Official Ollama Go SDK

```bash
go mod tidy
```

## Running the Example

```bash
# Initialize Go modules (first time only)
go mod tidy

# Run the example
go run main.go

# Or build and run
go build -o ollama-example
./ollama-example
```

## What You'll Learn

This example demonstrates:

1. **Basic Chat Completion** - Creating client, sending requests, handling responses
2. **Custom Options** - Temperature, top-k, top-p, repeat penalty, token limits
3. **Streaming Response** - Real-time token streaming with callback-based handling

## Key Configuration Options

```go
options := map[string]interface{}{
    "temperature":    0.7,    // Randomness (0.0-2.0)
    "top_k":          50,     // Top-k sampling
    "top_p":          0.95,   // Nucleus sampling
    "repeat_penalty": 1.2,    // Discourage repetition
    "num_predict":    200,    // Max tokens to generate
    "stop":           []string{"\n\n"}, // Stop sequences
    "seed":           42,     // Random seed
}
```

## Why Go for Inference?

**Advantages:**
- Fast compilation and execution
- Built-in concurrency (goroutines)
- Low memory overhead
- Easy deployment (single binary)
- Strong standard library
- Great for microservices

**Use Cases:**
- Production HTTP API servers
- High-throughput batch processing
- Concurrent request handling
- Containerized services

## Building Production Services

### Example HTTP Server

```go
func main() {
    client, _ := api.ClientFromEnvironment()

    http.HandleFunc("/chat", func(w http.ResponseWriter, r *http.Request) {
        var req ChatRequest
        json.NewDecoder(r.Body).Decode(&req)

        chatReq := &api.ChatRequest{
            Model: "llama3.2:1b",
            Messages: []api.Message{
                {Role: "user", Content: req.Message},
            },
        }

        var response string
        client.Chat(ctx, chatReq, func(resp api.ChatResponse) error {
            response = resp.Message.Content
            return nil
        })

        json.NewEncoder(w).Encode(ChatResponse{Response: response})
    })

    http.ListenAndServe(":8080", nil)
}
```

## Best Practices

1. **Always use contexts** for cancellation and timeouts
2. **Handle errors explicitly** - Go encourages error checking
3. **Use goroutines** for concurrent requests
4. **Stream responses** for better UX
5. **Set appropriate timeouts** for production
6. **Monitor goroutine leaks** in long-running services

## Further Reading

- [Ollama API Documentation](https://github.com/ollama/ollama/tree/main/docs)
- [Go Ollama Package](https://pkg.go.dev/github.com/ollama/ollama/api)
- [Go Concurrency Patterns](https://go.dev/blog/pipelines)
