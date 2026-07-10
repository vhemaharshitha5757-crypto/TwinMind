import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


class GeminiService:

    def ask(self, question, incident):

        prompt = f"""
You are TwinMind AI, an enterprise incident response assistant.

Below is the incident information.

Incident:
{incident}

User Question:
{question}

Instructions:
- Answer only using the provided incident information.
- If the answer is not available, reply:
  "The incident data does not contain enough information."
- Keep the answer concise and professional.
"""

        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-3.3-70b-instruct:free",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0.2,
                max_tokens=300,
            )

            return response.choices[0].message.content

        except Exception as e:
            print("OpenRouter Error:", e)
            return f"AI Error: {str(e)}"