# Import necessary libraries
import streamlit as st  # Library to build web applications
import time  # For time control (delay)
from langchain_core.prompts import ChatPromptTemplate  # Template for chat prompts
from langchain_core.output_parsers import StrOutputParser  # Parser for string outputs
from langchain_community.chat_models import ChatOpenAI  # Chat model from OpenAI/compatible sources

# API configuration for DeepSeek (used via OpenRouter)
DEEPSEEK_API_KEY = "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"
DEEPSEEK_API_BASE = "https://openrouter.ai/api/v1"

# Function to initialize the Language Model (LLM)
def initialize_llm():
    return ChatOpenAI(
        model_name="deepseek/deepseek-chat-v3-0324:free",  # DeepSeek model used
        openai_api_key=DEEPSEEK_API_KEY,  # API key for authentication
        openai_api_base=DEEPSEEK_API_BASE,  # API base URL
        temperature=0.7,  # Response creativity level (0-1, higher = more creative)
        max_tokens=4000  # Maximum number of tokens in the response
    )

# Function to respond to user input
def respond_to_user(problem):
    llm = initialize_llm()  # Initialize the model
    
    # Create prompt template with system and user messages
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are CurhatIn AI, a good and empathetic listener created by Rafli Damara. 
        Your task is to listen to the user's concerns and respond by:
        1. Showing understanding and empathy
        2. Avoiding judgment
        3. Providing emotional support
        4. Giving wise advice if needed (but never forcing)
        5. Using casual, friendly language like a close friend
        
        Use "I" for yourself and "you" for the user.
        Do not pretend to know the solution to every problem.
        If the problem is very serious, suggest seeking professional help.
        
        Example:
        User: I feel very lonely lately
        Answer: I understand that loneliness can be very hard. You are not alone, many people feel the same. Do you want to share more about what makes you feel this way?
        
        User: My partner just broke up with me
        Answer: Oh no, that must really hurt your feelings right now. Breakups are never easy. I’m here to listen if you want to share more."""), 
        ("user", "{problem}")  # Placeholder for user input
    ])
    
    # Create processing chain: prompt -> model -> parser
    chain = prompt_template | llm | StrOutputParser()
    return chain.invoke({"problem": problem})  # Process user input

# Function to reset the conversation
def reset_conversation():
    st.session_state.chat_history = [{  # Reset chat history
        "role": "assistant", 
        "content": "Hi! I’m CurhatIn, what’s bothering you today?"  # Opening message
    }]
    st.rerun()  # Refresh the page

# Streamlit page configuration
st.set_page_config(
    page_title="CurhatIn: Your Best Confidant",  # Page title
    page_icon="❤️‍🩹",  # Page icon
    layout="wide"  # Wide layout
)

# Main interface
st.title("What do you want to share today?")  # Main title
st.markdown("")  # Blank space

# Sidebar
st.sidebar.title("❤️‍🩹 CurhatIn AI - (Beta)")  # Sidebar title
option = st.sidebar.selectbox(  # Dropdown for mode selection
    "",
    ("CurhatIn AI - (Close Friend v1.0)", "CurhatIn AI - (Bestie v2.1)", "CurhatIn AI - (Psychologist v1.1)"),
)
st.sidebar.markdown("")  # Blank space
st.sidebar.markdown("")  # Blank space
# App description
st.sidebar.markdown("CurhatIn AI is an AI-based platform that provides a safe space to share your thoughts and be your conversation partner 24/7.")
st.sidebar.markdown("")  # Blank space
# External link
st.sidebar.markdown("[Learn More](https://github.com/Rfldmr/vokabot-ai-customer-service-for-sv-ipb)")

st.sidebar.markdown("---")  # Divider line

# Privacy information
st.sidebar.info("CurhatIn AI **is not designed** to store any user input data, ensuring the system is free from potential data theft.")
st.sidebar.markdown("")  # Blank space

# Reset conversation button
if st.sidebar.button("Reset Conversation"):
    reset_conversation()

# Initialize chat history if it doesn't exist
if "chat_history" not in st.session_state:
    reset_conversation()
    
# Container to display chat messages
chat_container = st.container()
            
# Display chat history
with chat_container:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):  # Chat bubble according to role (user/assistant)
            st.markdown(message["content"])  # Display message content
            
# Chat input from user
if prompt := st.chat_input("Type what you want to share..."):
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
                
    # Display user message
    with chat_container:
        with st.chat_message("user"):
            st.markdown(prompt)
                
    # Display AI response
    with chat_container:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()  # Message placeholder
            with st.spinner("I’m listening carefully..."):  # Loading animation
                time.sleep(1)  # Delay for realism
                response = respond_to_user(prompt)  # Get AI response
                message_placeholder.markdown(response)  # Show response
                

    # Add AI response to history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    st.rerun()  # Refresh for updated display
