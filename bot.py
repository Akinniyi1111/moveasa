import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token
BOT_TOKEN = "7812007390:AAGxzTXV3fP3pjOhbp3pjASER_vsDU60F3U"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Your bot is alive and working perfectly.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Bot Commands*\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/menu - Show main menu",
        parse_mode="Markdown"
    )

# /menu command
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛍 Main Menu:\n\n"
        "🔹 Option 1: Youtube Tools\n"
        "🔹 Option 2: Instagram Tools\n"
        "🔹 Option 3: Facebook Tools\n"
        "🔹 Option 4: TikTok Tools\n\n"
        "👉 Reply /help anytime for help!"
    )

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("menu", menu))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
