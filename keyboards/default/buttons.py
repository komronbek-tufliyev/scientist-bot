from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from api import *
from data.config import ADMINS


# Language buttons
choose_language = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
choose_language.insert(KeyboardButton('🇺🇿 O\'zbekcha')).insert(KeyboardButton('🇷🇺 Русский')).insert(KeyboardButton('🇬🇧 English'))

# Main menu buttons
main_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_uz.insert(KeyboardButton(text="📝 Xizmatlar")).row(KeyboardButton(text="🛒 Savat"), KeyboardButton(text="⚙️ Sozlamalar")).insert(KeyboardButton(text="✍️ Aloqa"))
main_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_ru.insert(KeyboardButton(text="📝 Услуги")).row(KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="⚙️ Настройки")).insert(KeyboardButton(text="✍️ Контакт"))
main_en = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_en.insert(KeyboardButton(text="📝 Services")).row(KeyboardButton(text="🛒 Basket"), KeyboardButton(text="⚙️ Settings")).insert(KeyboardButton(text="✍️ Contact"))


# Callback data

# Callback data for services button
services_callback = CallbackData('services', 'action', 'data')

# Callback data for articles button
article_callback = CallbackData('article', 'data')

# Callback data for patents button
patent_callback = CallbackData('patent', 'data')




