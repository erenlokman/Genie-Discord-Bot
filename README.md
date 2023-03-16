# Genie Discord Bot

Genie is a GPT-3 powered Discord bot that provides answers to user questions and stores the questions, answers, and user nicknames in a JSON file. It leverages OpenAI's GPT-3 model to generate high-quality, contextually relevant responses to user questions.

## Features

- Answer questions using OpenAI's GPT-3 API
- Store questions, answers, and user nicknames in a JSON file
- Easy setup using environment variables

## Setup

1. Clone this repository:

git clone https://github.com/yourusername/Genie-Discord-Bot.git
cd Genie-Discord-Bot

2. Install the required dependencies:

pip install -r requirements.txt

3. Create a .env file in the project directory and add your API keys:

DISCORD_API_KEY=your_discord_api_key
OPENAI_API_KEY=your_openai_api_key

4. Run the bot:

python genie.py

Now, your Genie Discord bot should be up and running. Users can ask questions using the !ask command.

# Tech Stack

1. Language: Python
2. Discord API Wrapper: discord.py
3. OpenAI API: openai
4. Environment Variables Management: python-dotenv

These are the primary components required to build and run the Genie Discord Bot project. Python is the programming language used, and discord.py is the library that allows interaction with the Discord API. The openai library is used to interact with the OpenAI GPT-3 API, and python-dotenv is used for managing environment variables.
