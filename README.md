# YouTube Transcript Summarizer

This is a web application that allows users to summarize the transcripts of YouTube videos. It fetches the transcript of a video using the YouTube Transcript API, and then generates a summarized version of the content. The summary can be customized based on the user's preferred length: Short, Medium, or Long.

## Features
- Fetches YouTube video transcripts automatically.
- Summarizes the transcript into different lengths (Short, Medium, Long).
- Provides an easy-to-use interface with Streamlit.

## How to Use
1. **Enter a YouTube URL**: Paste the YouTube video URL in the input box.
2. **Select the Summary Length**: Choose the length of the summary (Short, Medium, Long).
3. **Click on "Get Summary"**: After the video details are processed, the summary will be displayed on the screen.

## Deployment
You can check out the working version of the app [here](https://yt-transcript-summary.streamlit.app/)!

## Setup Instructions

To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/ruchirrohan/Youtube-Transcript-Summarizer.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Set up environment variables: Create a .env file in the project root directory with the following variables:
   ```bash
   GOOGLE_API_KEY=<get @ https://aistudio.google.com/app/apikey>
   SUMMARY_PROMPT=<your-summary-prompt>
4. Run the app
   ```bash
   streamlit run app.py

## Technologies Used
Python: Main programming language.

Streamlit: For building the interactive web app.

YouTube Transcript API: For fetching video transcripts.

Google Gemini API: For generating the summary of the transcript.

## Acknowledgement
The base structure of this app was inspired by a tutorial from [Krish Naik](https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig) on YouTube. Additional features were added to enhance the functionality.
