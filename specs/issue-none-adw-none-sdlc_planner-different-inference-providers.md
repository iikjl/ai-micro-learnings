# Feature: Different Inference Providers Learning Module

## Metadata
issue_number: `none`
adw_id: `none`
issue_json: `{"title": "Different Inference Providers", "body": "Create a comprehensive learning module showcasing various AI inference providers and their capabilities"}`

## Feature Description
Create a comprehensive learning module that showcases different AI inference providers and their capabilities. This module will provide hands-on examples of how to interact with various LLM inference providers using different programming languages and approaches. The module will demonstrate OpenAI (raw HTTP and SDK), Google Vertex AI, OpenRouter, Hugging Face Transformers, Ollama, and llama.cpp, with practical, runnable code examples in Python, JavaScript, Rust, Go, and Bash.

Note: There are many more inference providers and ways to run models, but these represent some of the most common and widely-used options in the industry.

## User Story
As a developer learning about AI inference
I want to see practical examples of different inference providers and their capabilities
So that I can understand the options available and choose the right provider and approach for my use case

## Problem Statement
Developers new to AI inference often struggle to understand the landscape of available inference providers, their different capabilities, configuration options, and how to integrate them using various programming languages and SDKs. There's a need for a centralized, hands-on learning resource that demonstrates these providers side-by-side with practical, runnable examples.

## Solution Statement
Create a new `different-inference-providers` directory containing organized, runnable code examples for each major inference provider. Each example will be self-contained with clear documentation, environment variable configuration, and comparison of available settings and capabilities. The examples will span multiple programming languages to demonstrate the flexibility and different approaches available to developers.

## Relevant Files
Use these files to implement the feature:

- `.env.sample` - Contains environment variable references that will be updated with new provider API keys
- `README.md` - Will be updated to include the new learning module in the repository structure table

### New Files

The following new files will be created under `different-inference-providers/`:

- `different-inference-providers/README.md` - Main documentation for the module with overview, learning objectives, and comparison tables
- `different-inference-providers/.gitignore` - Ignore patterns for dependencies and build artifacts
- `different-inference-providers/requirements.txt` - Python dependencies
- `different-inference-providers/package.json` - JavaScript/Node.js dependencies
- `different-inference-providers/Cargo.toml` - Rust dependencies
- `different-inference-providers/go.mod` - Go dependencies

#### OpenAI Examples
- `different-inference-providers/openai-raw-http/main.rs` - Rust implementation using raw HTTP requests
- `different-inference-providers/openai-raw-http/Cargo.toml` - Rust project configuration
- `different-inference-providers/openai-raw-http/README.md` - Documentation for raw HTTP approach
- `different-inference-providers/openai-sdk-python/main.py` - Python implementation using OpenAI SDK
- `different-inference-providers/openai-sdk-python/README.md` - Documentation for Python SDK approach

#### Google Vertex AI
- `different-inference-providers/google-vertex/main.py` - Python implementation using Google Vertex AI SDK
- `different-inference-providers/google-vertex/README.md` - Documentation and setup instructions

#### OpenRouter
- `different-inference-providers/openrouter/main.js` - JavaScript/Node.js implementation using OpenAI SDK
- `different-inference-providers/openrouter/README.md` - Documentation for OpenRouter integration

#### Hugging Face
- `different-inference-providers/huggingface-transformers/main.py` - Python implementation using transformers library
- `different-inference-providers/huggingface-transformers/README.md` - Documentation and model download instructions

#### Ollama
- `different-inference-providers/ollama-python/main.py` - Python implementation using Ollama SDK
- `different-inference-providers/ollama-python/README.md` - Documentation for Python Ollama SDK
- `different-inference-providers/ollama-go/main.go` - Go implementation using Ollama SDK
- `different-inference-providers/ollama-go/README.md` - Documentation for Go Ollama SDK

#### Llama.cpp
- `different-inference-providers/llama-cpp/run-server.sh` - Bash script to start llama.cpp server
- `different-inference-providers/llama-cpp/client-example.py` - Python client to connect to llama.cpp server
- `different-inference-providers/llama-cpp/README.md` - Documentation for llama.cpp setup and usage

## Implementation Plan

### Phase 1: Foundation
Create the base directory structure and shared configuration files. Set up dependency management files for Python, JavaScript, Rust, and Go. Update the root `.env.sample` file with all necessary API keys and configuration variables for the different providers.

### Phase 2: Core Implementation
Implement runnable examples for each inference provider across different programming languages. Each example will be self-contained with its own README explaining the approach, required dependencies, and how to run it. Focus on demonstrating the key capabilities and configuration options of each provider.

### Phase 3: Integration
Create comprehensive documentation that ties all examples together, including comparison tables of different settings, capabilities, and trade-offs. Update the main repository README to include the new learning module in the structure table.

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### 1. Create Base Directory Structure and Configuration

