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
    bot.send_message(last_chat_id, "Hello, {}!\nWelcome to the social rating studio!\n "
                                   "Here are the commands to use here\n"
                                   "/rateit - start assessment".format(last_username))


@bot.message_handler(commands=['rateit'])
def handle_rate(message):
    global isRateCommandActive
    isRateCommandActive = 1
    bot.send_message(last_chat_id, "Great!\n"
                                   "In order to start assessment process, please enter the name of the thing "
                                   "you wish to get rating for."
                                   "\nExample: (USA election)")


@bot.message_handler(content_types='text')
def rating(message):
    if isRateCommandActive:
        new_search = TwitterCrawler()
        text = new_search.tweet_search('#' + message.text.strip())

        analyzer = ToneAnalyzer(text)
        analytics = analyzer.analyze_tone()

        bot.send_message(last_chat_id, analytics)


bot.polling()
