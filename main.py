import os
import google.generativeai as genai
from dotenv import load_dotenv
import chainlit as cl

# Load environment variables from .env file
load_dotenv()


api_key = os.environ.get("GEMINI_API_KEY", "").strip()
if not api_key:
    raise ValueError("GEMINI_API_KEY not found or is empty in .env file.")


genai.configure(api_key=api_key)


model = None

# Chainlit event: when chat starts
@cl.on_chat_start
async def start():
    global model

    # Welcome messages
    await cl.Message(content="--- Welcome to the Gemini-Powered Text Summarizer Agent ---").send()
    await cl.Message(content="Please paste the text you want to summarize. I will summarize each message you send.").send()

    # Try loading 
    model_names = ['gemini-1.5-flash', 'gemini-2.0-flash', 'models/text-bison-001']
    for model_name in model_names:
        try:
            model = genai.GenerativeModel(model_name)
            await cl.Message(content=f"Using model: `{model_name}`").send()
            break
        except Exception as e:
            await cl.Message(content=f"Could not load `{model_name}`: {e}").send()

    if model is None:
        await cl.Message(content="Agent could not start. Please check your API key and model availability.").send()


async def summarize_text(text_to_summarize: str, word_limit: int = 100) -> str:
    """
    Uses Gemini API to summarize the given text.
    """
    if not text_to_summarize or len(text_to_summarize.strip()) < 50:
        return "Please provide a longer text to summarize (at least 50 characters)."

    prompt = f"Summarize the following text concisely in approximately {word_limit} words:\n\n{text_to_summarize}\n\nSummary:"

    try:
        if model is None:
            return "Model is not initialized. Please restart the chat or check server logs."

        
        response = await model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No summary could be generated."
    except Exception as e:
        return f"Sorry, I couldn't summarize the text. An error occurred: {e}"

# Chainlit event: when user sends a message
@cl.on_message
async def handle_message(message: cl.Message):
    user_text = message.content.strip()

    if model is None:
        await cl.Message(content="Model is not ready. Please try again later or restart the application.").send()
        return

    
    summary = await summarize_text(user_text, word_limit=150)
    await cl.Message(content=f"--- Your Summary ---\n{summary}").send()
