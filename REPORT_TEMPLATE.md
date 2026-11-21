# Smart Notes Organizer — Procedure Report

**Project Title:** Smart Notes Organizer  
**Problem Statement Number:** [Enter PS number]  
**Name:** [Enter name]  
**Roll Number:** [Enter roll number]  
**Class:** [Enter class]  
**GitHub Link:** [Paste repository URL]

## 1. Problem Statement
Notes collected from lectures, websites and other sources are often scattered and difficult to revise. The aim of this project is to develop a Generative AI application that groups related notes under meaningful topic headings and presents them as organized Markdown notes.

## 2. Tools and Model
- Programming language: Python
- UI framework: Streamlit
- LLM: Google Gemini 2.5 Flash through Gemini API
- SDK: google-genai
- Output format: Markdown
- Development environment: Visual Studio Code

## 3. Procedure
1. Created a project folder and opened it in Visual Studio Code.
2. Created a Python virtual environment and installed Streamlit, google-genai and python-dotenv.
3. Generated a Gemini API key using Google AI Studio. The key is entered securely in the app and is not hard-coded in the source code.
4. Prepared and tested a prompt that instructs Gemini to identify related notes, group them under descriptive headings and format each group with bullet points.
5. Developed the Python application in app.py. It accepts notes, sends the prompt to Gemini through the API and receives the organized Markdown response.
6. Built the user interface using Streamlit, including a text area, an Organize Notes button, output display and Markdown download option.
7. Tested the application with at least five different sets of notes and checked whether related information was grouped correctly.
8. Added requirements.txt, README.md and .gitignore, then uploaded the project code to GitHub without the API key.

## 4. Prompt Used
You are an expert study-notes organizer. Read the user's scattered notes and group related ideas under meaningful topic headings. Use Markdown headings and concise bullet points. Preserve important facts and meaning, remove exact repetition, do not invent information, and place unmatched notes under Other Notes. Return only the organized Markdown notes.

**Prompt improvement:** The initial prompt was improved by adding instructions to preserve unique information, avoid hallucinating facts, remove only exact repetition and use an "Other Notes" heading for unmatched items.

## 5. Results
The application accepts unorganized notes and generates topic-wise Markdown output with headings and bullet points. Insert screenshots of the running application and its output here.

## 6. Challenges
Possible challenges include an invalid API key, internet connectivity problems, API quota limits and occasional grouping mistakes. These can be addressed by checking the key, verifying connectivity and improving the prompt with clearer grouping instructions.

## 7. Conclusion
The Smart Notes Organizer demonstrates how a Large Language Model can be integrated into a simple Python application to solve a practical information-organization problem. It successfully groups related notes and generates Markdown output. A future improvement would be adding file upload support for PDF and text documents.
