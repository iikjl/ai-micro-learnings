#!/usr/bin/env node

/**
 * OpenRouter Example (JavaScript/Node.js)
 *
 * Demonstrates how to use OpenRouter with the OpenAI SDK.
 * OpenRouter provides a unified API to access multiple AI models.
 */

import OpenAI from 'openai';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config({ path: '../../.env' });

async function main() {
    // Get API key
    const apiKey = process.env.OPENROUTER_API_KEY;
    if (!apiKey) {
        throw new Error(
            'OPENROUTER_API_KEY environment variable not set. ' +
            'Please set it in your .env file.'
        );
    }

    console.log('OpenRouter Example (JavaScript/Node.js)\n');
    console.log('='.repeat(50) + '\n');

    // Initialize OpenAI client with OpenRouter configuration
    const client = new OpenAI({
        apiKey: apiKey,
        baseURL: 'https://openrouter.ai/api/v1',
        defaultHeaders: {
            'HTTP-Referer': 'https://github.com/yourusername/ai-micro-learnings',
            'X-Title': 'AI Micro Learnings',
        }
    });

    // Example 1: Basic chat with different model
    console.log('Example 1: Basic Chat Completion');
    console.log('-'.repeat(50));
    await basicChatCompletion(client);

    console.log('\n');

    // Example 2: Comparing different models
    console.log('Example 2: Comparing Different Models');
    console.log('-'.repeat(50));
    await compareModels(client);

    console.log('\n');

    // Example 3: Streaming response
    console.log('Example 3: Streaming Response');
    console.log('-'.repeat(50));
    await streamingResponse(client);
}

async function basicChatCompletion(client) {
    console.log('Using model: z-ai/glm-4.5-air:free\n');

    const response = await client.chat.completions.create({
        model: 'z-ai/glm-4.5-air:free',
        messages: [
            { role: 'system', content: 'You are a helpful assistant.' },
            { role: 'user', content: 'What is the capital of France?' }
        ]
    });

    const message = response.choices[0].message;

    console.log(`Response ID: ${response.id}`);
    console.log(`Model: ${response.model}`);

    // Handle reasoning models (like GLM-4.5-Air) that separate reasoning from content
    if (message.reasoning) {
        console.log(`\nReasoning:\n${message.reasoning}`);
    }

    if (message.content) {
        console.log(`\nAssistant: ${message.content}`);
    } else if (!message.reasoning) {
        console.log(`\nAssistant: [No content returned]`);
    }

    if (response.usage) {
        console.log('\nToken Usage:');
        console.log(`  Prompt tokens: ${response.usage.prompt_tokens}`);
        console.log(`  Completion tokens: ${response.usage.completion_tokens}`);
        console.log(`  Total tokens: ${response.usage.total_tokens}`);
    }
}

async function compareModels(client) {
    const models = [
        'z-ai/glm-4.5-air:free',
        'mistralai/mistral-7b-instruct:free',
    ];

    const prompt = 'Write a one-sentence fun fact about the ocean.';
    console.log(`Prompt: "${prompt}"\n`);

    for (const model of models) {
        try {
            console.log(`Model: ${model}`);

            const response = await client.chat.completions.create({
                model: model,
                messages: [
                    { role: 'system', content: 'You are a helpful assistant. Provide clear, direct answers.' },
                    { role: 'user', content: prompt }
                ],
                max_tokens: 500,  // Increased for reasoning models that need more tokens
                temperature: 0.7
            });

            // Check if we have choices and content
            if (response.choices && response.choices.length > 0) {
                const message = response.choices[0].message;

                // Show reasoning if present
                if (message.reasoning) {
                    console.log(`Reasoning:\n${message.reasoning}\n`);
                }

                // Show final response/content
                const content = message?.content || message?.text || '';
                if (content) {
                    console.log(`Response: ${content}`);
                } else if (message.reasoning) {
                    console.log(`Response: [Reasoning model - final answer in content field is empty]`);
                } else {
                    console.log(`Response: [No content returned]`);
                }
            } else {
                console.log(`Response: [No choices returned]`);
                console.log('Full response:', JSON.stringify(response, null, 2));
            }

            console.log();
        } catch (error) {
            console.log(`Error with ${model}: ${error.message}`);
            if (error.response) {
                console.log('Error details:', error.response.data);
            }
            console.log();
        }
    }
}

async function streamingResponse(client) {
    console.log('Streaming response (Assistant): ');

    const stream = await client.chat.completions.create({
        model: 'z-ai/glm-4.5-air:free',
        messages: [
            { role: 'user', content: 'Count from 1 to 5 with a word after each number.' }
        ],
        max_tokens: 500,  // Increased for reasoning models
        stream: true
    });

    for await (const chunk of stream) {
        const content = chunk.choices[0]?.delta?.content;
        if (content) {
            process.stdout.write(content);
        }
    }

    console.log('\n\nStreaming complete!');
}

// Run the main function
main().catch(error => {
    console.error('Error:', error.message);
    process.exit(1);
});
