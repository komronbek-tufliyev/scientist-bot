from aiogram import types
from keyboards.default.buttons import *
from aiogram.dispatcher import FSMContext
from api import *
from states import Level, Language
from aiogram.utils.callback_data import CallbackData, CallbackDataFilter
from aiogram.dispatcher.filters import Text 
from loader import dp, bot
from aiogram.types import ContentTypes




@dp.message_handler(Text(equals=['📝 Услуги', '📝 Xizmatlar', '📝 Services']), state='*')
async def services_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'services'
    })
    if language == 'uz':
        await message.answer("Xizmatlarimiz", reply_markup=services(language))
    elif language == 'en':
        await message.answer("Our services", reply_markup=services(language))
    else:
        await message.answer("Наши услуги", reply_markup=services(language))


    # await 

# @dp.message_handler(state=Level.services, )
# async def services2_handler(message: types.Message, state:FSMContext):
#     await message.answer_poll("Poll", ["1", "2", "3", "4", "5"], is_anonymous=False, type=types.PollType.REGULAR, allows_multiple_answers=True, correct_option_id=0, explanation="Explanation", explanation_parse_mode=types.ParseMode.MARKDOWN, open_period=10, close_date=10, is_closed=False, disable_notification=False, reply_to_message_id=0, reply_markup=None, timeout=None, reply=False, dont_parse_links=False, allow_sending_without_reply=False)
#     await state.finish()



@dp.message_handler(Text(equals=['Maqola', 'Статья', 'Article']))
async def article_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'article'
    })
    if language == 'uz':
        await message.answer("Maqolangizni qayerda ko'rishni xohlaysiz?!", reply_markup=article_buttons(language))
    elif language == 'en':
        await message.answer("Where would you like to see your article?!", reply_markup=article_buttons(language))
    else:
        await message.answer("Где бы вы хотели видеть свою статью?!", reply_markup=article_buttons(language))
    await state.finish()






@dp.message_handler(Text(equals=['Sertifikat', 'Сертификат', 'Certificate']))
async def certificate_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'certificate'
    })
    if language == 'uz':
        await message.answer("Bot test rejimida ishlamoqda. Iltimos, keyinroq urinib ko'ring!")
    elif language == 'en':
        await message.answer("The bot is working in test mode. Please try again later!")
    else:
        await message.answer("Бот работает в тестовом режиме. Пожалуйста, попробуйте позже!")
    await state.finish()



@dp.message_handler(Text(equals=['OAK uchun', 'Для ОАК', 'For OAK']))
async def oak_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'oak'
    })
    if language == 'uz':
        await message.answer("Quyidagilardan birini tanlang 👇", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Choose one of the following 👇", reply_markup=write_article(language))
    else:
        await message.answer("Выберите один из следующих 👇", reply_markup=write_article(language))
    await state.finish()



@dp.message_handler(Text(equals=['Respublika konferensiya uchun', 'Для Республиканской конференции', 'For Republic conference']))
async def conference_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'conference'
    })
    if language == 'uz':
        await message.answer("Quyidagilardan birini tanlang 👇", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Choose one of the following 👇", reply_markup=write_article(language))
    else:
        await message.answer("Выберите один из следующих 👇", reply_markup=write_article(language))
    await state.finish()


@dp.message_handler(Text(equals=['Xalqaro konferensiya uchun', 'Для Международной конференции', 'For International conference']))
async def international_conference_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'international_conference'
    })
    if language == 'uz':
        await message.answer("Quyidagilardan birini tanlang 👇", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Choose one of the following 👇", reply_markup=write_article(language))
    else:
        await message.answer("Выберите один из следующих 👇", reply_markup=write_article(language))
    await state.finish()



@dp.message_handler(Text(equals=["Xalqaro ilmiy jurnal uchun", "Для Международного научного журнала", "For International scientific journal"]))
async def international_journal_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'international_journal'
    })
    if language == 'uz':
        await message.answer("Quyidagilardan birini tanlang 👇", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Choose one of the following 👇", reply_markup=write_article(language))
    else:
        await message.answer("Выберите один из следующих 👇", reply_markup=write_article(language))
    await state.finish()



@dp.message_handler(Text(equals=["Yozib berish", "Writing", "Написание"]))
async def writing_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'writing'
    })
    if language == 'uz':
        await message.answer("Quyidagi sohalardan birini tanlang 👇", reply_markup=status(language))
    elif language == 'en':
        await message.answer("Choose one of the fields below 👇", reply_markup=status(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=status(language))
    await state.finish()



@dp.message_handler(Text(equals=["Yozib berish va chop etish", "Writing and publishing", "Написание и публикация"]))
async def writing_and_publishing_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'writing_and_publishing'
    })
    if language == 'uz':
        await message.answer("Quyidagi sohalardan birini tanlang 👇", reply_markup=status(language))
    elif language == 'en':
        await message.answer("Choose one of the fields below 👇", reply_markup=status(language))
    else:
        await message.answer("Choose one of the fields below 👇", reply_markup=status(language))
    await state.finish()



