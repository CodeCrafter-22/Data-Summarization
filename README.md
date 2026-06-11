# Data Summarization Web App

A simple Flask-based web application that generates concise summaries from long text using the Hugging Face Inference API.

## Features

* Summarize large paragraphs of text
* Adjustable summary length
* Clean and simple user interface
* Powered by Hugging Face NLP models
* Built with Flask

## Tech Stack

* Python
* Flask
* HTML/CSS
* Hugging Face Inference API
* Requests
* Python Dotenv

## Project Structure

```text
Data-Summarization/
│
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── Lexi.png
│
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/CodeCrafter-22/Data-Summarization.git
cd Data-Summarization
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_access_token
```

You can generate a token from your Hugging Face account settings.

## Running the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

## Deployment

This application can be deployed on platforms such as:

* Render
* Railway
* PythonAnywhere

### Render Configuration

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
gunicorn app:app
```

Add the following environment variable in Render:

```env
HF_TOKEN=your_huggingface_access_token
```

## How It Works

1. User enters a paragraph of text.
2. User selects the desired summary length.
3. Flask sends the text to the Hugging Face Inference API.
4. The model generates a concise summary.
5. The summarized text is displayed on the webpage.

## Future Improvements

* Multiple summarization models
* File upload support (PDF/TXT)
* Copy-to-clipboard functionality
* Summary download option
* User authentication

## Author

Mansi

GitHub: https://github.com/CodeCrafter-22
