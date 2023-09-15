from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from api import *


choose_language = ReplyKeyboardMarkup(resize_keyboard=True )
choose_language.insert(KeyboardButton('🇺🇿 O\'zbekcha')).insert(KeyboardButton('🇷🇺 Русский')).insert(KeyboardButton('🇬🇧 English'))
main_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_uz.insert(KeyboardButton(text="📝 Menyu")).row(KeyboardButton(text="📖 Buyurtmalarim"), KeyboardButton(text="🛒 Savat"), KeyboardButton(text="⚙️ Sozlamalar"), KeyboardButton(text="✍️ Sharh qoldiring"))
main_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_ru.insert(KeyboardButton(text="📝 Меню")).row(KeyboardButton(text="📖 Мои заказы"), KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="✍️ Оставить отзыв"))
main_en = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_en.insert(KeyboardButton(text="📝 Menu")).row(KeyboardButton(text="📖 My orders"), KeyboardButton(text="🛒 Basket"), KeyboardButton(text="⚙️ Settings"), KeyboardButton(text="✍️ Leave a feedback"))


# GET ALL CATEGORIES
def categories(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        button.row(KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🛒 Savat"))
    elif language == 'ru':
        button.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🛒 Корзина"))
    else:
        button.row(KeyboardButton(text="⬅️ Back"), KeyboardButton(text="🛒 Basket"))
    categories = get_categories(language)
    for i in categories:
        button.insert(KeyboardButton(text=i))
    
    return button


############## Button Settings
def settings(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, )
    button.row(InlineKeyboardButton(text="🇺🇿 O'zbekcha"), InlineKeyboardButton(text="🇷🇺 Русский"), InlineKeyboardButton(text="🇬🇧 English"))
    if language == 'ru':
        # return to main menu
        button.row(InlineKeyboardButton(text="🔝 Вернуться в главное меню",))
    elif language == 'en':
        # return to main menu
        button.row(InlineKeyboardButton(text="🔝 Return to main menu",))
    else:
        button.row(InlineKeyboardButton(text="🔝 Bosh menyuga qaytish",))

    return button

############## Button Comment ##############
def cancel(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, )
    if language == 'ru':
        # cancel
        button.row(InlineKeyboardButton(text="❌ Отменить",))
    elif language == 'en':
        # cancel
        button.row(InlineKeyboardButton(text="❌ Cancel",))
    else:
        button.row(InlineKeyboardButton(text="❌ Bekor qilish",))

    return button

