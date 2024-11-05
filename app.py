import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from config import TOKEN
from functions import is_subscribed
from keyboard import channel_list

dp = Dispatcher()
bot = Bot(token=TOKEN)
router = Router()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    check = await is_subscribed(user_id=message.from_user.id, bot=bot)
    if not check:
        await message.answer(
            "Bot dan foydalanish uchun , iltimos kanalga obuna bo'lganizni tekshirib ko'ring",
            reply_markup=channel_list,
        )
        return
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}!")
    await message.answer("https://t.me/+l7_uD-Nwuvc1ZmZi")


@router.callback_query(F.data == "check_subscribed")
async def check_subscription(callback_query: CallbackQuery):
    check = await is_subscribed(user_id=callback_query.from_user.id, bot=bot)
    print(check)
    await callback_query.message.delete()
    if check:
        await callback_query.message.answer(
            f"Assalomu aleykum, {callback_query.from_user.full_name}!"
        )
        await callback_query.message.answer("https://t.me/+l7_uD-Nwuvc1ZmZi")
    else:
        await callback_query.message.answer(
            "Bot dan foydalanish uchun , iltimos kanalga obuna bo'lganizni tekshirib ko'ring.", reply_markup=channel_list
        )
    await callback_query.answer()


@dp.message()
async def echo_handler(message: Message) -> None:
    await message.answer(message.text)


dp.include_router(router)

if __name__ == "__main__":
    dp.run_polling(bot)
