---
title: RefineMyWords
app_file: frontend/interface.py
sdk: gradio
sdk_version: 5.1.0
---

# RefineMyWords

RefineMyWords is a sentence correction tool designed to help users enhance their English writing. Using machine learning, it efficiently corrects grammar, improves clarity, and refines overall sentence structure.

## Features

- User Interface (Frontend): The app’s user-friendly interface is powered by Gradio, enabling easy and interactive access to the tool.
- Backend: FastAPI serves as the backbone for the API endpoint, ensuring fast and reliable performance.
- Inference Process: The app leverages LangChain to manage LLM-based (Large Language Model) inference. Currently, it uses OpenAI’s gpt-3.5-turbo for its sentence correction capabilities.

## How It Works

RefineMyWords takes user input text, pass it through a machine learning pipeline, and returns a polished, refined version with improved grammar and clarity.
