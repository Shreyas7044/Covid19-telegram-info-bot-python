import requests
import json
from telegram.ext import Updater, CommandHandler

def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')

    if response.status_code == 200:
        data = response.json()
        global_summary = data['Global']

        message = (
            "🌍 COVID-19 Global Summary\n\n"
            f"New Confirmed: {global_summary['NewConfirmed']}\n"
            f"Total Confirmed: {global_summary['TotalConfirmed']}\n"
            f"New Deaths: {global_summary['NewDeaths']}\n"
            f"Total Deaths: {global_summary['TotalDeaths']}\n"
            f"New Recovered: {global_summary['NewRecovered']}\n"
            f"Total Recovered: {global_summary['TotalRecovered']}"
        )

        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="❌ Error fetching data. Please try again later.")

def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('summary', summary))

    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == '__main__':
    main()