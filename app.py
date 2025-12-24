import os
import streamlit as st
from openai import OpenAI

# Set page config FIRST
st.set_page_config(
    page_title="Marketing Bot",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Get API key
api_key = None
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ API Key Error - OPENAI_API_KEY not configured")
    st.info("Add OPENAI_API_KEY to Streamlit Secrets (Settings → Secrets tab)")
    st.stop()

try:
    client = OpenAI(api_key=api_key)
except Exception as e:
    st.error(f"❌ API Error: {str(e)}")
    st.stop()

# Header
st.title("🎯 Digital Marketing Consultancy Bot")
st.caption("Powered by OpenAI GPT-3.5-turbo")

# Sidebar
with st.sidebar:
    st.subheader("⚙️ Settings")
    
    mode = st.selectbox(
        "Mode:",
        ["💬 Chat", "📊 Strategy Analysis", "📱 Social Media Plan", "🔍 SEO Audit", "💰 Budget Planning"],
        index=0
    )
    
    temperature = st.slider(
        "Temperature:",
        0.0, 1.0, 0.7, 0.1
    )
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.success("Chat cleared!")

# System prompts
system_prompts = {
    "💬 Chat": "You are an expert digital marketing consultant with 15+ years of experience. Provide specific, actionable recommendations.",
    "📊 Strategy Analysis": "You are a strategic digital marketing expert. Analyze marketing strategies and provide: strengths, weaknesses, opportunities, risks, ROI estimation, and 90-day action plan.",
    "📱 Social Media Plan": "You are a social media marketing specialist. Create comprehensive social media strategies with platform selection, content calendar, posting frequency, engagement strategies, and metrics.",
    "🔍 SEO Audit": "You are an SEO expert. Provide comprehensive SEO recommendations: on-page, technical, backlink strategy, keyword research, content optimization, and implementation roadmap.",
    "💰 Budget Planning": "You are a marketing finance strategist. Create detailed budget allocation plans with percentages, justifications, ROI by channel, month-by-month breakdown, and contingency recommendations."
}

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Ask your digital marketing question...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompts[mode]}
                    ] + st.session_state.messages,
                    temperature=temperature,
                    max_tokens=800
                )
                
                assistant_message = response.choices[0].message.content
                st.write(assistant_message)
                
                st.session_state.messages.append({"role": "assistant", "content": assistant_message})
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.session_state.messages.pop()