@dp.message_handler(Text(equals=["Tayyor maqolani chop etish", "Publishing a ready-made article", "Публикация готовой статьи"]))
async def document_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'document'
    })
    if language == 'uz':
        await message.answer("Faylni yuklang!")
    elif language == 'en':
        await message.answer("Upload file!")
    else:
        await message.answer("Загрузить файл!")

    await Level.document.set()



def confirm(language):
    if language == 'uz':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm"),
            types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor_qilish")
        )
    elif language == 'en':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Confirm", callback_data="confirm"),
            types.InlineKeyboardButton(text="❌ Cancel", callback_data="bekor_qilish")
        )
    else:
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm"),
            types.InlineKeyboardButton(text="❌ Отменить", callback_data="bekor_qilish")
        )
    

@dp.message_handler(state=Level.document, content_types=types.ContentType.DOCUMENT)
async def document_get(message:types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'document': message.document.file_id
    })
    # send "confirm button"
    if language == 'uz':
        await message.answer("Maqolani tasdiqlaysizmi?", reply_markup=confirm(language))
    elif language == 'en':
        await message.answer("Do you confirm article?", reply_markup=confirm(language))
    else:
        await message.answer("Вы подтверждаете статью?", reply_markup=confirm(language))

    await Level.confirm.set()



@dp.callback_query_handler(text="confirm", state=Level.confirm)
async def document_confirm(call:types.CallbackQuery, state:FSMContext):
    language = language_info(call.from_user.id)
    data = await state.get_data()
    await call.message.answer_document(data['document'])
    if language == 'uz':
        await call.message.answer("✅ Maqola yuklandi!")
    elif language == 'en':
        await call.message.answer("✅ Article uploaded!")
    else:
        await call.message.answer("✅ Статья загружена!")
    await state.finish()


@dp.callback_query_handler(text="cancel", state=Level.confirm)
async def document_cancel(call:types.CallbackQuery, state:FSMContext):
    language = language_info(call.from_user.id)
    if language == 'uz':
        await call.message.answer("❌ Maqola yuklanmadi!")
    elif language == 'en':
        await call.message.answer("❌ Article not uploaded!")
    else:
        await call.message.answer("❌ Статья не загружена!")
    await state.finish()



##################### Texnika uchun shartnoma #####################

@dp.message_handler(Text(equals=["Texnika", "Техника", "Technique"]))
async def technique_handler(message: types.Message, state: FSMContext):
    agreement_path = "Share Data.pdf"
    with open(agreement_path, 'rb') as agreement_file:
        await bot.send_document(message.chat.id, agreement_file)
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language
    })
    if language == 'uz':
        await message.answer("Shartnomani o'qib chiqib, rozilik bildiring:", reply_markup=Tasdiqlash(language))
    elif language == 'en':
        await message.answer("Read the agreement and give your consent:", reply_markup=Tasdiqlash(language))
    else:
        await message.answer("Прочитайте соглашение и дайте свое согласие:", reply_markup=Tasdiqlash(language))

    
def Tasdiqlash(language):
    if language == 'uz':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Roziman", callback_data="tasdiqlash"),
            types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor_qilish")
        )
    elif language == 'en':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ I agree", callback_data="tasdiqlash"),
            types.InlineKeyboardButton(text="❌ Cancel", callback_data="bekor_qilish")
        )
    else:
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Подтвердить", callback_data="tasdiqlash"),
            types.InlineKeyboardButton(text="❌ Отменить", callback_data="bekor_qilish")
        )