- Create `different-inference-providers/` directory
- Create `different-inference-providers/README.md` with module overview, learning objectives, and placeholder for comparison tables
- Create `different-inference-providers/.gitignore` with appropriate ignore patterns for Python, JavaScript, Rust, Go, and model files
- Create `different-inference-providers/requirements.txt` with Python dependencies (openai, google-genai, ollama, transformers, torch, requests)
- Create `different-inference-providers/package.json` with JavaScript dependencies (openai SDK)
- Create `different-inference-providers/Cargo.toml` with Rust workspace configuration
- Create `different-inference-providers/go.mod` with Go module configuration
- Update root `.env.sample` to include environment variables for all providers (OPENAI_API_KEY, GOOGLE_VERTEX_PROJECT_ID, GOOGLE_APPLICATION_CREDENTIALS, OPENROUTER_API_KEY, HF_TOKEN, OLLAMA_HOST)

### 2. Implement OpenAI Raw HTTP Example (Rust)

- Create `different-inference-providers/openai-raw-http/` directory
- Create `different-inference-providers/openai-raw-http/Cargo.toml` with dependencies (reqwest, tokio, serde, serde_json, dotenv)
- Create `different-inference-providers/openai-raw-http/main.rs` implementing raw HTTP POST request to OpenAI API with streaming and non-streaming examples
- Create `different-inference-providers/openai-raw-http/README.md` documenting the approach, configuration options, and how to run

### 3. Implement OpenAI SDK Example (Python)

- Create `different-inference-providers/openai-sdk-python/` directory
- Create `different-inference-providers/openai-sdk-python/main.py` implementing OpenAI SDK usage with examples of different parameters (temperature, max_tokens, top_p, frequency_penalty, presence_penalty)
- Create `different-inference-providers/openai-sdk-python/README.md` documenting SDK features, configuration options, and comparison with raw HTTP approach

### 4. Implement Google Vertex AI Example (Python)

- Create `different-inference-providers/google-vertex/` directory
- Create `different-inference-providers/google-vertex/main.py` implementing Google Vertex AI SDK with examples of different models and generation parameters
- Create `different-inference-providers/google-vertex/README.md` documenting setup (service account, project configuration), available models, and unique Vertex AI features

### 5. Implement OpenRouter Example (JavaScript)

- Create `different-inference-providers/openrouter/` directory
- Create `different-inference-providers/openrouter/main.js` implementing OpenRouter using OpenAI SDK with custom base URL and examples of model selection
- Create `different-inference-providers/openrouter/README.md` documenting OpenRouter's model marketplace, pricing, and how it differs from direct OpenAI access

### 6. Implement Hugging Face Transformers Example (Python)

- Create `different-inference-providers/huggingface-transformers/` directory
- Create `different-inference-providers/huggingface-transformers/main.py` implementing local model inference using transformers library with Qwen3-8B or similar model
- Create `different-inference-providers/huggingface-transformers/README.md` documenting model download, hardware requirements, quantization options, and inference parameters

### 7. Implement Ollama Examples (Python and Go)

- Create `different-inference-providers/ollama-python/` directory
- Create `different-inference-providers/ollama-python/main.py` implementing Ollama Python SDK with streaming and non-streaming examples
- Create `different-inference-providers/ollama-python/README.md` documenting Ollama setup, model management, and SDK features
- Create `different-inference-providers/ollama-go/` directory
- Create `different-inference-providers/ollama-go/main.go` implementing Ollama Go SDK with similar examples
- Create `different-inference-providers/ollama-go/README.md` documenting Go-specific usage patterns

### 8. Implement Llama.cpp Example (Bash and Python)

- Create `different-inference-providers/llama-cpp/` directory
- Create `different-inference-providers/llama-cpp/run-server.sh` bash script to download/convert model and start llama.cpp server with example parameters
- Create `different-inference-providers/llama-cpp/client-example.py` implementing HTTP client to connect to llama.cpp server
- Create `different-inference-providers/llama-cpp/README.md` documenting llama.cpp compilation, model formats (GGUF), quantization, server parameters, and client usage

### 9. Create Comprehensive Documentation and Comparisons

- Update `different-inference-providers/README.md` with:
  - Complete overview of all providers covered
  - Learning objectives for each provider type
  - Comparison table of configuration options across providers (temperature, top_p, top_k, max_tokens, stop sequences, etc.)
  - Comparison table of deployment approaches (cloud API, local inference, managed service, self-hosted)
  - Comparison table of programming language support
  - Cost and performance considerations
  - When to use each provider (decision matrix)
  - Links to official documentation for each provider
- Add note that there are many more inference providers available (Anthropic, Cohere, AI21, etc.) and these examples represent common patterns

### 10. Update Root Documentation

- Update root `README.md` Repository Structure table to include new module:
  - Folder: `different-inference-providers`
  - Topic: "Inference Providers"
  - Description: "Hands-on examples of various AI inference providers and their capabilities across multiple programming languages"

### 11. Run Validation Commands

