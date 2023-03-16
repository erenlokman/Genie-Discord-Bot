import logging
import openai
import json
import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

DC_API_KEY = os.environ["DISCORD_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command(name="ask")
async def ask(ctx, *, question):
    print(f"{ctx.author.name} asked: {question}")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{question}\n\n",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    answer = response.choices[0].text.strip()
    save_question_and_answer_to_file(question, answer)

    await ctx.send(f"Answer: {answer}")


@ask.error
async def ask_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a question.")
    else:
        await ctx.send(f"An error occurred while processing your question: {error}")


@bot.command(name="test")
async def test(ctx):
    await ctx.send("Test command received!")


@test.error
async def test_error(ctx, error):
    await ctx.send(f"An error occurred while processing the test command: {error}")


def save_question_and_answer_to_file(question, answer):
    print(f"Saving question and answer to file: {question} - {answer}")
    questions_file = "questions.json"

    if os.path.exists(questions_file):
        with open(questions_file, "r") as file:
            data = json.load(file)
    else:
        data = {"entries": []}

    data["entries"].append({"question": question, "answer": answer})

    with open(questions_file, "w") as file:
        json.dump(data, file, indent=4)


bot.run(DC_API_KEY)
