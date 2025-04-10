import os
import subprocess
from flask import Flask, render_template, request, redirect
from transformers import pipeline

app = Flask(__name__)

# Load summarization model
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn") # Using a more standard model
except Exception as e:
    print(f"Error loading summarization model: {e}")
    summarizer = None

def extract_transcript(youtube_url):
    try:
        # Use yt-dlp to extract subtitles to a file
        command = [
            'yt-dlp',
            '--write-auto-sub',
            '--sub-lang', 'en',
            '--skip-download',
            '--output', '%(id)s.%(ext)s',
            youtube_url
        ]
        subprocess.run(command, check=True, capture_output=True, text=True)

        # Extract video ID
        video_id = youtube_url.split("v=")[-1].split("&")[0]
        subtitle_file = f"{video_id}.en.vtt"

        if not os.path.exists(subtitle_file):
            return None

        # Read and return transcript as plain text
        with open(subtitle_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            text = ''.join([line for line in lines if not line.startswith(('WEBVTT', '00:', '\n'))])
            return text
    except subprocess.CalledProcessError as e:
        print(f"Error during yt-dlp execution: {e.stderr}")
        return None
    except Exception as e:
        print(f"Error extracting transcript: {e}")
        return None
    finally:
        # Clean up subtitle file
        if 'video_id' in locals() and os.path.exists(f"{video_id}.en.vtt"):
            os.remove(f"{video_id}.en.vtt")

def summarize_text(text):
    if summarizer:
        max_chunk = 1000
        chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
        summaries = []
        for chunk in chunks:
            try:
                summary_output = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
                if summary_output:
                    summaries.append(summary_output[0]['summary_text'])
            except Exception as e:
                print(f"Error during summarization: {e}")
                continue
        return ' '.join(summaries)
    else:
        return "Summarization model not loaded."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ai_summarize')
def ai_summarize_page():
    return render_template('AI summarize.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    youtube_link = request.form['youtube_link']

    if not youtube_link:
        return "Please enter a YouTube URL."

    try:
        transcript = extract_transcript(youtube_link)
        if transcript:
            summary = summarize_text(transcript)
            return render_template('AI summarize.html', summary=summary)
        else:
            return "Could not fetch the transcript for the provided YouTube URL."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)