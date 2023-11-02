from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

import logging

from states import Level
from keyboards.inline import basket_keyboard
from keyboards.default.buttons import *
from aiogram.types import ParseMode


from api import *

@dp.message_handler(text=["🛒 Корзина", "🛒 Savat", "🛒 Basket"])
async def show_basket(message: types.Message, state: FSMContext):
    language = language_info(message.from_user.id)
    my_basket = get_basket(message.from_user.id)
    if my_basket:
        msg = f"📦 {my_basket[0]['type']}\n\n"
        await message.answer(f"🛒 Savatingiz: ```{my_basket}```", reply_markup=basket_keyboard.basket(language), parse_mode=ParseMode.MARKDOWN)
        await Level.basket.set()
    else:
        await message.answer("🛒 Savatingiz bo'sh!", reply_markup=basket_keyboard.basket(language))
        await Level.basket.set()


@dp.callback_query_handler(basket_keyboard.basket_callback.filter(item_id="basket", action="basket"), state=Level.basket)
async def show_basket(call: types.CallbackQuery, state: FSMContext):
    language = language_info(call.from_user.id)
    my_basket = get_basket(call.from_user.id)
    if my_basket:
        await call.message.answer(f"🛒 Savatingiz: {my_basket}", reply_markup=basket_keyboard.basket(language))
        await Level.basket.set()
    else:
        await call.message.answer("🛒 Savatingiz bo'sh!", reply_markup=basket_keyboard.basket(language))
        await Level.basket.set()





@dp.callback_query_handler(basket_keyboard.basket_callback.filter(item_id="order", action="order"), state=Level.basket)
async def order(call: types.CallbackQuery, state: FSMContext):
    language = language_info(call.from_user.id)
    await call.message.answer("📦 Buyurtma berish", reply_markup=basket_keyboard.order(language))
    await Level.order.set()





@dp.callback_query_handler(basket_keyboard.basket_callback.filter(item_id="cancel", action="cancel"), state=Level.basket)   
async def cancel(call: types.CallbackQuery, state: FSMContext):
    language = language_info(call.from_user.id)
    await call.message.answer("Level basket")
    await call.message.answer("❌ Bekor qilish", reply_markup=main_uz)
    await state.reset_state()    
    await call.answer(cache_time=60) 



@dp.callback_query_handler(basket_keyboard.basket_callback.filter(item_id="cancel", action="cancel"), state=Level.order)   
async def cancel(call: types.CallbackQuery, state: FSMContext):
    language = language_info(call.from_user.id)
    await call.message.answer("Level order")


    await call.message.answer("❌ Bekor qilish", reply_markup=main_uz)
    await state.reset_state()
    # await state.reset_data()    
    # await
    # call timeout
    await call.answer(cache_time=60) 
