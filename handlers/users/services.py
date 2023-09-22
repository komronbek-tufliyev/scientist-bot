from aiogram import types
from keyboards.default.buttons import *
from aiogram.dispatcher import FSMContext
from api import *
from states import Language
from states import Level
from aiogram.utils.callback_data import CallbackData, CallbackDataFilter
from aiogram.dispatcher.filters import Text 
from loader import dp
from aiogram.types import ContentTypes




@dp.message_handler(Text(equals=['📝 Услуги', '📝 Xizmatlar', '📝 Services']))
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
    await state.finish()







@dp.message_handler(Text(equals=['Maqola', 'Статья', 'Article']))
async def article_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'article'
    })
    if language == 'uz':
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=article_buttons(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=article_buttons(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=article_buttons(language))
    await state.finish()








@dp.message_handler(Text(equals=['DGU', 'Патент', 'Patent']))
async def patent_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'patent'
    })
    if language == 'uz':
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=patent_buttons(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=patent_buttons(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=patent_buttons(language))
    await state.finish()



@dp.message_handler(Text(equals=['OAK uchun', 'Для ОАК', 'For OAK']))
async def oak_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'oak'
    })
    if language == 'uz':
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=write_article(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=write_article(language))
    await state.finish()



@dp.message_handler(Text(equals=['Respublika konferensiya uchun', 'Для Республиканской конференции', 'For Republic conference']))
async def conference_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'conference'
    })
    if language == 'uz':
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=write_article(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=write_article(language))
    await state.finish()


@dp.message_handler(Text(equals=['Xalqaro konferensiya uchun', 'Для Международной конференции', 'For International conference']))
async def international_conference_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'international_conference'
    })
    if language == 'uz':
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=write_article(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=write_article(language))
    await state.finish()



@dp.message_handler(Text(equals=["Xalqaro ilmiy jurnal uchun", "Для Международного научного журнала", "For International scientific journal"]))
async def international_journal_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'international_journal'
    })
    if language == 'uz':
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=write_article(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=write_article(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=write_article(language))
    await state.finish()



@dp.message_handler(Text(equals=["Yozib berish", "Writing", "Написание"]))
async def writing_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'writing'
    })
    if language == 'uz':
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=status(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=status(language))
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
        await message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=status(language))
    elif language == 'en':
        await message.answer("Thank you! Your opinion is important to us!", reply_markup=status(language))
    else:
        await message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=status(language))
    await state.finish()



@dp.message_handler(Text(equals=["Tayyor maqolani chop etish", "Publishing a ready-made article", "Публикация готовой статьи"]))
async def document_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    await state.update_data({
        'language': language,
        'level': 'document'
    })
    if language == 'uz':
        await message.answer("Faylni yuklang!", reply_markup=cancel(language))
    elif language == 'en':
        await message.answer("Upload file!", reply_markup=cancel(language))
    else:
        await message.answer("Upload file(ru)!", reply_markup=cancel(language))

    await Level.document.set()

def confirm(language):
    if language == 'uz':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm"),
            types.InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel")
        )
    elif language == 'en':
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Confirm", callback_data="confirm"),
            types.InlineKeyboardButton(text="❌ Cancel", callback_data="cancel")
        )
    else:
        return types.InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm"),
            types.InlineKeyboardButton(text="❌ Отменить", callback_data="cancel")
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
        await message.answer("Do you confirm article(ru)?", reply_markup=confirm(language))

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
        await call.message.answer("✅ Article uploaded(ru)!")
    await state.finish()



















# @dp.callback_query_handler(text="confirm", state=Level.document)
# async def document_confirm(call:types.CallbackQuery, state:FSMContext):
#     language = language_info(call.from_user.id)
#     data = await state.get_data()
#     await call.message.answer_document(data['document'])
#     if language == 'uz':
#         await call.message.answer("✅ Maqola yuklandi!")
#     elif language == 'en':
#         await call.message.answer("✅ Article uploaded!")
#     else:
#         await call.message.answer("✅ Article uploaded(ru)!")
#     await state.finish()


# @dp.callback_query_handler(text="cancel", state=Level.document)
# async def document_cancel(call:types.CallbackQuery, state:FSMContext):
#     language = language_info(call.from_user.id)
#     if language == 'uz':
#         await call.message.answer("❌ Maqola yuklanmadi!")
#     elif language == 'en':
#         await call.message.answer("❌ Article not uploaded!")
#     else:
#         await call.message.answer("❌ Article not uploaded(ru)!")
#     await state.finish()
#     from loader import bot
#     await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)




