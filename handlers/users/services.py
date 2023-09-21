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



@dp.message_handler(Text(equals=["Tayyor maqolani chop etish", "Publishing a ready-made article", "Публикация готовой статьи"]), content_types=ContentTypes.DOCUMENT)




@dp.callback_query_handler(lambda c: c.data and c.data.startswith('services'))
async def services_callback_handler(call: types.CallbackQuery):
    data = services_callback.parse(call.data)
    language = language_info(call.from_user.id)
    
    # Handle the data accordingly based on 'data' and 'action'
    if data['action'] == 'article':
        await call.message.answer("Handle article action", reply_markup=services(language))
    elif data['action'] == 'patent':
        await call.message.answer("Handle patent action", reply_markup=services(language))
    elif data['action'] == 'certificate':
        await call.message.answer("Handle certificate action", reply_markup=services(language))

    await call.answer()



@dp.callback_query_handler(lambda c: c.data)
async def article_callback_handler(call: types.CallbackQuery):
    language = language_info(call.from_user.id)
    
    # Handle article action
    await call.message.answer("Handle article action", reply_markup=article_buttons(language))
    await call.answer()


@dp.callback_query_handler(lambda c: c.data and c.data == 'patent')
async def patent_callback_handler(call: types.CallbackQuery):
    language = language_info(call.from_user.id)
    
    # Handle patent action
    await call.message.answer("Handle patent action", reply_markup=patent_buttons(language))
    await call.answer()




@dp.callback_query_handler(lambda c: c.data == 'services')
async def callback_inline(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    print(call.data)
    if call.data == 'services':
        language = language_info(call.from_user.id)
        await call.message.answer("Xizmatlarimiz", reply_markup=services(language))

@dp.callback_query_handler(lambda c: c.data == 'article')
async def callback_inline2(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    print(call.data)
    if call.data == 'services':
        language = language_info(call.from_user.id)
        await call.message.answer("Xizmatlarimiz", reply_markup=services(language))




# @dp.callback_query_handler(lambda c: c.data == 'article_buttons')
# async def callback_inline3(call: types.CallbackQuery):
#     await call.answer(cache_time=60)
#     print(call.data)
#     if call.data == 'article_buttons':
#         language = language_info(call.from_user.id)
#         await call.message.answer("Xizmatlarimiz", reply_markup=article_buttons(language))







@dp.callback_query_handler(text=['services'])
async def article_handler(call: types.CallbackQuery, callback_data: dict):
    language = language_info(call.from_user.id)
    # call.data = callback_data
    print("CALL DATA: ", call.data)
    print("CALLback DATA: ", callback_data)
    # await state.update_data({
    #     'language': language,
    #     'level': 'article'
    # })

    if language == 'uz':
        await call.message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=article_buttons(language))
    elif language == 'en':
        await call.message.answer("Thank you! Your opinion is important to us!", reply_markup=article_buttons(language))
    else:
        await call.message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=article_buttons(language))
    await call.answer()






@dp.callback_query_handler(text='article')
async def patent_handler(call: types.CallbackQuery, callback_data: dict):
    language = language_info(call.from_user.id)
    
    # await state.update_data({
    #     'language': language,
    #     'level': 'patent'
    # })

    if language == 'uz':
        await call.message.answer("Rahmat! Sizning fikringiz biz uchun muhim!", reply_markup=patent_buttons(language))
    elif language == 'en':
        await call.message.answer("Thank you! Your opinion is important to us!", reply_markup=patent_buttons(language))
    else:
        await call.message.answer("Спасибо! Ваше мнение важно для нас!", reply_markup=patent_buttons(language))
    await call.answer()


