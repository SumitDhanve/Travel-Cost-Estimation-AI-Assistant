# Travel-Cost-Estimation-AI-Assistant
An AI-powered travel cost estimator built using Streamlit, LangChain, and Google Gemini.
Users simply enter Source, Destination, and Mode of Transport, and the app instantly returns an estimated travel cost.

## Features
Real-time Travel Cost Estimation using Google Gemini

LangChain Prompting for structured responses

Dynamic transport mode images

Simple, clean Streamlit UI

Model outputs cost only, with no suggestions (as per system prompt)

## Tech Stack
Python 3.10+

Streamlit

LangChain

Google Generative AI (Gemini 2.0 Flash)

Pillow (PIL)

## How It Works
User enters source, destination, and mode

Input is sent to a LangChain PromptTemplate

Gemini model processes it and returns only the estimated travel cost

Streamlit displays output cleanly

## Requirements File
Your requirements.txt should include:

streamlit
langchain
langchain-core
langchain-google-genai
google-generativeai
pillow

## The Frontend using Streamlit:
<img width="639" height="860" alt="Screenshot 2025-10-26 133004" src="https://github.com/user-attachments/assets/c185a1fe-1557-421e-b46d-cba0a6e43d51" />