- Execute all validation commands listed below to ensure all examples work correctly with zero errors
- Verify all code is properly formatted and dependencies are correctly specified
- Test that documentation is clear and complete

## Testing Strategy

### Unit Tests
This is a learning module focused on examples rather than production code, so formal unit tests are not required. However, each example should:
- Be runnable without errors (given proper API keys/setup)
- Include error handling for common failure cases (missing API keys, network errors, invalid responses)
- Demonstrate both successful execution and error scenarios in code comments

### Edge Cases
- Missing or invalid API keys - each example should check for environment variables and provide clear error messages
- Network failures - examples should handle connection errors gracefully
- Rate limiting - examples should handle API rate limit errors where applicable
- Model not found errors - especially for Ollama and llama.cpp examples
- Memory constraints - Hugging Face example should warn about hardware requirements
- Different response formats - examples should handle streaming vs non-streaming responses

## Acceptance Criteria
- [ ] `different-inference-providers/` directory exists with all subdirectories for each provider
- [ ] All dependency files (requirements.txt, package.json, Cargo.toml, go.mod) are present and complete
- [ ] Each provider example has a runnable script in the specified language
- [ ] Each provider example has a comprehensive README with setup instructions, usage examples, and configuration explanations
- [ ] Root `.env.sample` is updated with all necessary environment variables
- [ ] Main `different-inference-providers/README.md` includes comparison tables and learning objectives
- [ ] Root `README.md` is updated with the new module in the structure table
- [ ] All code examples follow language-specific best practices and include error handling
- [ ] Documentation mentions that these are common examples and many more providers exist
- [ ] `.gitignore` properly excludes dependencies, build artifacts, and model files

## Validation Commands
Execute every command to validate the feature works correctly with zero regressions.

- `cd different-inference-providers && cat README.md` - Verify main module documentation exists and is complete
- `cd different-inference-providers && cat .gitignore` - Verify gitignore is properly configured
- `cat .env.sample | grep -E "(OPENAI|VERTEX|OPENROUTER|OLLAMA|HF_TOKEN)"` - Verify environment variables are documented
- `cd different-inference-providers/openai-raw-http && cargo check` - Verify Rust code compiles without errors
- `cd different-inference-providers/openai-sdk-python && python -m py_compile main.py` - Verify Python code has no syntax errors
- `cd different-inference-providers/google-vertex && python -m py_compile main.py` - Verify Python code has no syntax errors
- `cd different-inference-providers/openrouter && node -c main.js` - Verify JavaScript code has no syntax errors
- `cd different-inference-providers/huggingface-transformers && python -m py_compile main.py` - Verify Python code has no syntax errors
- `cd different-inference-providers/ollama-python && python -m py_compile main.py` - Verify Python code has no syntax errors
- `cd different-inference-providers/ollama-go && go build` - Verify Go code compiles without errors
- `cd different-inference-providers/llama-cpp && bash -n run-server.sh` - Verify bash script syntax is valid
- `cd different-inference-providers/llama-cpp && python -m py_compile client-example.py` - Verify Python client code has no syntax errors
- `cat README.md | grep -i "different-inference-providers"` - Verify root README is updated with new module
- `find different-inference-providers -name "README.md" -type f | wc -l` - Verify all subdirectories have README files (should be 9)

## Notes

### Dependencies to Install
Python packages:
- `openai` - OpenAI official SDK
- `google-genai` - Google Vertex AI SDK
- `ollama` - Ollama Python SDK
- `transformers` - Hugging Face transformers library
- `torch` - PyTorch for transformers
- `requests` - HTTP client for llama.cpp example

JavaScript packages:
- `openai` - OpenAI SDK (used for OpenRouter as well)

Rust crates:
- `reqwest` - HTTP client
- `tokio` - Async runtime
- `serde` / `serde_json` - JSON serialization
- `dotenv` - Environment variable loading

Go packages:
- `github.com/rozoomcool/go-ollama-sdk` - Ollama Go SDK

### Reference Documentation
- OpenAI REST API: https://platform.openai.com/docs/api-reference/backward-compatibility
- OpenAI SDKs: https://platform.openai.com/docs/libraries
- Google Vertex GenAI SDK: https://googleapis.github.io/python-genai/
- OpenRouter Docs: https://openrouter.ai/docs/community/open-ai-sdkdocs
- Ollama Go SDK: https://pkg.go.dev/github.com/rozoomcool/go-ollama-sdk
- Ollama Python SDK: https://github.com/ollama/ollama-python
- Hugging Face Example: https://huggingface.co/Qwen/Qwen3-8B
- llama.cpp: https://github.com/ggml-org/llama.cpp

### Future Considerations
- Could expand to include additional providers like Anthropic Claude, Cohere, AI21 Labs
- Could add examples of batch processing and async patterns
- Could include cost comparison calculations
- Could add benchmarking examples to compare inference speed
- Could demonstrate fine-tuning workflows for different providers
