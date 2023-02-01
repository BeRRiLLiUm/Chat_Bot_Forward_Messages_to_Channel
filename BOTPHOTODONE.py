import logging
from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#для корректной работы бота необходимо установить библиотеку telegram(pip3 install python-telegram-bot==12.8 либо pip install python-telegram-bot==12.8)
#установка библиотеки в терминале, последующий импорт (1- python3, 2- import telegram)
#установка более поздней версии библиотеки приведет к ошибкам синтаксиса, требует доработки.
#python 3.11, возможна работа на более ранних версиях(2021 год и ранее)
#должен быть доступ к интернету
#если выдает ошибку, проблема в версии питона, версии библиотеки телеграм либо отсутствие подключения к интернету.

logging.basicConfig(format='%(asctime)s - message done - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot: Bot, update: Update):
    name = update.message.from_user.first_name
    update.message.reply_text("🤖Привет, {}, это бот для фотоотчета LuxStore. ".format(name))
    update.message.reply_text("Тебе необходимо отправить фото, и подписать его в таком формате:\nИмя, адрес точки, время и причина отправки(открытие/закрытие смены).\n\nНапример: Александр Васильев, ул.Пушкина,д.Колотушкина,ТЦ Красная Заря, 9:55, открытие смены.")
    #update.message.reply_text("За несоблюдение формата отправки, фотоотчет не засчитывается.")


def echo(bot: Bot, update: Update):
    if update.message.photo:
        #chat-id - айди группы,куда пересылаются фото и текст
        bot.forward_message(chat_id='-1001880947365', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        bot.send_message(chat_id=update.message.chat_id, text="Photo is done.")
    else:
        bot.forward_message(chat_id='-1001880947365', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        bot.send_message(chat_id=update.message.chat_id, text="Text is done.")

def main():
    #токен бота, берется в телеграм боте bot-father, там же создается бот и выдается токен, который необходимо вставить ниже
    bot = Bot(token='5966930989:AAHAdzX6QHHgfhmSlh6k6tVrzkaS9pYcl3c')
    updater = Updater(bot=bot)

    startbot = CommandHandler('start', start)
    updater.dispatcher.add_handler(startbot)

    handler = MessageHandler(Filters.photo | Filters.text, echo)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    #бот работает пока не остановишь, обычно ошибок нет.
    #на отправку голосовых и документов никак не реагирует, не слетает. В консоль записывает каждую корректную отправку