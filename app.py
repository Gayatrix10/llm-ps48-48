
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODEL_NAME = "gemini-3.5-flash-lite"

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Smart Notes Organizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- CUSTOM STYLING ----------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #F8F7FC;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        background: #F0ECFA;
        border-right: 1px solid #E5DDF5;
    }

    .hero {
        background: linear-gradient(120deg, #39216F, #7650C9);
        padding: 35px;
        border-radius: 22px;
        margin-bottom: 28px;
        color: white;
        box-shadow: 0 8px 25px rgba(74, 48, 130, 0.13);
    }

    .hero h1 {
        color: white;
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        color: #E8DFFF;
        font-size: 15px;
        line-height: 1.7;
    }

    .tag {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        color: white;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        margin: 12px 5px 0 0;
    }

    .section-title {
        font-size: 21px;
        font-weight: 700;
        color: #302052;
        margin-bottom: 5px;
    }

    .section-subtitle {
        font-size: 13px;
        color: #817A91;
        margin-bottom: 16px;
    }

    div[data-testid="stTextArea"] textarea {
        background: white;
        border: 1px solid #E5DDF5;
        border-radius: 13px;
        color: #302052;
        font-size: 14px;
        line-height: 1.8;
    }

    div[data-testid="stTextArea"] textarea:focus {
        border-color: #8060CF;
        box-shadow: 0 0 0 2px rgba(128,96,207,0.12);
    }

    .stButton > button {
        background: linear-gradient(110deg, #6241B5, #805BD0);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 20px;
        font-weight: 700;
        min-height: 48px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #503397;
        color: white;
        border: none;
    }

    .stDownloadButton > button {
        background: #F0EBFC;
        color: #593BA0;
        border: 1px solid #D9CEF2;
        border-radius: 11px;
        font-weight: 600;
        min-height: 43px;
    }

    .stDownloadButton > button:hover {
        background: #E5DDF8;
        color: #402675;
        border-color: #B9A7E6;
    }

    hr {
        border-color: #E9E3F3;
    }

    footer,
    #MainMenu {
        visibility: hidden;
    }

    /* Hide Streamlit Deploy button */
    [data-testid="stAppDeployButton"] {
        display: none !important;
    }

    /* Hide Streamlit status indicator */
    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("###  AI Settings")

    api_key = st.text_input(
        "Gemini API Key",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password",
        placeholder="Enter your API key",
    )

    st.caption(
        "Your API key is used to connect to Google's Gemini model."
    )

    st.divider()

    st.markdown("###    How it works ?")

    st.markdown(
        """
        01. Add your scattered notes.     
        02. Gemini identifies related topics.
        03. Get meaningful headings and bullet points.**
        04. Save your organized notes as Markdown.**      
        """
    )

    st.divider()

    st.markdown("###  Model Used ")
    st.code(MODEL_NAME)

    st.caption("Powered by Google Gemini API")


# ---------------- MAIN HEADER ----------------

st.markdown(
    """
    <div class="hero">
        <h1>Bring your scattered notes together. ✨</h1>
        <p>
            Transform unorganized thoughts, lecture notes and random ideas
            into beautifully structured, topic-wise notes using Generative AI.
        </p>
        <span class="tag">✦ AI Powered</span>
        <span class="tag">Smart Topic Grouping</span>
        <span class="tag">Markdown Export</span>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------- INPUT SECTION ----------------

st.markdown(
    '<div class="section-title">Your Notes 📝</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">Paste your notes below. '
    'Let AI take care of the organization.</div>',
    unsafe_allow_html=True,
)


# Sample notes

sample_notes = """ The Taj Mahal is located in Agra, India.
Photosynthesis converts light energy into chemical energy.
A startup business often begins by identifying an unmet customer need.
The Indian Constitution came into effect on 26 January 1950.
Python supports libraries such as NumPy and Pandas.
The Moon is Earth's natural satellite.
Brand positioning helps a company differentiate its products.
Water boils at approximately 100 degrees Celsius at standard atmospheric pressure.
A firewall monitors and controls incoming and outgoing network traffic.
Yoga combines physical postures, breathing and meditation.
The Amazon rainforest contains a large variety of plant and animal species.
A mutual fund pools money from multiple investors.
The Eiffel Tower is located in Paris, France.
Data visualization presents information through charts and graphs.
Renewable energy sources include solar, wind and hydropower.
"""


notes = st.text_area(
    "Paste your scattered notes here",
    value=sample_notes,
    height=230,
    placeholder="Start typing or paste your notes here...",
    label_visibility="collapsed",
)


# ---------------- CENTERED BUTTON ----------------

st.write("")

left_space, button_column, right_space = st.columns([1, 2, 1])

with button_column:

    organize_clicked = st.button(
        "Organize My Notes✨",
        use_container_width=True,
        type="primary",
    )


# ---------------- GEMINI PROCESSING ----------------

if organize_clicked:

    cleaned_notes = notes.strip()

    if not cleaned_notes:

        st.warning("Please enter some notes before organizing.")

    elif not api_key.strip():

        st.error("Please enter your Gemini API key in the sidebar.")

    else:

        prompt = f"""
You are an expert study-notes organizer.

Your task is to organize scattered notes into meaningful topic groups.

INSTRUCTIONS:

1. Carefully read all the notes.
2. Identify related concepts and group them together.
3. Generate clear and descriptive Markdown headings.
4. Use bullet points under each heading.
5. Preserve all important information and original meaning.
6. Remove exact duplicate information only.
7. Do not invent facts or add unsupported information.
8. Place unrelated notes under an appropriate separate heading.
9. Keep the output clean, structured and easy to revise.
10. Return only the organized notes in Markdown.

USER NOTES:

{cleaned_notes}
"""

        try:

            with st.spinner(
                "Gemini is analyzing and organizing your notes..."
            ):

                client = genai.Client(
                    api_key=api_key.strip(),
                    http_options=types.HttpOptions(timeout=60000),
                )

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                )

                organized_text = (response.text or "").strip()

            if organized_text:

                st.session_state["organized_notes"] = organized_text
                st.session_state["original_notes"] = cleaned_notes

                st.success(
                    "Your notes have been organized successfully!"
                )

            else:

                st.warning(
                    "Gemini returned an empty response. Please try again."
                )

        except Exception as error:

            error_message = str(error)

            if "503" in error_message:

                st.warning(
                    "Gemini is currently experiencing high demand. "
                    "Please try again shortly."
                )

            elif "429" in error_message:

                st.warning(
                    "API usage limit reached. Please check your Gemini quota."
                )

            elif "403" in error_message:

                st.error(
                    "API access denied. Check your API key and permissions."
                )

            else:

                st.error("Unable to organize your notes.")

                st.caption(
                    "Please check your connection and API configuration."
                )

                st.code(error_message)


# ---------------- OUTPUT SECTION ----------------

if "organized_notes" in st.session_state:

    # st.divider()

    st.markdown(
        '<div class="section-title">Organized Notes : </div>',
        unsafe_allow_html=True,
    )

    

    organized_text = st.session_state["organized_notes"]

    # Display organized Markdown

    with st.container(border=True):

        st.markdown(organized_text)

    st.write("")

    left_space, download_column, right_space = st.columns([1, 2, 1])

    with download_column:

        st.download_button(
            label=" Download Markdown ⬇️",
            data=organized_text,
            file_name="organized_notes.md",
            mime="text/markdown",
            use_container_width=True,
        )

  


# ---------------- FOOTER ----------------

st.divider()


