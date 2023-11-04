from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def client_phone(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add(KeyboardButton("Telefon raqamni ulashish 📞", request_contact=True), KeyboardButton("❌ Bekor qilish"))
    elif language == 'en':
        button.add(KeyboardButton("Share your phone 📞", request_contact=True), KeyboardButton("❌ Cancel"))
    else:
        button.add(KeyboardButton("Share your phone 📞", request_contact=True), KeyboardButton("❌ Cancel"))
    
    return button


def client_full_name(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add()
    elif language == 'en':
        button.add()
    else:
        button.add()
    return button

def client_maydon(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add()
    elif language == 'en':
        button.add()
    else:
        button.add()
    return button

def client_JSHSHR(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    if language == 'uz':
        button.add()
    elif language == 'en':
        button.add()
    else:
        button.add()
    return button

