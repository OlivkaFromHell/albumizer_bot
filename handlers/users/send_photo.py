from aiogram.types import ContentType, Message, InputFile

from loader import dp
from utils.imgproc import make_cover


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo_id(message: Message):
    if message.photo[-1].width != message.photo[-1].height:
        await message.reply(text='Я работаю только с квадратным соотношением сторон\n'
                                 'Сделать изображение квадратным можно сразу в Телеграме')
    elif message.photo[-1].width == message.photo[-1].height:
        await message.photo[-1].download(destination_file=
                                         '/home/albumizer_bot/data/images/photo.jpg')
        await make_cover()
        cover = InputFile('/home/albumizer_bot/data/images/cover.jpg')
        await message.reply_photo(photo=cover)
