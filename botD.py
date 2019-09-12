from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater('668790236:AAEZRbHTkho-Bgcmzn1CCL67x6XqJaoGR-k', request_kwargs=PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
