import csv
import re
import logging
from email.message import EmailMessage

import aiohttp
from aiogram import types, filters, F, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiosmtplib import SMTP
from pydantic import BaseModel, EmailStr

import config

router = Router()


@router.message(filters.StateFilter(None), F.text == "тест")
async def handler_text_dialogue98(message: types.Message):
    await message.answer("тест")
    await handler_command_start(message)


@router.message(filters.StateFilter(None), filters.CommandStart())
async def handler_command_start(message: types.Message):
    start_keyboard = None

    await message.answer(
        "Привет!",
        reply_markup=start_keyboard
    )