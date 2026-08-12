# FX Mitra 🤖

A conversational **currency converter chatbot** built using Google Dialogflow, Python, and Telegram.

## Features

* Currency conversion through natural language
* Dialogflow intent and entity handling
* External currency exchange API integration
* Conversational context and parameters
* Casual and sarcastic chatbot responses
* Telegram Bot integration
* Backend deployed on Render

## Tech Stack

* Python
* Google Dialogflow
* Telegram Bot API
* Currency Exchange API
* Render

## How It Works

```text
User
  ↓
Telegram
  ↓
Dialogflow
  ↓
Intent & Entity Detection
  ↓
Python Backend
  ↓
Currency Exchange API
  ↓
Response
```

## Example

```text
User: Convert 100 USD to INR

FX Mitra: 100 USD ≈ 8,300 INR
```

## Current Status

🚧 **Work in Progress**

Currently improving:

* Currency entity recognition
* Parameter handling
* Context management
* Intent matching
* Error handling

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd FX-Mitra
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_token
CURRENCY_API_KEY=your_api_key
```

### 4. Run

```bash
python app.py
```

## Project Structure

```text
FX-Mitra/
│
├── app.py
├── requirements.txt
├── .env
├── dialogflow/
├── services/
└── README.md
```

## Future Improvements

* Better intent recognition
* Improved multi-turn conversations
* More reliable currency detection
* Better fallback handling
* More testing for natural-language inputs
