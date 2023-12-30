# C102 - Homework Completer - Yuvanth B
"""
=> Packages used in this project:
1. Google Gemini AI
2. OpenCV (for Gemini to process)
"""

# Importing Packages
from homework import read_content   # My package
import google.generativeai as genai # Google Gemini
import cv2                          # OpenCV

genai.configure(api_key="AIzaSyBqmOpqydkpy2u-R7ewi7B5YSNYP3bpwxQ") # Configuring using API

# Setting up the AI Model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# Safety Settings
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT", # Blocks all harrasment talk
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH", # Blocks all bad words
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT", # Blocks dangerous (like hacking, SQL Injection) and terriost talk and information
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
]) # Starts the chat, I have cleared the history and cache

convo.send_message(read_content()) # Sending the AI the homework assignment
print("Answers: ")
print()
print(convo.last.text)