# GET ALL CATEGORIES
def categories(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        button.row(KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🛒 Savat"))
    elif language == 'ru':
        button.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🛒 Корзина"))
    else:
        button.row(KeyboardButton(text="⬅️ Back"), KeyboardButton(text="🛒 Basket"))
    # # categories = get_categories(language)
    # for i in categories:
    #     button.insert(KeyboardButton(text=i))
    
    return button


############## Button Settings
def settings(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button.row(InlineKeyboardButton(text="🇺🇿 O'zbekcha"), InlineKeyboardButton(text="🇷🇺 Русский"), InlineKeyboardButton(text="🇬🇧 English"))
    if language == 'uz':
        # return to main menu
        button.insert(InlineKeyboardButton(text="🔝 Bosh menyuga qaytish")).insert(KeyboardButton(text="Kontaktni ulashish", request_contact=True),)
    elif language == 'en':
        # return to main menu
        button.row(InlineKeyboardButton(text="🔝 Return to main menu")).add(KeyboardButton(text="Share contact", request_contact=True),)
    else:
        button.row(InlineKeyboardButton(text="🔝 Вернуться в главное меню",)).add(KeyboardButton(text="Поделиться контактом", request_contact=True),)

    return button

############## Button Comment ##############
def cancel(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        # cancel
        button.row(InlineKeyboardButton(text="❌ Bekor qilish",))
    elif language == 'en':
        # cancel
        button.row(InlineKeyboardButton(text="❌ Cancel",))
    else:
        button.row(InlineKeyboardButton(text="❌ Отменить",))

    return button

services_callback = CallbackData('services', 'action', 'data')

def services(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        button.add(
            InlineKeyboardButton('Maqola', callback_data=services_callback.new(data='article', action='article'))).add( 
            InlineKeyboardButton('DGU', callback_data=services_callback.new(data='patent', action='patent'))).add( 
            InlineKeyboardButton('Sertifikat', callback_data=services_callback.new(data='certificate', action='certificate'))).add( 
            # InlineKeyboardButton(text="🔝 Bosh menyuga qaytish"),
            InlineKeyboardButton(text="⬅️ Orqaga")
            )
    elif language == 'en':
        button.add(
            InlineKeyboardButton('Article', callback_data=services_callback.new(data='article', action='article')), 
            InlineKeyboardButton('Patent', callback_data=services_callback.new(data='patent', action='patent')), 
            InlineKeyboardButton('Certificate', callback_data=services_callback.new(data='certificate', action='certificate')), 
            # InlineKeyboardButton(text="🔝 Return to main menu",),
            InlineKeyboardButton(text="⬅️ Back")
        )
    else:
        button.add(
            InlineKeyboardButton('Статья', callback_data=services_callback.new(data='article', action='article')), 
            InlineKeyboardButton('Патент', callback_data=services_callback.new(data='patent', action='patent')), 
            InlineKeyboardButton('Сертификат', callback_data=services_callback.new(data='certificate', action='certificate')), 
            # InlineKeyboardButton(text="🔝 Вернуться в главное меню",),
            InlineKeyboardButton(text="⬅️ Назад")
        )

    # print(button)
    return button


def article_buttons(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if language == 'uz':
        button.add(
            InlineKeyboardButton('OAK uchun', callback_data=article_callback.new(data='oak')), 
            InlineKeyboardButton('Respublika konferensiya uchun', callback_data=article_callback.new(data='conference')),
            InlineKeyboardButton('Xalqaro konferensiya uchun', callback_data=article_callback.new(data='international_conference')),
            InlineKeyboardButton("Xalqaro ilmiy jurnal uchun", callback_data=article_callback.new(data='international_journal')),
            # InlineKeyboardButton('🔝 Bosh menyuga qaytish'),
            InlineKeyboardButton('⬅️ Orqaga')
        )
    elif language == 'en':
        button.add(
            InlineKeyboardButton('For OAK', callback_data='oak'), 
            InlineKeyboardButton('For Republic conference', callback_data=article_callback.new(data='conference')),
            InlineKeyboardButton('For International conference', callback_data=article_callback.new(data='international_conference')),
            InlineKeyboardButton("For International scientific journal", callback_data=article_callback.new(data='international_journal')),
            # InlineKeyboardButton('🔝 Return to main menu'),
            InlineKeyboardButton('⬅️ Back')
        )
    else:
        button.add(
            InlineKeyboardButton('Для ОАК', callback_data='oak'), 
            InlineKeyboardButton('Для Республиканской конференции', callback_data=article_callback.new(data='conference')),
            InlineKeyboardButton('Для Международной конференции', callback_data=article_callback.new(data='international_conference')),
            InlineKeyboardButton("Для Международного научного журнала", callback_data=article_callback.new(data='international_journal')),
            # InlineKeyboardButton('🔝 Вернуться в главное меню'),
            InlineKeyboardButton('⬅️ Назад')
        )
    
    
    return button



def write_article(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if language == 'uz':
        button.add(
            InlineKeyboardButton('Yozib berish', callback_data='yozish'),
            InlineKeyboardButton('Yozib berish va chop etish', call_back_data='yozish_chop'),
            InlineKeyboardButton('Tayyor maqolani chop etish', call_back_data='chop_etish'),
            # InlineKeyboardButton('🔝 Bosh menyuga qaytish'),
            InlineKeyboardButton('⬅️ Orqaga')
        )
    elif language == 'en':
        button.add(
            InlineKeyboardButton('Writing', callback_data='yozish'),
            InlineKeyboardButton('Writing and publishing', call_back_data='yozish_chop'),
            InlineKeyboardButton('Publishing a ready-made article', call_back_data='chop_etish'),
            # InlineKeyboardButton('🔝 Return to main menu'),
            InlineKeyboardButton('⬅️ Back')
        )
    else:
        button.add(
            InlineKeyboardButton('Написание', callback_data='yozish'),
            InlineKeyboardButton('Написание и публикация', call_back_data='yozish_chop'),
            InlineKeyboardButton('Публикация готовой статьи', call_back_data='chop_etish'),
            # InlineKeyboardButton('🔝 Вернуться в главное меню'),
            InlineKeyboardButton('⬅️ Назад')
        )

    return button



def status(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if language == 'uz':
        button.add(
            InlineKeyboardButton('Texnika', callback_data='texnika'),
            InlineKeyboardButton('Pedagogika', callback_data='pedagogika'),
            InlineKeyboardButton('Iqtisodiyot', callback_data='iqtisod'),
            InlineKeyboardButton('Tibbiyot', callback_data='tibbiyot'),
            # InlineKeyboardButton('🔝 Bosh menyuga qaytish'),
            InlineKeyboardButton('⬅️ Orqaga')
        )
    elif language == 'en':
        button.add(
            InlineKeyboardButton('Technology', callback_data='texnika'),
            InlineKeyboardButton('Pedagogy', callback_data='pedagogika'),
            InlineKeyboardButton('Economics', callback_data='iqtisod'),
            InlineKeyboardButton('Medicine', callback_data='tibbiyot'),
            # InlineKeyboardButton('🔝 Return to main menu'),
            InlineKeyboardButton('⬅️ Back')
        )
    else:
        button.add(
            InlineKeyboardButton('Техника', callback_data='texnika'),
            InlineKeyboardButton('Педагогика', callback_data='pedagogika'),
            InlineKeyboardButton('Экономика', callback_data='iqtisod'),
            InlineKeyboardButton('Медицина', callback_data='tibbiyot'),
            # InlineKeyboardButton('🔝 Вернуться в главное меню'),
            InlineKeyboardButton('⬅️ Назад')
        )
    return button
    




def share_contact(language):
    button = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if language == 'uz':
        button.add(
            KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True),
            KeyboardButton(text="⬅️ Orqaga")
        )
    elif language == 'en':
        button.add(
            KeyboardButton(text="📞 Send phone number", request_contact=True),
            KeyboardButton(text="⬅️ Back")
        )
    else:
        button.add(
            KeyboardButton(text="📞 Отправить номер телефона", request_contact=True),
            KeyboardButton(text="⬅️ Назад")
        )

    return button




