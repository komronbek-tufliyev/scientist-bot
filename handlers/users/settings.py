from loader import dp, bot
from aiogram import types
from api import *
from keyboards.default.buttons import *


############  Click Settings Button ###############
@dp.message_handler(text=["⚙️ Настройки", "⚙️ Sozlamalar", "⚙️ Settings"])
async def gotosettings(message:types.Message):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("⚙️ Sozlamalar bo'limiga xush kelibsiz!\n\n"\
                             f"🇺🇿/🇷🇺/🇬🇧  Tugmachalar orqali tilni o'zgartirishingiz mumkin.", reply_markup=settings(language))

    elif language == 'en':
        await message.answer("⚙️ Welcome to settings!\n\n"\
                                f"🇺🇿/🇷🇺/🇬🇧 You can change the language using the buttons.", reply_markup=settings(language))
        
    else:
        await message.answer("⚙️ Добро пожаловать в настройки!\n\n"\
                              f"🇺🇿/🇷🇺/🇬🇧 Вы можете изменить язык с помощью кнопок.", reply_markup=settings(language))


###########  Select Language  #################
@dp.message_handler(text=["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"])
async def change_lang(message:types.Message):
    if message.text == "🇺🇿 O'zbekcha":
        change_language(telegram_id=message.from_user.id, language="uz")
        await message.answer(f"🙂 Assalomu alaykum, {message.from_user.full_name}, @new_scientist_bot botiga xush kelibsiz!\n\n"\
                             "📚 Ushbu bot orqali mahalliy va xalqaro ilmiy jurnallardan siz yozgan maqola va boshqalarni chop etishingiz, ilmiy ishingiz uchun kerakli materiallar olishingiz mumkin. Marhamat xizmatlarimizidan foydalaning!\n\n"\
                             "💻 Buyurtna berishni boshlaysizmi?", reply_markup=main_uz)
    elif message.text == "🇬🇧 English":
        change_language(telegram_id=message.from_user.id, language="en")
        await message.answer(f"🙂 Hello, {message.from_user.full_name}, welcome to @new_scientist_bot!\n\n"\
                             "📚 Through this bot, you can publish your articles and others from local and international scientific journals, and get necessary materials for your scientific work. Take advantage of our services!\n\n"\
                             "💻 Are you starting to order?", reply_markup=main_en)
    else:
        change_language(telegram_id=message.from_user.id, language="ru")
        await message.answer(
            f"🙂 Здравствуйте, {message.from_user.full_name}, добро пожаловать в бот @new_scientist_bot!\n\n"\
            "📚 С помощью этого бота вы можете публиковать свои и другие статьи из местных и международных научных журналов, а также получать необходимые материалы для своей научной работы. Воспользуйтесь нашими услугами!\n\n"
            "💻 Начать заказывать?", reply_markup=main_ru)


################  Go to Menu  ####################
@dp.message_handler(text=["🔝 Bosh menyuga qaytish", "🔝 Вернуться в главное меню", "🔝 Return to main menu"])
async def back(message:types.Message):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("✅ Bosh menyuga xush kelibsiz\n" \
                             f"💻 Maqola, jurnal yozish, mahalliy va xalqaro jurnallarda chop etish xizmatlari! Buyurtma berishni boshlaysizmi?", reply_markup=main_uz)
    elif language == 'en':
        await message.answer("✅ Welcome to the main menu\n" \
                             f"💻 Articles, magazine writing, publishing services in local and international magazines! Are you starting to order?", reply_markup=main_en)
    else:
        await message.answer("✅ Добро пожаловать в главное меню\n" \
                             f"💻 Статьи, написание журналов, издательские услуги в местных и международных журналах! Вы начинайте заказывать?", reply_markup=main_ru)


##################  Change Language Command   #################
@dp.message_handler(commands='set_language')
async def change(message:types.Message):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("⚙️ Sozlamalar bo'limiga xush kelibsiz!\n\n"
                             f"🇺🇿/🇷🇺/🇬🇧  Tugmachalar orqali tilni o'zgartirishingiz mumkin.",
                             reply_markup=settings(language))
        
    elif language == 'en':
        await message.answer("⚙️ Welcome to settings!\n\n"\
                             f"🇺🇿/🇷🇺/🇬🇧 You can change the language using the buttons.",
                             reply_markup=settings(language))

    else:
        await message.answer("⚙️ Добро пожаловать в настройки!\n\n"\
                             f"🇺🇿/🇷🇺/🇬🇧 Вы можете изменить язык с помощью кнопок.", reply_markup=settings(language))
        

# Get contact
@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def get_contact(message: types.Message):
    language = language_info(message.from_user.id)
    phone = message.contact.phone_number
    change_phone(telegram_id=message.from_user.id, phone=phone)
    
    if language == 'uz':
        await message.answer("📞 Telefon raqamingiz qabul qilindi. Tez orada siz bilan bog'lanamiz!")
    elif language == 'en':
        await message.answer("📞 Your phone number has been received. We will contact you shortly!")
    else:
        await message.answer("📞 Ваш номер телефона получен. Мы свяжемся с вами в ближайшее время!")