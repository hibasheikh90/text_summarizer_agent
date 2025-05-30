Gemini-Powered Text Summarizer Agent
Overview
Yeh ek simple chatbot agent hai jo Google Gemini AI ke API ko use karke user ke diye hue text ka summary banata hai. Yeh Chainlit framework par bana hai jo chat applications develop karna easy banata hai.

Features
User se input text leta hai.

Gemini AI ke generative models se text ka concise summary banata hai.

Multiple Gemini models try karta hai aur pehla available model use karta hai.

Text chhota ho (kam se kam 50 characters) to user ko warning deta hai.

Real-time chat interface mein user ke messages ka summary reply karta hai.

API key environment variable .env file se securely load karta hai.

Technologies Used
Python 3.8+

Chainlit — Chatbot framework for real-time chat interactions.

Google Generative AI (Gemini) — Text summarization model.

dotenv — Load environment variables from .env file.

Async programming — Chat events aur API calls asynchronous hain for better performance.

How It Works
API Key Setup:

.env file mein GEMINI_API_KEY set karni hoti hai.

Code us key ko environment se leta hai aur Gemini AI ko configure karta hai.

Model Initialization:

Jab chat start hota hai (on_chat_start event), agent Gemini ke multiple models check karta hai:

gemini-1.5-flash

gemini-2.0-flash

models/text-bison-001

Pehla jo model available hota hai use load karta hai.

User Interaction:

User chat mein koi bhi text bhejta hai.

Agent text ko Gemini model ko bhejta hai prompt ke saath jisme summary banani hoti hai.

Gemini model summarized text generate karta hai.

Agent summarized text user ko chat mein wapas bhejta hai.

Validation:

Text agar chhota ya empty hoga to user ko batata hai ke text zyada lamba bhejen (kam se kam 50 characters).

Usage
.env file banayein aur usme apni Gemini API key likhein:

ini
Copy
Edit
GEMINI_API_KEY=your_actual_api_key_here
Dependencies install karein:

bash
Copy
Edit
pip install google-generativeai chainlit python-dotenv
Application chalayein (Chainlit se):

bash
Copy
Edit
chainlit run your_script_name.py
Chat start karne par aapko welcome message milega. Phir apna koi bhi lamba text paste karein, aur aapko uska summarized text mil jayega.

Notes
API key sahi hona chahiye warna model load nahi hoga.

Gemini AI model ki availability ke mutabiq hi summary milegi.

Summary approx 150 words ki hoti hai, lekin aap summarize_text function mein word_limit adjust kar sakte hain.

Summary
Is project mein maine ek chatbot banaya hai jo Google Gemini AI ko use karta hai taake user ke texts ko summarize kar sake. Yeh bot asynchronous programming aur Chainlit framework se chat experience smooth banata hai. User ke texts ko analyze karke clear aur concise summaries provide karta hai.
