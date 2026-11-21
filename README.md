# Smart Notes Organizer

A Generative AI mini project that organizes scattered notes into meaningful topic groups with headings and bullet points.

## Problem statement
Notes collected from different sources are scattered and difficult to revise. This application uses a Large Language Model (Gemini) to group related notes under descriptive topic headings and returns the result in Markdown.

## Tech stack
- Python
- Streamlit
- Google Gemini API (`gemini-2.5-flash`)
- Google Gen AI Python SDK
- Markdown

## Features
- Paste multiple unorganized notes
- AI-based topic clustering
- Automatic topic headings
- Concise bullet-point formatting
- Download organized notes as a Markdown file

## Setup

1. Install Python 3.11 or newer.
2. Open this project folder in VS Code.
3. Create and activate a virtual environment:

   **Windows PowerShell**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Get a Gemini API key from https://aistudio.google.com/app/apikey
6. Run the app:

   ```bash
   streamlit run app.py
   ```

7. Paste your API key into the password field in the sidebar and click **Organize Notes**.

You can alternatively create a `.env` file containing `GEMINI_API_KEY=your_key`. Never upload `.env` to GitHub.

## Prompt design
The prompt asks Gemini to identify related ideas, group them under concise Markdown headings, preserve meaning and important details, remove exact repetition, avoid inventing facts, and return only Markdown.

## Sample test
Input:
- Machine learning is a subset of AI.
- Deep learning uses neural networks.
- SQL is used to query relational databases.
- MySQL is a relational database management system.

Expected grouping:
- Artificial Intelligence / Machine Learning
- Databases

## Security
Do not commit `.env`, API keys, or virtual-environment folders. The `.gitignore` file excludes these items.
