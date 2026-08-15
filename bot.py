import random
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ============================================
# EDIT THIS LINE - Put your bot token here
# ============================================
TOKEN = "8636741510:AAEhlG6iuj_WtFMR-aKWKFs1U0TCCrO5dO88636741510:AAEhlG6iuj_WtFMR-aKWKFs1U0TCCrO5dO8"
# ============================================

logging.basicConfig(level=logging.INFO)

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = random.choice(['Heads', 'Tails'])
    if result == 'Heads':
        await update.message.reply_text("🪙👤 Heads!")
    else:
        await update.message.reply_text("🪙🦅 Tails!")

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        dice_msg = await update.message.reply_dice(emoji="🎲")
        await asyncio.sleep(2)
        result = dice_msg.dice.value
        dice_emojis = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
        await update.message.reply_text(f"{dice_emojis[result]} {result}!")
    except Exception as e:
        await update.message.reply_text("❌ Error!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎰 Commands:\n/coin\n/dice")

def main():
    if TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Edit bot.py and add your token!")
        return
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("coin", coin))
    app.add_handler(CommandHandler("dice", dice))
    
    print("🤖 Bot running! Commands: /coin, /dice")
    app.run_polling()

if __name__ == "__main__":
    main()
