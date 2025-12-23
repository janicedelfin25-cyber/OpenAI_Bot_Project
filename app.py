import os
import streamlit as st
from openai import OpenAI

# Set page config FIRST before any other streamlit commands
st.set_page_config(
    page_title="Digital Marketing Consultancy Bot",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_key_valid" not in st.session_state:
    st.session_state.api_key_valid = False

# Get API key from environment or secrets
api_key = None
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ API Key Error")
    st.markdown("""
    ### Missing OpenAI API Key
    
    The OPENAI_API_KEY is not configured.
    
    **To fix this on Streamlit Cloud:**
    1. Go to your Streamlit Cloud app dashboard
    2. Click on your app → **Settings** (gear icon in top right)
    3. Go to **Secrets** tab
    4. Add this line:
       ```
       OPENAI_API_KEY=your_openai_api_key_here
       ```
    5. Click **Save** and your app will redeploy automatically
    
    **For local development:**
    1. Create `.streamlit/secrets.toml` file
    2. Add: `OPENAI_API_KEY="your_key_here"`
    3. Run: `streamlit run streamlit_app.py`
    """)
    st.stop()

try:
    client = OpenAI(api_key=api_key)
    st.session_state.api_key_valid = True
except Exception as e:
    st.error(f"❌ API Configuration Error: {str(e)}")
    st.markdown(f"**Error details:** {str(e)}")
    st.stop()

# Header
st.markdown("# 🎯 Digital Marketing Consultancy Bot")
st.markdown("*Powered by OpenAI GPT-3.5-turbo*")

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    mode = st.radio(
        "Select Mode:",
        ["💬 Chat", "📊 Strategy Analysis", "📱 Social Media Plan", "🔍 SEO Audit", "💰 Budget Planning"]
    )
    
    temperature = st.slider(
        "Temperature (Creativity):",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Lower = more focused, Higher = more creative"
    )
    
    max_tokens = st.slider(
        "Response Length:",
        min_value=100,
        max_value=2000,
        value=1000,
        step=100
    )
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.success("Chat history cleared!")
    
    st.markdown("---")
    st.markdown("""
    ### 📖 About This Bot
    
    This is an AI-powered digital marketing consultant. Ask questions about:
    - Marketing strategy
    - Social media tactics
    - SEO optimization
    - Budget allocation
    - Conversion optimization
    - And much more!
    """)

# System prompts for different modes
system_prompts = {
    "💬 Chat": """You are an expert digital marketing consultant with 15+ years of experience.
Provide specific, actionable recommendations tailored to the user's situation.
Be professional yet approachable. Ask clarifying questions when needed.""",
    
    "📊 Strategy Analysis": """You are a strategic digital marketing expert. Analyze marketing strategies and provide:
1. Strengths and weaknesses
2. Opportunities for improvement
3. Risks and mitigation strategies
4. ROI estimation
5. 90-day action plan
Be data-driven and specific in your recommendations.""",
    
    "📱 Social Media Plan": """You are a social media marketing specialist. Create comprehensive social media strategies including:
1. Platform selection and justification
2. Content calendar overview
3. Posting frequency and best times
4. Content types and themes
5. Engagement strategies
6. Analytics metrics
7. Budget allocation
Provide actionable, specific recommendations.""",
    
    "🔍 SEO Audit": """You are an SEO expert. Provide comprehensive SEO recommendations including:
1. On-page SEO improvements
2. Technical SEO fixes
3. Backlink strategy
4. Keyword research focus areas
5. Content optimization priorities
6. Local SEO recommendations
7. Competitive analysis insights
8. Implementation roadmap with timeline
Be thorough and technical yet understandable.""",
    
    "💰 Budget Planning": """You are a marketing finance strategist. Create detailed budget allocation plans including:
1. Recommended channel allocation (percentages and amounts)
2. Justification for each allocation
3. Expected ROI by channel
4. Month-by-month breakdown
5. Quick wins vs. long-term investments
6. Contingency recommendations
7. Key metrics to monitor per channel
Provide realistic, data-backed recommendations."""
}

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask your digital marketing question...", key="user_input")

if user_input:
    # Add user message to session state
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get response from OpenAI
    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            try:
                # Prepare messages for API
                messages_for_api = [
                    {"role": "system", "content": system_prompts[mode]}
                ] + st.session_state.messages
                
                # Call OpenAI API
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages_for_api,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                
                # Extract and display response
                assistant_message = response.choices[0].message.content
                st.markdown(assistant_message)
                
                # Add assistant message to session state
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                st.error(error_msg)
                # Remove the user message if there was an error
                st.session_state.messages.pop()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🎯 Digital Marketing Consultancy Bot | Powered by OpenAI</p>
    <p style='font-size: 0.8em'>This bot provides marketing advice based on current best practices and data-driven strategies.</p>
</div>
""", unsafe_allow_html=True)
