from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Text
from keyboards.default.patent_buttons import *


from loader import dp
from api import *
from states.client import *

@dp.message_handler(Text(equals=['DGU', 'Патент', 'Patent']))
async def patent_handler(message: types.Message, state:FSMContext):
    language = language_info(message.from_user.id)
    if language == 'uz':
        await message.answer("Shartnomani o'qib tanishib chiqing")
    elif language == 'en':
        await message.answer("Shartnomani o'qib tanishib chiqing")
    else:
        await message.answer("Shartnomani o'qib tanishib chiqing")
    # await state.finish()

    await state.update_data(
        {'level': 'patent'}
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
    await state.set_state(Client.first)

@dp.message_handler(state=Client.phone_number)
async def phone_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    msg = "Telefon raqamingizni yuboring!" if language == 'uz' else ("Share phone number" if language =='en' else "Share phone number ru")
    await message.answer(f"{msg}", reply_markup=client_phone(language))
    await state.set_state(Client.full_name)

@dp.message_handler(state=Client.full_name)
async def full_name_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    msg  = "Ism Familiyangizni yozing" if language=='uz' else "Your full name" 
    await message.answer(f"{msg}", reply_markup=client_full_name(language))
    await state.set_state(Client.maydon)

@dp.message_handler(state=Client.maydon)
async def full_name_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    msg  = "Nimanidir yozing" if language=='uz' else "Your full name" 
    await message.answer(f"{msg}", reply_markup=client_maydon(language))
    await state.set_state(Client.JSHSHR)

@dp.message_handler(state=Client.maydon)
async def full_name_handler(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    msg  = "Nimanidir yozing" if language=='uz' else "Your full name" 
    await message.answer(f"{msg}", reply_markup=client_JSHSHR(language))
    await state.finish()



     



