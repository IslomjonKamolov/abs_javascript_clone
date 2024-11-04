from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

channel_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Obuna bo'lish", url="https://t.me/Artifex_Gravis")
        ],
           [
            InlineKeyboardButton(text="Tasdiqlash", callback_data="check_subscribed")
        ],
    ]
)