@dp.callback_query_handler(text="tasdiqlash")
async def agreement_accepted(call: types.CallbackQuery, state: FSMContext):
    language = language_info(call.from_user.id)
    # delete last message 
    await call.message.delete()
    if language == 'uz':
        await call.message.answer("✅ Shartnoma tasdiqlandi!")
    elif language == 'en':
        await call.message.answer("✅ Agreement confirmed!")
    else:
        await call.message.answer("✅ Соглашение подтверждено!")
    await state.finish()


@dp.callback_query_handler(text="bekor_qilish")
async def agreement_cancelled(call: types.CallbackQuery, state: FSMContext):
    language = language_info(call.from_user.id)
    await call.message.delete()
    if language == 'uz':
        await call.message.answer("❌ Shartnoma bekor qilindi!")
    elif language == 'en':
        await call.message.answer("❌ Agreement cancelled!")
    else:
        await call.message.answer("❌ Соглашение отменено!")
    await state.finish()





##################### Pedagogika uchun shartnoma #####################

@dp.message_handler(Text(equals=["Pedagogika", "Педагогика", "Pedagogy"]))
async def pedagogy_handler(message: types.Message, state:FSMContext):
    agreement_path = "Share Data.pdf"
    with open(agreement_path, 'rb') as agreement_file:
        await bot.send_document(message.chat.id, agreement_file)
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language
    })

    if language == 'uz':
        await message.answer("Shartnomani o'qib chiqib, rozilik bildiring:", reply_markup=Tasdiqlash(language))
    elif language == 'en':
        await message.answer("Read the agreement and give your consent:", reply_markup=Tasdiqlash(language))
    else:
        await message.answer("Прочитайте соглашение и дайте свое согласие:", reply_markup=Tasdiqlash(language))


# "Tushundim" degan buttonni yaratish
def Tasdiqlash(language):
    if language == 'uz':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Roziman", callback_data="tasdiqlash"),
            types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor_qilish")
        )
    elif language == 'en':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ I agree", callback_data="tasdiqlash"),
            types.InlineKeyboardButton(text="❌ Cancel", callback_data="bekor_qilish")
        )
    else:
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Подтвердить", callback_data="tasdiqlash"),
            types.InlineKeyboardButton(text="❌ Отменить", callback_data="bekor_qilish")
        )
        


@dp.callback_query_handler(text="tasdiqlash", state=Level.pedagogy)
async def agreement_accepted(call: types.CallbackQuery, state=FSMContext):
    language = language_info(call.from_user.id)
    if language == 'uz':
        await call.message.answer("✅ Shartnoma tasdiqlandi!")
    elif language == 'en':
        await call.message.answer("✅ Agreement confirmed!")
    else:
        await call.message.answer("✅ Соглашение подтверждено!")
    await state.finish()


@dp.callback_query_handler(text="bekor_qilish", state=Level.pedagogy)
async def agreement_cancelled(call: types.CallbackQuery, state=FSMContext):
    language = language_info(call.from_user.id)
    if language == 'uz':
        await call.message.answer("❌ Shartnoma bekor qilindi!")
    elif language == 'en':
        await call.message.answer("❌ Agreement cancelled!")
    else:
        await call.message.answer("❌ Соглашение отменено!")
    await state.finish()




######################## Iqtisodiyot uchun shartnoma #####################

@dp.message_handler(Text(equals=["Iqtisodiyot", "Экономика", "Economy"]))
async def economy_handler(message: types.Message, state:FSMContext):
    agreement_path = "Share Data.pdf"
    with open(agreement_path, 'rb') as agreement_file:
        await bot.send_document(message.chat.id, agreement_file)
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language
    })
    # "Tushundim" degan buttonni yaratish
    def Tasdiqlash(language):
        if language == 'uz':
            return types.InlineKeyboardMarkup(row_width=2).add(
                types.InlineKeyboardButton(text="✅ Roziman", callback_data="tasdiqlash"),
                types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor_qilish")
            )
        elif language == 'en':
            return types.InlineKeyboardMarkup(row_width=2).add(
                types.InlineKeyboardButton(text="✅ I agree", callback_data="tasdiqlash"),
                types.InlineKeyboardButton(text="❌ Cancel", callback_data="bekor_qilish")
            )
        else:
            return types.InlineKeyboardMarkup(row_width=2).add(
                types.InlineKeyboardButton(text="✅ Подтвердить", callback_data="tasdiqlash"),
                types.InlineKeyboardButton(text="❌ Отменить", callback_data="bekor_qilish")
            )
    shart = Tasdiqlash(language)

    if language == 'uz':
        await message.answer("Shartnomani o'qib chiqib, rozilik bildiring:", reply_markup=shart)
    elif language == 'en':
        await message.answer("Read the agreement and give your consent:", reply_markup=shart)
    else:
        await message.answer("Прочитайте соглашение и дайте свое согласие:", reply_markup=shart)


