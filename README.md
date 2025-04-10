# Briefly: AI-Powered YouTube Video Summarizer

## Overview

"Briefly" is a web application that leverages Artificial Intelligence (AI) to summarize YouTube videos. It allows users to quickly obtain concise summaries of video content, saving time and improving information accessibility. The application extracts video transcripts and employs a powerful Natural Language Processing (NLP) model to generate these summaries.

## Features

* **YouTube URL Input:** Users can provide a YouTube video URL.
* **Automatic Transcript Extraction:** The application automatically fetches the video's English subtitles.
* **AI-Powered Summarization:** Utilizes a pre-trained NLP model to generate a summary of the transcript.
* **Clear Output Display:** Presents the generated summary in a user-friendly format.

## Technologies Used

* **Backend:**
    * Python
    * Flask (Web framework)
* **NLP:**
    * `transformers` library (Hugging Face)
    * Pre-trained summarization model (e.g., BART, DistilBART)
* **Transcript Extraction:**
    * `yt-dlp` (YouTube downloader and processor)
* **Frontend:**
    * HTML
    * CSS

## Setup and Installation

1.  **Prerequisites:**
    * Python 3.x installed
    * pip (Python package installer)

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables:** (If applicable, and if you have any API keys or sensitive information)
    * Create a `.env` file in the project root.
    * Add any necessary environment variables (e.g., API keys) to the `.env` file.

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    * The application will typically be accessible at `http://127.0.0.1:5000` in your web browser.

## Usage

1.  Open the application in your web browser.
2.  Enter the URL of a YouTube video in the provided input field.
3.  Click the "Summarize" button.
4.  The application will process the video and display the generated summary.

## Notes

* Ensure that the YouTube video has available English subtitles for successful transcript extraction.
* Error handling is implemented to manage potential issues during transcript retrieval and summarization.
* The summarization model can be changed by modifying the `app.py` file.
