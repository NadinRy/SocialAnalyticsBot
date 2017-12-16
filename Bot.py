import telebot
from ToneAnalyzer import ToneAnalyzer
from TwitterCrawler import TwitterCrawler

token = "494262611:AAFsbPdr0BHy-LuIVvkiomx4kigJ-sGOblA"
bot = telebot.TeleBot(token)
update = bot.get_updates()
last_update = update[-1]
last_chat_text = last_update.message.text
last_chat_id = last_update.message.chat.id
last_username = last_update.message.from_user.first_name

isRateCommandActive = 0


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hello, {}!\nWelcome to the social rating studio!\n "
                                   "Here are the commands to use here\n"
                                   "/rateit - start assessment".format(message.from_user.first_name))


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "This bot provides the assessment of emotional, writing and social tone of various things or objects.\n\n"
                                   "<b>List of commands with description</b>"
                                   "\n/start - begin using this rating bot"
                                   "\n/rateit - start assessment process. Please specify the name of the thing to be assessed as precisely as possible"
                                   "\n/help - view the list of commands with description"
                                   "\n/givefeedback - submit feedback about the bot functioning")


@bot.message_handler(commands=['rateit'])
def handle_rate(message):
    global isRateCommandActive
    isRateCommandActive = 1
    bot.send_message(message.chat.id, "Great!\n"
                                   "In order to start assessment process, please enter the name of the thing "
                                   "you wish to get rating for."
                                   "\nExample: (USA election)")


@bot.message_handler(content_types='text')
def rating(message):
    if isRateCommandActive == 1:
        new_search = TwitterCrawler()
        text = new_search.tweet_search('#' + message.text.strip())

        if text == '':
            bot.send_message(message.chat.id, 'Sorry, information is not found.')
        else:
            bot.send_message(message.chat.id, "Wait please. The analysis is in process")
            analyzer = ToneAnalyzer(text)
            analytics = analyzer.analyze_tone()

            bot.send_message(message.chat.id, analytics)

    else:
        bot.send_message(message.chat.id, "I can't understand you. If you want to analyze this text, use /rateit")




bot.polling()


