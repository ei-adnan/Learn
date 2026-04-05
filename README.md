# Week 1 — OpenAI API Basics

A Python script that calls the OpenAI API, sends a structured prompt, and returns a parsed JSON response.

## What it does
- Loads API key securely from .env
- Sends a text analysis prompt
- Forces JSON output
- Handles API and parsing errors

## Setup
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your OpenAI API key
5. Run: `python main.py`