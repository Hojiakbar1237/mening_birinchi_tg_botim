from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

TOKEN = "5696114800:AAE0GgugCZmja_pzhnsxJk9gUWH9ai3ithQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton(text="/start"))
rkb.add(KeyboardButton(text="/help"))

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("❤",callback_data="Like")],
    [InlineKeyboardButton("👎",callback_data="dislike")]
])

'''@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Salom!\nMenga nimadir yoz!")'''
'''
@dp.message_handler(commands=['start', 'help'])

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def exxxo_message(msg: types.Message):
    await msg.reply(text=msg.text.upper()) '''


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSggLLCvYrZQQWp78JRBj4JkxN6lpMGLps2uDFp1uY5Zg&s",
                         caption="Bu rasm sizga yoqdimi ?",
                         reply_markup=rkb)

@dp.callback_query_handler(text="Like")
async def like_button(callback:types.CallbackQuery) :  #yurakchani boskanda you likr it sozini korsatadi
    await  callback.answer("You like it")

@dp.callback_query_handler(text="dislike")
async def like_button(callback:types.CallbackQuery) :
    await  callback.answer("You don't like it")


# locatsiyani jonatis]h
'''@dp.message_handler(Text(equals="Location"))
async def get_location(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,latitude=41.29871,longitude=69.22215)  '''


@dp.message_handler(Text(equals="kamandalar"))
async def get_kamandalar(message: types.Message):
    text = """
    /newbot - create a new bot
/mybots - edit your bots [beta]
    """
    await message.answer(text=text)




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
