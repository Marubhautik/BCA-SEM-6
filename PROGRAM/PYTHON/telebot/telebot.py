from telegram import Bot, MessageEntity, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, bot, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          Dispatcher, CallbackQueryHandler, CallbackContext)
import logging
import json, re
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

# telegram bot token
TOKEN = "5243368069:AAHbax3Tsn15YG45K4Kv10h9UcWCZJGLI90"

# Enable logging
logging.basicConfig(filename='pvChat_bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# The complete pattern for any kind of URLs
url_pattern = re.compile(r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.]
				(?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi
				|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq
				|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv
				|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd
				|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd
				|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id
				|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky
				|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo
				|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz
				|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb
				|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td
				|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc
				|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]
				*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]
				*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:
				[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|
				info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag
				|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm
				|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs
				|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk
				|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk
				|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki
				|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg
				|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni
				|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re
				|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su
				|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug
				|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))""")

# Read more: https://developers.google.com/api-client-library/python/auth/service-accounts
scopes = ['https://www.googleapis.com/auth/urlshortener']


# def start(bot, Update):
#     print("start called")
#     print("Hellow:"+Update.message.text)
#     Update.message.reply_text(u'Welcome to the best Url shortener\nJust send me a link and I\'ll shorten it.')
def start(update: Update, context: CallbackContext):
    print(update.message.text)
    update.message.reply_text(
        "Enter the text you want to show to the user whenever they start the bot")

def insert(update: Update, context: CallbackContext):
    print("inserted called")
    print(update.message.text)
    print(update.message.caption)
    user = update.message.from_user

    text = update.message.text
    caption = update.message.caption

    if text:
        print("if called")
        urls = url_pattern.findall(text)
        print(urls)
        if urls:
            longUrl = urls[0]
            print(longUrl)# Just select the first URL in the text for shortening
        else:
            invalid_link(update,CallbackContext)
            return
    elif caption:
        print("elseif called")
        urls = url_pattern.findall(caption)
        if urls:
            longUrl = urls[0]  # Just select the first URL in the caption for shortening
        else:
            invalid_link(update,CallbackContext)
            return
    else:
        print("else called")
        invalid_link(update,CallbackContext)
        return

    # Connect to google API service
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/path/to/googleProject.json', scopes)
    http_auth = credentials.authorize(Http())
    service = build('urlshortener', 'v1', http=http_auth)

    body = {'longUrl': longUrl}
    response = service.url().insert(body=body).execute()

    keyboard = [[InlineKeyboardButton("Refresh total clicks", callback_data=response['id'] + ' 0')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    longUrl = response['longUrl']
    shortUrl = response['id'].split('//')[1]
    update.message.reply_text('Long url: {}\n\nShort url: {}\n\nTotal clicks: 0\n'.format(longUrl, shortUrl),
                              reply_markup=reply_markup)


def get(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.callback_query.from_user

    shortUrl = query.data.split()[0]
    old_number_of_clicks = query.data.split()[1]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/path/to/googleProject.json', scopes)
    http_auth = credentials.authorize(Http())
    service = build('urlshortener', 'v1', http=http_auth)

    try:
        response = service.url().get(shortUrl=shortUrl, projection='ANALYTICS_CLICKS').execute()

        longUrl = response['longUrl']
        shortUrl = response['id'].split('//')[1]
        totalClicks = response['analytics']['allTime']['shortUrlClicks']
        number_of_new_clicks = int(totalClicks) - int(old_number_of_clicks)

        if number_of_new_clicks is 0:
            update.callback_query.answer(text='No new click!🖱', cache_time=0)
            return
        elif number_of_new_clicks is 1:
            update.callback_query.answer(text='{} new click!👌'.format(str(number_of_new_clicks)), cache_time=0)
        else:
            update.callback_query.answer(text='{} new clicks!👌'.format(str(number_of_new_clicks)), cache_time=0)

        keyboard = [[InlineKeyboardButton("Refresh total clicks", callback_data=response['id'] + ' ' + totalClicks)]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        bot.edit_message_text(
            'Long url: {}\n\nShort url: {}\n\nTotal clicks: {}\n'.format(longUrl, shortUrl, totalClicks),
            chat_id=query.message.chat_id, message_id=query.message.message_id, reply_markup=reply_markup)

    except Exception as e:  # message was not modified! It means there is no new click...
        print(e)


def invalid_link(update: Update, context: CallbackContext):
    user = update.message.from_user
    print(user)
    update.message.reply_text('Oops! Your message seems to not have any regular Link...!!! 🙄')


# return SEND_TEXT


def error(update: Update, context: CallbackContext, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main(webhook_url=None):
    # Get the dispatcher to register handlers
    updater = Updater("5243368069:AAHbax3Tsn15YG45K4Kv10h9UcWCZJGLI90")
    bot = updater.bot
    dp = updater.dispatcher
    print("Hekkiw")
    start_handler = CommandHandler('start', start)
    insert_handler = MessageHandler(Filters.all, insert)
    dp.add_handler(start_handler)
    dp.add_handler(insert_handler)
    dp.add_handler(CallbackQueryHandler(get))
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()


main()
