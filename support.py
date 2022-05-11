#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os

from telegram import ForceReply, Update
from telegram.ext import Application, CallbackContext, CommandHandler, MessageHandler, filters

TOKEN = os.getenv('TG_SUPPORT_TOKEN')


# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    # await update.message.reply_html(rf"Hi {user.mention_html()}!",reply_markup=ForceReply(selective=True))
    await update.message.reply_html("Здравствуйте!", reply_markup=ForceReply(selective=True))


async def echo(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    text = update.message.text
    # print(text)
    await update.message.reply_text(text)


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # application.add_handler(MessageHandler(filters.TEXT, echo))
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(stop_signals=None)


if __name__ == "__main__":
    main()
