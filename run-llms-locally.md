## Run Large Language Models(LLMs) Locally Or With Github Codespaces using Ollama

This repository provides step-by-step instructions to install and run a LLM or lightweight language model (e.g., [TinyLlama](https://github.com/jzhang38/TinyLlama)) in GitHub Codespaces or Locally using [Ollama](https://ollama.com).
Ollama is a free, open-source tool that allows users to run large language models (LLMs) locally on their computers. Ollama is available on MacOS and Linux and uses a command-line interface. 

## Prerequisites For Online Environment (For Locally you need Python Only)

- A **GitHub account** with access to GitHub Codespaces.
- Familiarity with basic **command-line usage**.
- (Optional) If you want to run a different model, update the model name in the instructions below.

---

## Step 1: Create and Open a Codespace

1. **Fork or Clone This Repository:**
   - Click the **Code** button on this repository and choose **Open with Codespaces**.
   - Alternatively, create a Codespace from any repository with a minimal environment.

2. **Wait for Initialization:**
   - GitHub Codespaces will provision a Linux container.
   - Open the integrated terminal (**Terminal → New Terminal** in VS Code).

---

## Step 2: Install Ollama in the Codespace Or in Python Environment

Run the following command in the Codespace terminal to install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
#Once the installation completes, start the Ollama server:

ollama serve

# Run the TinyLlama Model (Any model)
#With Ollama running, use the following command to download and start TinyLlama:

ollama run tinyllama
```
Press Enter, and the model will generate a response.

## Example
[Integate Ollama with LangChain](https://github.com/heyibad/agentic-and-generative-ai/blob/main/ollama-exmple-langchain.md)
