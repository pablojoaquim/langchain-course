import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("Hello from langchain-course!")
    print(f"OpenAI API Key: {openai_api_key}")
    if not openai_api_key:
        print("OpenAI API Key is not set.")
    else:
        print("OpenAI API Key is set.")
        
if __name__ == "__main__":
    main()