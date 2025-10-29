package main

import (
	"context"
	"fmt"
	"os"

	"github.com/ollama/ollama/api"
)

func main() {
	fmt.Println("Ollama Go SDK Example\n")
	fmt.Println("======================================\n")

	// Get Ollama host from environment or use default
	host := os.Getenv("OLLAMA_HOST")
	if host == "" {
		host = "http://localhost:11434"
	}
	fmt.Printf("Ollama Host: %s\n\n", host)

	// Create client
	client, err := api.ClientFromEnvironment()
	if err != nil {
		fmt.Printf("Error creating client: %v\n", err)
		fmt.Println("\nMake sure Ollama is running:")
		fmt.Println("  ollama serve")
		os.Exit(1)
	}

	// Check available models
	ctx := context.Background()
	models, err := client.List(ctx)
	if err != nil {
		fmt.Printf("Error connecting to Ollama: %v\n", err)
		fmt.Println("\nMake sure Ollama is running:")
		fmt.Println("  ollama serve")
		os.Exit(1)
	}

	if len(models.Models) == 0 {
		fmt.Println("No models found! Please pull a model first:")
		fmt.Println("  ollama pull qwen2.5:3b")
		fmt.Println("  ollama pull phi4")
		os.Exit(1)
	}

	fmt.Println("Available models:")
	modelNames := make([]string, 0, len(models.Models))
	for _, model := range models.Models {
		modelNames = append(modelNames, model.Model)
		fmt.Printf("  - %s\n", model.Model)
	}
	fmt.Println()

	// Use a modern, efficient model for demonstration
	// Qwen2.5:3b is a newer, high-quality model with good performance
	modelName := "qwen2.5:3b"

	// Check if the specific model we want to use is available
	modelFound := false
	for _, name := range modelNames {
		if name == modelName {
			modelFound = true
			break
		}
	}

	if !modelFound {
		fmt.Printf("Warning: Model '%s' not found locally.\n", modelName)
		fmt.Println("To use this example, please pull the model first:")
		fmt.Printf("  ollama pull %s\n", modelName)
		fmt.Println("\nOr you can use one of the available models listed above.")
		os.Exit(1)
	}

	fmt.Printf("✓ Using model: %s (already downloaded)\n\n", modelName)

	// Example 1: Basic chat completion
	fmt.Println("Example 1: Basic Chat Completion")
	fmt.Println("--------------------------------------------------")
	basicChat(ctx, client, modelName)

	fmt.Println("\n")

	// Example 2: Custom options
	fmt.Println("Example 2: Custom Options")
	fmt.Println("--------------------------------------------------")
	customOptions(ctx, client, modelName)

	fmt.Println("\n")

	// Example 3: Streaming response
	fmt.Println("Example 3: Streaming Response")
	fmt.Println("--------------------------------------------------")
	streamingChat(ctx, client, modelName)
}

func basicChat(ctx context.Context, client *api.Client, model string) {
	fmt.Printf("Using model: %s\n\n", model)

	req := &api.ChatRequest{
		Model: model,
		Messages: []api.Message{
			{
				Role:    "system",
				Content: "You are a helpful assistant.",
			},
			{
				Role:    "user",
				Content: "What is the capital of France?",
			},
		},
	}

	var response api.ChatResponse
	err := client.Chat(ctx, req, func(resp api.ChatResponse) error {
		response = resp
		return nil
	})

	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	fmt.Printf("Assistant: %s\n", response.Message.Content)

	if response.EvalCount > 0 {
		fmt.Printf("\nTokens generated: %d\n", response.EvalCount)
	}
	if response.PromptEvalCount > 0 {
		fmt.Printf("Prompt tokens: %d\n", response.PromptEvalCount)
	}
}

func customOptions(ctx context.Context, client *api.Client, model string) {
	fmt.Println("Request Options:")
	fmt.Println("  Temperature: 0.9 (high creativity)")
	fmt.Println("  Top K: 50")
	fmt.Println("  Top P: 0.95")
	fmt.Println("  Repeat Penalty: 1.2")
	fmt.Println()

	temperature := 0.9
	topK := 50
	topP := 0.95
	repeatPenalty := 1.2
	numPredict := 150

	req := &api.ChatRequest{
		Model: model,
		Messages: []api.Message{
			{
				Role:    "system",
				Content: "You are a creative storyteller.",
			},
			{
				Role:    "user",
				Content: "Tell me a very short story about a robot in one paragraph.",
			},
		},
		Options: map[string]interface{}{
			"temperature":    temperature,
			"top_k":          topK,
			"top_p":          topP,
			"repeat_penalty": repeatPenalty,
			"num_predict":    numPredict,
		},
	}

	var response api.ChatResponse
	err := client.Chat(ctx, req, func(resp api.ChatResponse) error {
		response = resp
		return nil
	})

	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	fmt.Printf("Assistant: %s\n", response.Message.Content)

	if response.EvalCount > 0 {
		fmt.Printf("\nTokens generated: %d\n", response.EvalCount)
	}
}

func streamingChat(ctx context.Context, client *api.Client, model string) {
	fmt.Print("Streaming response (Assistant): ")

	numPredict := 100

	req := &api.ChatRequest{
		Model: model,
		Messages: []api.Message{
			{
				Role:    "user",
				Content: "Count from 1 to 5 with a word after each number.",
			},
		},
		Options: map[string]interface{}{
			"num_predict": numPredict,
		},
	}

	err := client.Chat(ctx, req, func(resp api.ChatResponse) error {
		fmt.Print(resp.Message.Content)
		return nil
	})

	if err != nil {
		fmt.Printf("\nError: %v\n", err)
		return
	}

	fmt.Println("\n\nStreaming complete!")
}
