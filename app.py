import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from PIL import Image


st.set_page_config(page_title="🌍 GenAI Travel Assistant", page_icon="🧭", layout="centered")
st.title("🌍 **GenAI Travel Assistant**")
st.write("Hey Buddy! I'm your AI travel planner — tell me where you're going, and how you'd like to travel 🚀")

st.divider()
# Input 1: Source Location
# Input 2: Destination Location
# Input 3: Mode of Transport
source = st.text_input("Source", placeholder="Eg: Hyderabad")
destination = st.text_input("Destination", placeholder="Eg: New Delhi")
mode = st.selectbox("Mode of Transport", options=["bus", "train", "flight","car","bike","walk"], 
                    placeholder="Choose an option")

mode_images = {
    "car": "Car.jpeg",
    "bike": "Bike.png",
    "train": "Train.png",
    "flight": "Flight.png",
    "bus": "BUS.jpeg",
    "walk": "Walk.png"
}

if mode in mode_images:
    try:
        img = Image.open(mode_images[mode])
        st.image(img, caption=f"Mode: {mode.title()}", use_container_width=False)
    except Exception as e:
        st.warning(f"⚠️ Could not load image for {mode}: {e}")

st.divider()

# Response Format: Output the cost estimation only. Donot give any suggestions
btn_click = st.button("Estimate Travel Cost")

# Template
chat_template = ChatPromptTemplate(
    messages = [
        ("system", """Act as a Travel Cost Estimation AI Assistant. You are an AI who takes user's input and 
                      find the estimated cost of travel. Make sure not to estimate the cost of staying at the location. 
                      User will enter 3 inputs. 
                      Input 1: Source Location
                      Input 2: Destination Location
                      Input 3: Mode of Transport
                      
                      Response Format: Output the cost estimation only. Donot give any suggestions."""), 
        ("human", "I want to travel to {destination} from {source} via {mode}.")
    ]
)

# Chat Model
chat_model = ChatGoogleGenerativeAI(api_key="your api key", 
                                    model="gemini-2.0-flash-exp", 
                                    temperature=1)

# Output Parser
output_parser = StrOutputParser()

# Chaining
chain = chat_template | chat_model | output_parser

if btn_click==True:
    raw_input = {"destination": destination, "mode": mode, "source": source}
    st.write(chain.invoke(raw_input))