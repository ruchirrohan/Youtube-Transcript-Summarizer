import os
import re
import streamlit as st
from dotenv import load_dotenv
load_dotenv() #load all env variables
from youtube_transcript_api import YouTubeTranscriptApi

import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt_template = os.getenv("SUMMARY_PROMPT")

#fetch transcript data in the form of list and then append them to one single para.
def extract_transcript_details(youtube_video_url):
    try:
        video_id = extract_video_url(youtube_video_url)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

def extract_video_url(youtube_video_url):
    """Extracts video ID from different types of YouTube URLs"""
    pattern = r"(?:v=|\/|youtu\.be\/|\/embed\/|watch\?v=|watch\?.+&v=)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, youtube_video_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")


def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

#Streamlit UI
st.title("YouTube Transcript Summarizer")
yt_link = st.text_input("Enter YouTube URL")

if yt_link:
    video_id = extract_video_url(yt_link)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

summary_length = st.radio("Choose Summary Length", ["Short", "Medium", "Long"])

if summary_length == "Short":
    prompt = prompt_template.replace("{summary_length}", "short (3 points)")
elif summary_length == "Medium":
    prompt = prompt_template.replace("{summary_length}", "medium (3-5 points, max 5 points)")
else:
    prompt = prompt_template.replace("{summary_length}", "long (5-8 points, max 8 points)")
# start summarizing
if st.button("Get Summary"):
    transcript_text = extract_transcript_details(yt_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Summary:")
        st.write(summary)
