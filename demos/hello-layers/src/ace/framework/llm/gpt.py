# llm/gpt.py
from typing import List, TypedDict, Optional
import time
import openai


class GptMessage(TypedDict):
    role: str
    name: Optional[str]
    content: str


class GPT:

    def _create_conversation_completion(self, model, conversation: List[GptMessage], max_retries=5) -> GptMessage:
        for i in range(max_retries):
            try:
                # openai.api_key = self.api_key
                chat_completion = openai.ChatCompletion.create(
                    model=model,
                    messages=conversation
                )
                response = chat_completion.choices[0].message
                return response
            except Exception as e:
                print(f"Error: {e}. Attempt {i+1} of {max_retries}. Retrying...")
                time.sleep(1)  # wait for 1 second before retrying
        raise Exception("Max retries exceeded")

    def _create_image(self, prompt, size='256x256', max_retries=5) -> str:
        for i in range(max_retries):
            try:
                print("Generating image for prompt: " + prompt)
                openai.api_key = self.api_key
                result = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size=size
                )
                image_url = result.data[0].url
                print(".... finished generating image for prompt" + prompt + ":\n" + image_url)
                return image_url
            except Exception as e:
                print(f"Error: {e}. Attempt {i+1} of {max_retries}. Retrying...")
                time.sleep(1)  # wait for 1 second before retrying
        raise Exception("Max retries exceeded")