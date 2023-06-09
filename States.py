from configuration import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import re

pattern = re.compile("^\+?998[0-9]{9}$")
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
rkb = ReplyKeyboardMarkup(resize_keyboard=True)
rkb.add(KeyboardButton("Ariza toldirish"))


class Form(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    email = State()


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text="Assalomu aleykum botimizga xush kelibsiz",
                         reply_markup=rkb)


async def on_startup(_):
    print("bot run")


@dp.message_handler(Text(equals="Ariza toldirish"))
async def fill_form(message: types.Message):
    await Form.name.set()
    await message.answer("Ismingizni kiriting")


@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    """
    Set user name
    """
    async with state.proxy() as data:
        data['name'] = message.text

    await  Form.next()
    await message.answer("yoshingizni kiriting : ")


@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def avoid_age_format(message: types.Message):
    await message.answer("yosh faqat sonlardan iborat bolishi kerak ! ")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await Form.next()
    await message.answer("Telefon raqamingizni kiriting :")

@dp.message_handler(lambda message: re.match(pattern, message.text), state=Form.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    msg = f"name: {data['name']}, \n age: {data['age']}, \n phone: {data['phone_number']}"
    await bot.send_message(chat_id=message.from_user.id, text=msg)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,
                           skip_updates=True)
