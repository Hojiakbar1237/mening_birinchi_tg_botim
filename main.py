from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
TOKEN = "5696114800:AAE0GgugCZmja_pzhnsxJk9gUWH9ai3ithQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Salom!\nMenga nimadir yoz!")
'''
@dp.message_handler(commands=['start', 'help'])

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def exxxo_message(msg: types.Message):
    await msg.reply(text=msg.text.upper()) '''

@dp.message_handler(Text(equals="kamandalar"))
async def get_kamandalar(message: types.Message):
    text = """
    /newbot - create a new bot
/mybots - edit your bots [beta]
    """
    await message.answer(text=text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