@dp.callback_query_handler(text="tasdiqlash", state=Level.economy)
async def agreement_accepted(call: types.CallbackQuery, state=FSMContext):
    language = language_info(call.from_user.id)
    data = await state.get_data()
    if language == 'uz':
        await call.message.answer("✅ Shartnoma tasdiqlandi!")
    elif language == 'en':
        await call.message.answer("✅ Agreement confirmed!")
    else:
        await call.message.answer("✅ Соглашение подтверждено!")
    await state.finish()



############################# Tibbiyot uchun shartnoma #############################

@dp.message_handler(Text(equals=["Tibbiyot", "Медицина", "Medicine"]))
async def medicine_handler(message: types.Message, state:FSMContext):
    agreement_path = "Share Data.pdf"
    with open(agreement_path, 'rb') as agreement_file:
        await bot.send_document(message.chat.id, agreement_file)
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language
    })
    # "Tushundim" degan buttonni yaratish
    def Tasdiqlash(language):
        if language == 'uz':
            return types.InlineKeyboardMarkup(row_width=2).add(
                types.InlineKeyboardButton(text="✅ Roziman", callback_data="tasdiqlash"),
                types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="bekor_qilish")
            )
        elif language == 'en':
            return types.InlineKeyboardMarkup(row_width=2).add(
                types.InlineKeyboardButton(text="✅ I agree", callback_data="tasdiqlash"),
                types.InlineKeyboardButton(text="❌ Cancel", callback_data="bekor_qilish")
            )
        else:
            return types.InlineKeyboardMarkup(row_width=2).add(
                types.InlineKeyboardButton(text="✅ Подтвердить", callback_data="tasdiqlash"),
                types.InlineKeyboardButton(text="❌ Отменить", callback_data="bekor_qilish")
            )
    shart = Tasdiqlash(language)

    if language == 'uz':
        await message.answer("Shartnomani o'qib chiqib, rozilik bildiring:", reply_markup=shart)
    elif language == 'en':
        await message.answer("Read the agreement and give your consent:", reply_markup=shart)
    else:
        await message.answer("Прочитайте соглашение и дайте свое согласие:", reply_markup=shart)

    await Level.medicine.set()


@dp.callback_query_handler(text="tasdiqlash", state=Level.medicine)
async def agreement_accepted(call: types.CallbackQuery, state:FSMContext):
    language = language_info(call.from_user.id)
    if language == 'uz':
        await call.message.answer("✅ Shartnoma tasdiqlandi!\n\nEndi quyidagi formalarni to'ldiring iltimos!" )
    elif language == 'en':
        await call.message.answer("✅ Agreement confirmed!\n\nNow fill out the following forms please!")
    else:
        await call.message.answer("✅ Соглашение подтверждено!\n\nТеперь заполните следующие формы пожалуйста!")

    await Level.authors.set()



############################# Maqola mualliflari #############################

@dp.message_handler(state=Level.authors)
async def authors_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language
    })
    if language == 'uz':
        await message.answer("Maqola mualliflarini kiriting:")
    elif language == 'en':
        await message.answer("Enter the authors of the article:")
    else:
        await message.answer("Введите авторов статьи:")

    await Level.article_name.set()


@dp.message_handler(state=Level.article_name)
async def authors_get(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'authors': message.text
    })
    if language == 'uz':
        await message.answer("Maqola nomini kiriting:")
    elif language == 'en':
        await message.answer("Enter the name of the article:")
    else:
        await message.answer("Введите название статьи:")

    await state.finish()







