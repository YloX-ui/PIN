from aiogram import Router
from aiogram.filters import Command 
from aiogram.types import Message,FSInputFile
from .inline_booton import main_key


# Создаем роутер
router = Router()

@router.message(Command('start'))
async def start_command(msg: Message):
    ph = FSInputFile('images\photo_2026-05-30_08-22-40.jpg')
    await msg.answer_photo(
        photo=ph,
        caption="💎 (name VPN)\n\nВыбери действие:",
        reply_markup=main_key,
    )