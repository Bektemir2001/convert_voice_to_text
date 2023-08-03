import time
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from aiogram.dispatcher.filters.state import State, StatesGroup
from env import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


class UserState(StatesGroup):
    CHOOSING = State()

memory = {}


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    logging.info(f'{user_id} {time.asctime()}')
    await message.reply(f"Привет отправите аудио или голосовой. Я переведу в текст")


@dp.message_handler(content_types=ContentType.VOICE)
async def handle_voice_message(message: types.Message):
    voice = message.voice
    # здесь можно обработать полученный голосовой файл, например, сохранить его или проанализировать содержимое
    await message.answer("Вы отправили голосовое сообщение.")

# Обработчик для аудиофайлов
@dp.message_handler(content_types=ContentType.AUDIO)
async def handle_audio_message(message: types.Message):
    audio = message.audio
    # здесь можно обработать полученный аудиофайл, например, сохранить его или проанализировать метаданные
    await message.answer("Вы отправили аудиофайл.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




