import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipeline.prediction_pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", page_icon="🌀", layout="wide")

load_dotenv()

# Custom CSS for anime look (gender-neutral, softer contrast)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #4b6cb7 0%, #182848 100%);
    }
    .anime-header {
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', cursive;
        font-size: 3em;
        color: #ffd700;
        text-shadow: 2px 2px 8px #4b6cb7;
        margin-bottom: 0.2em;
    }
    .anime-card {
        background: #232946;
        border-radius: 18px;
        box-shadow: 0 4px 16px #232946;
        padding: 1.5em;
        margin-bottom: 1em;
        border: 2px solid #8f5cff;
        color: #e0e7ff;
        font-size: 1.1em;
        line-height: 1.6em;
    }
    .stTextInput>div>div>input {
        background: #232946;
        border-radius: 8px;
        border: 1px solid #8f5cff;
        color: #e0e7ff;
    }
    .anime-watch-btn {
        display: inline-block;
        background: linear-gradient(90deg, #8f5cff 0%, #ffd700 100%);
        color: #232946;
        font-weight: bold;
        font-size: 1.1em;
        padding: 0.7em 1.5em;
        border-radius: 12px;
        text-decoration: none;
        box-shadow: 0 2px 8px #23294644;
        animation: beat 1s infinite;
        margin-top: 1em;
        margin-bottom: 2em;
        transition: transform 0.2s;
    }
    @keyframes beat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.08); }
    }
    .anime-watch-btn:hover {
        background: linear-gradient(90deg, #ffd700 0%, #8f5cff 100%);
        color: #fff;
        transform: scale(1.12);
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_resource # catching the pipeline to avoid reloading it on every interaction, stored in memory
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.markdown('<div class="anime-header">🌀 Anime Recommender Engine 🌀</div>', unsafe_allow_html=True)
st.markdown("<p style='color:#ffd700;font-size:1.2em;'>Find your next favorite anime! 🎌✨</p>", unsafe_allow_html=True)

query = st.text_input("What kind of anime do you want to watch? (e.g. action, adventure, comedy)", help="Type a genre, mood, or theme!")
if query:
    with st.spinner("Summoning jutsu... 🌀"):
        response = pipeline.recommend(query)
        st.markdown("<h3 style='color:#8f5cff;'>Your Anime Recommendations:</h3>", unsafe_allow_html=True)
        # Show each recommendation in a styled card if response is a list, else just show text
        if isinstance(response, list):
            for rec in response:
                st.markdown(f'<div class="anime-card">{rec}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="anime-card">{response}</div>', unsafe_allow_html=True)


# Animated button-style hyperlink with dark green color and white text
st.markdown(
    """
    <style>
    .anime-watch-btn {
        display: inline-block;
        background: linear-gradient(180deg, #14532d 0%, #22c55e 100%);
        color: #FFF;
        font-weight: bold;
        font-size: 1.1em;
        padding: 0.7em 1.5em;
        border-radius: 12px;
        text-decoration: none;
        box-shadow: 0 2px 8px #23294644;
        animation: beat 1s infinite;
        margin-top: 1em;
        margin-bottom: 2em;
        transition: transform 0.2s;
        border: 2px solid #14532d;
    }
    @keyframes beat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.08); }
    }
    .anime-watch-btn:hover {
        background: linear-gradient(90deg, #22c55e 0%, #14532d 100%);
        color: #fff;
        transform: scale(1.12);
    }
    </style>
    <div style='text-align:center;'>
        <a class='anime-watch-btn' href='https://ww.aniwave.se/home-animes' target='_blank'>Here's where you can watch anime!</a>
    </div>
    """,
    unsafe_allow_html=True
)