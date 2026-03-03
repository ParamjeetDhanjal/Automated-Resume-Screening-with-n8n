
# AI Resume Analyzer - n8n Workflow

A resume screening automation system built with **n8n** that receives resumes via webhook, analyzes them using AI, and processes candidate data efficiently.

---

## Overview

This workflow automates the resume screening process by:

* Receiving candidate information and resumes from a FastAPI backend
* Extracting text from PDF resumes
* Analyzing content using **Groq LLM**
* Storing results for HR review
* Notifying HR and sending candidate confirmations

It is designed to reduce manual resume screening effort while maintaining human oversight.

---

## Workflow Nodes

| Node                       | Function                                                                         |
| -------------------------- | -------------------------------------------------------------------------------- |
| **Webhook**                | Receives POST requests from FastAPI containing candidate details and resume file |
| **Extract from File**      | Extracts text content from uploaded PDF resumes                                  |
| **Basic LLM Chain (Groq)** | Analyzes resume content using AI to evaluate candidate suitability               |
| **Merge**                  | Combines original candidate data with AI analysis results                        |
| **Upload File**            | Saves original resume to Google Drive for storage                                |
| **Edit Fields (Manual)**   | Formats and structures data for subsequent nodes                                 |
| **Send a Message**         | Sends notification to HR via email or Slack                                      |
| **Respond to Webhook**     | Returns confirmation response to the FastAPI backend                             |

---

## Data Flow

1. Candidate submits resume through an HTML form.
2. FastAPI backend receives submission and forwards it to the n8n webhook.
3. n8n extracts text from the PDF resume.
4. **Groq LLM** analyzes resume content and generates score/insights.
5. Results are merged with candidate information.
6. Original resume is saved to Google Drive.
7. Candidate data is stored in Google Sheets.
8. HR receives notification about the new candidate.
9. Confirmation is sent back to the candidate.

---

## Setup Requirements

* n8n instance
* Groq API key for LLM analysis
* Google Sheets and Google Drive credentials
* FastAPI backend with HTML form
* Environment variables for webhook URL and API keys

---

## Features

* Automated resume parsing and text extraction
* AI-powered candidate evaluation and scoring
* Centralized candidate database in Google Sheets
* Resume storage in Google Drive
* Instant HR notifications
* Scalable architecture for high-volume processing

---

## Installation & Usage

1. Clone the repository to your server:

   ```bash
   git clone <repo-url>
   cd ai-resume-analyzer
   ```

2. Set up **environment variables**:

   ```
   N8N_WEBHOOK_URL=<your_n8n_webhook_url>
   GROQ_API_KEY=<your_groq_api_key>
   GOOGLE_CREDENTIALS=<your_google_credentials_json>
   ```

3. Start your n8n instance and import the workflow `.json` file.

4. Ensure your FastAPI backend sends candidate submissions to the n8n webhook endpoint.

5. HR can review candidates via Google Sheets, and notifications will be sent automatically.

---

## Contributing

Feel free to open issues, suggest improvements.
This workflow can be extended to integrate with Slack, Teams, or other HR systems.
