use reqwest::Client;
use serde::{Deserialize, Serialize};
use std::env;

#[derive(Serialize)]
struct ChatRequest {
    model: String,
    messages: Vec<Message>,
    #[serde(skip_serializing_if = "Option::is_none")]
    temperature: Option<f32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    max_tokens: Option<u32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    top_p: Option<f32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    frequency_penalty: Option<f32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    presence_penalty: Option<f32>,
    #[serde(skip_serializing_if = "Option::is_none")]
    stream: Option<bool>,
}

#[derive(Serialize, Deserialize, Debug)]
struct Message {
    role: String,
    content: String,
}

#[derive(Deserialize, Debug)]
struct ChatResponse {
    id: String,
    choices: Vec<Choice>,
    usage: Option<Usage>,
}

#[derive(Deserialize, Debug)]
struct Choice {
    index: u32,
    message: Message,
    finish_reason: Option<String>,
}

#[derive(Deserialize, Debug)]
struct Usage {
    prompt_tokens: u32,
    completion_tokens: u32,
    total_tokens: u32,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Load environment variables from .env file if present
    dotenv::dotenv().ok();

    // Get API key from environment
    let api_key = env::var("OPENAI_API_KEY").map_err(|_| {
        "OPENAI_API_KEY environment variable not set. Please set it in your .env file."
    })?;

    println!("OpenAI Raw HTTP Example (Rust)\n");
    println!("================================\n");

    // Example 1: Basic non-streaming request
    println!("Example 1: Basic Non-Streaming Request");
    println!("---------------------------------------");
    basic_request(&api_key).await?;

    println!("\n");

    // Example 2: Request with custom parameters
    println!("Example 2: Custom Parameters");
    println!("----------------------------");
    custom_parameters_request(&api_key).await?;

    Ok(())
}

async fn basic_request(api_key: &str) -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();

    let request = ChatRequest {
        model: "gpt-3.5-turbo".to_string(),
        messages: vec![
            Message {
                role: "system".to_string(),
                content: "You are a helpful assistant.".to_string(),
            },
            Message {
                role: "user".to_string(),
                content: "What is the capital of France?".to_string(),
            },
        ],
        temperature: None,
        max_tokens: None,
        top_p: None,
        frequency_penalty: None,
        presence_penalty: None,
        stream: None,
    };

    let response = client
        .post("https://api.openai.com/v1/chat/completions")
        .header("Authorization", format!("Bearer {}", api_key))
        .header("Content-Type", "application/json")
        .json(&request)
        .send()
        .await?;

    if !response.status().is_success() {
        let error_text = response.text().await?;
        return Err(format!("API request failed: {}", error_text).into());
    }

    let chat_response: ChatResponse = response.json().await?;

    println!("Response ID: {}", chat_response.id);
    println!("Assistant: {}", chat_response.choices[0].message.content);

    if let Some(usage) = chat_response.usage {
        println!("\nToken Usage:");
        println!("  Prompt tokens: {}", usage.prompt_tokens);
        println!("  Completion tokens: {}", usage.completion_tokens);
        println!("  Total tokens: {}", usage.total_tokens);
    }

    Ok(())
}

async fn custom_parameters_request(api_key: &str) -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();

    let request = ChatRequest {
        model: "gpt-3.5-turbo".to_string(),
        messages: vec![
            Message {
                role: "system".to_string(),
                content: "You are a creative storyteller.".to_string(),
            },
            Message {
                role: "user".to_string(),
                content: "Tell me a very short story about a robot.".to_string(),
            },
        ],
        temperature: Some(0.9),
        max_tokens: Some(100),
        top_p: Some(0.95),
        frequency_penalty: Some(0.3),
        presence_penalty: Some(0.2),
        stream: Some(false),
    };

    println!("Request Parameters:");
    println!("  Model: {}", request.model);
    println!("  Temperature: {:?}", request.temperature);
    println!("  Max Tokens: {:?}", request.max_tokens);
    println!("  Top P: {:?}", request.top_p);
    println!("  Frequency Penalty: {:?}", request.frequency_penalty);
    println!("  Presence Penalty: {:?}", request.presence_penalty);
    println!();

    let response = client
        .post("https://api.openai.com/v1/chat/completions")
        .header("Authorization", format!("Bearer {}", api_key))
        .header("Content-Type", "application/json")
        .json(&request)
        .send()
        .await?;

    if !response.status().is_success() {
        let error_text = response.text().await?;
        return Err(format!("API request failed: {}", error_text).into());
    }

    let chat_response: ChatResponse = response.json().await?;

    println!("Assistant: {}", chat_response.choices[0].message.content);

    if let Some(usage) = chat_response.usage {
        println!("\nToken Usage:");
        println!("  Total tokens: {}", usage.total_tokens);
    }

    Ok(())
}
