import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
from handlers.catalog import router

BOT_TOKEN = '7185256751:AAFhofLs-HWoSQ-RndN1AeEUNcE--p5N-3g'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Hello!\n" "<b>Urban Lang Club - специализированная школа, обучающая разговорным языкам по кембриджской методике. Школа ULC - одна из немногих в Минске, которая гарантирует результат по договору: либо Вы повышаете уровень языка за курс, либо проходите повторное обучение за счет школы (бесплатно).</b>!",
        parse_mode=ParseMode.HTML)
    await message.answer("Желаете ли вы записаться на пробное занятие?😊 /da или /not")

@router.message(Command("da"))
async def da(message: types.Message):
    await message.answer('Отлично!\n' 'Выберите язык для изучения: /language')

@router.message(Command("not"))
async def da(message: types.Message):
    await message.answer('До новых встреч!😊')

@router.message(Command("language"))
async def language(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Английский", callback_data="v_1"))
    builder.add(types.InlineKeyboardButton(text="Китайский", callback_data="v_2"))
    builder.add(types.InlineKeyboardButton(text="Немецкий", callback_data="v_3"))
    builder.add(types.InlineKeyboardButton(text="Итальянский", callback_data="v_4"))
    await message.answer('Выбери и нажми на одну из кнопок!', reply_markup=builder.as_markup())

@router.callback_query(F.data)
async def x_random_value(callback: types.CallbackQuery):
    data = callback.data.split('_')[1]
    if data == '1': return await callback.message.answer(
        'Отлично! Вы выбрали английский язык для изучения! Для записи на пробное занятие напишите команду: /english и введите свой номер телефона.')
    if data == '2': return await callback.message.answer(
        'Отлично! Вы выбрали китайский язык для изучения! Для записи на пробное занятие напишите команду: /chinese и введите свой номер телефона.')
    if data == '3': return await callback.message.answer(
        'Отлично! Вы выбрали немецкий язык для изучения! Для записи на пробное занятие напишите команду: /german и введите свой номер телефона.')
    if data == '4': return await callback.message.answer(
        'Отлично! Вы выбрали немецкий язык для изучения! Для записи на пробное занятие напишите команду: /italian и введите свой номер телефона.')

@router.message(Command("english"))
async def cmd_set(message: types.Message, command):
    if command.args is None:
        await message.answer("Вот правильный пример записи:/english +97564532622")
        return
    await message.answer("Вы записаны на пробное занятие! До встречи!🤗")

@router.message(Command("chinese"))
async def cmd_set(message: types.Message, command):
    if command.args is None:
        await message.answer("Вот правильный пример записи:/chinese +57685847373")
        return
    await message.answer("Вы записаны на пробное занятие! До встречи!🤗")

@router.message(Command("german"))
async def cmd_set(message: types.Message, command):
    if command.args is None:
        await message.answer("Вот правильный пример записи:/german +675849393")
        return
    await message.answer("Вы записаны на пробное занятие! До встречи!🤗")

@router.message(Command("italian"))
async def cmd_set(message: types.Message, command):
    if command.args is None:
        await message.answer("Вот правильный пример записи:/italian +843658765")
        return
    await message.answer("Вы записаны на пробное занятие! До встречи!🤗")

@router.message()
async def cmd_v(message: types.Message):
    await message.reply("посмотри как нужно написать!")

if __name__ == "main":
    asyncio.run(main())