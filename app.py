import os

import streamlit as st
from dotenv import load_dotenv
load_dotenv() #load all env variables
from youtube_transcript_api import YouTubeTranscriptApi

import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a Youtube video summarizer. You will be taking the transcript text and summarizing it and providing the important summary in points within 250 words. The transcript text will be appended after this"""

#fetch transcript data in the form of list and then append them to one single para.
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

st.title("YouTube Transcript Summarizer")
yt_link = st.text_input("Enter YouTube URL")

if yt_link:
    video_id = yt_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Summary"):
    transcript_text = extract_transcript_details(yt_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        #st.markdown("Summary:")
        st.write(summary)
