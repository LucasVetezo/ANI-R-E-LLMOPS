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
        background: #232946;
        overflow-x: hidden;
    }
    /* Fun shapes: circles, stars, swirls */
    .fun-shape {
        position: fixed;
        z-index: 0;
        opacity: 0.18;
        pointer-events: none;
    }
    .shape1 {
        left: 5vw; top: 10vh; width: 80px; height: 80px; background: #ffd700; border-radius: 50%;
        animation: moveShape1 12s linear infinite;
    }
    .shape2 {
        right: 8vw; top: 20vh; width: 60px; height: 60px; background: #8f5cff; border-radius: 50%;
        animation: moveShape2 14s linear infinite;
    }
    .shape3 {
        left: 20vw; bottom: 10vh; font-size: 60px; color: #22c55e;
        animation: moveShape3 16s linear infinite;
    }
    .shape4 {
        right: 15vw; bottom: 15vh; font-size: 70px; color: #ffd700;
        animation: moveShape4 18s linear infinite;
    }
    .shape5 {
        left: 50vw; top: 50vh; font-size: 80px; color: #8f5cff;
        animation: moveShape5 20s linear infinite;
    }
    @keyframes moveShape1 {
        0% {transform: translate(0,0);}
        25% {transform: translate(40px,60px);}
        50% {transform: translate(-30px,120px);}
        75% {transform: translate(-60px,-40px);}
        100% {transform: translate(0,0);}
    }
    @keyframes moveShape2 {
        0% {transform: translate(0,0);}
        20% {transform: translate(-30px,40px);}
        40% {transform: translate(50px,-60px);}
        60% {transform: translate(-40px,80px);}
        80% {transform: translate(30px,-40px);}
        100% {transform: translate(0,0);}
    }
    @keyframes moveShape3 {
        0% {transform: translate(0,0);}
        30% {transform: translate(60px,-40px);}
        60% {transform: translate(-50px,60px);}
        90% {transform: translate(40px,-80px);}
        100% {transform: translate(0,0);}
    }
    @keyframes moveShape4 {
        0% {transform: translate(0,0);}
        25% {transform: translate(-40px,60px);}
        50% {transform: translate(30px,-120px);}
        75% {transform: translate(60px,40px);}
        100% {transform: translate(0,0);}
    }
    @keyframes moveShape5 {
        0% {transform: translate(0,0);}
        20% {transform: translate(80px,40px);}
        40% {transform: translate(-50px,-60px);}
        60% {transform: translate(40px,80px);}
        80% {transform: translate(-30px,-40px);}
        100% {transform: translate(0,0);}
    }

    .anime-header {
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', cursive;
        font-size: 3em;
        color: #FFFFFF;
        text-shadow: 2px 2px 8px #4b6cb7;
        margin-bottom: 0.2em;
        text-align: center;
    }
    </style>
    <div class='fun-shape shape1'></div>
    <div class='fun-shape shape2'></div>
    <div class='fun-shape shape3'>⭐</div>
    <div class='fun-shape shape4'>🌀</div>
    <div class='fun-shape shape5'>🌟</div>
    <!-- Japanese Kanji symbols -->
    <div class='fun-shape' style='left:10vw;top:60vh;font-size:60px;color:#ffd700;animation:moveShape3 16s linear infinite;'>愛</div>
    <div class='fun-shape' style='right:12vw;top:35vh;font-size:70px;color:#8f5cff;animation:moveShape4 18s linear infinite;'>忍</div>
    <div class='fun-shape' style='left:60vw;bottom:20vh;font-size:80px;color:#22c55e;animation:moveShape5 20s linear infinite;'>火</div>
    """,
    unsafe_allow_html=True
)

@st.cache_resource # catching the pipeline to avoid reloading it on every interaction, stored in memory
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

# Naruto-style icons and shapes for anime vibe
naruto_icons = """
<div style='text-align:center; margin-bottom: 0.5em;'>
    <span style='font-size:2.5em; margin:0 0.2em;'>🌀</span>
    <span style='font-size:2.5em; margin:0 0.2em;'>🥷</span>
    <span style='font-size:2.5em; margin:0 0.2em;'>🌿</span>
    <span style='font-size:2.5em; margin:0 0.2em;'>⚔️</span>
</div>
"""
st.markdown(naruto_icons, unsafe_allow_html=True)

st.markdown('<div class="anime-header">🌀 Anime Recommender Engine 🌀</div>', unsafe_allow_html=True)
st.markdown("<p style='color:#ffd700;font-size:1.2em;'>Find your next favorite anime! 🎌✨</p>", unsafe_allow_html=True)

query = st.text_input("What kind of anime do you want to watch? (e.g. action, adventure, comedy)", help="Type a genre, mood, or theme!")
if query:
    with st.spinner("Summoning anime recommendations... 🌀"):
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
        color: #00000;
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


# Signature with static lightning icons, fixed at the bottom
st.markdown("""
    <style>
    .sasuke-signature-bottom {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100vw;
        background: linear-gradient(120deg, rgba(20,41,90,0.85) 60%, #b3e0ff 100%);
        color: #FFF00;
        font-size: 1.2em;
        padding: 0.7em 0;
        text-align: center;
        z-index: 9999;
        text-shadow: 0 0 8px #b4e0ff, 0 0 2px #fff;
    }
    </style>
    <div class='sasuke-signature-bottom'>⚡ <em>Created by Uchiha Sasuke</em> ⚡</div>
""", unsafe_allow_html=True)