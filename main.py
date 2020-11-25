import logging
from DB import *
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1493623823:AAH_LMMeOZf54r6eD7yvXBGKIG-SQqwwY9o'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
DB = DB()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Cool_Storage_Bot!\nPowered by aiogram.")



@dp.message_handler(content_types=['file', 'photo', 'video', 'document'])
async def set_file(message: types.Message):
    # logging.INFO()
    print(12)
    try:
        tags = message.text.split()
    except AttributeError:
        tags = [" "]
    if message.document is not None:
        DB.save_file(message.document.file_id, tags)
    elif message.photo is not None:
        print(message.photo)
        # DB.save_file(message.photo.file_id, tags)
    elif message.video.file_id is not None:
        DB.save_file(message.video.file_id, tags)
    # await message.answer(message.text)


@dp.message_handler(commands=['get'])
async def get_files_by_tag_name(message: types.Message):
    tags = message.text.split()
    files = DB.get_files(tags)
    for file in files:
        bot.sendDocument(chat_id=message.sender_chat, document = file.file_id)



@dp.message_handler(commands=['delate'])
async def delate_file(message: types.Message):
    tags = message.text.split()
    files = DB.get_files(tags)
    for file in files:
        bot.sendDocument(chat_id=message.sender_chat, document = file.file_id)
    await 1


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

