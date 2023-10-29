import openai
import os


openai.api_key = os.environ['GPT_API_KEY']


def gpt_summarize(text):
    ai_task = "summarize the following text:\n"
    message = [{"role": "assistant", "content": ai_task + text}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.2,
        max_tokens=500,
        frequency_penalty=0.0
    )

    summary = response['choices'][0]['message']['content']
    return summary
