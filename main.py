import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI

MODEL_NAME = "openrouter/free"


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    working_directory = os.path.abspath("/home/jcuz/workspace/jcuz/cuz-agent")
    target_dir = os.path.normpath(os.path.join(working_directory, directory))

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    args = parse_args()

    chat_messages = build_messages(args.user_prompt)

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=chat_messages,
    )

    print_response(args.verbose, response, chat_messages)


def parse_args():
    parser = argparse.ArgumentParser(description="Cuzbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def build_messages(user_prompt):
    return [{"role": "user", "content": user_prompt}]


def print_response(verbose, response, chat_messages):
    if verbose:
        print(f"User prompt: {chat_messages}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response: {response.choices[0].message.content}")


if __name__ == "__main__":
    main()
