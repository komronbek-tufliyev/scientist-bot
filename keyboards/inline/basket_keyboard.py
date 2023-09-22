from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData


basket_callback = CallbackData("basket", "item_id", "action")

def basket(language):
    markup = InlineKeyboardMarkup(row_width=2)
    if language == 'uz':
        markup.insert(InlineKeyboardButton("🛒 Savat", callback_data=basket_callback.new(item_id="basket", action="basket")))
        markup.insert(InlineKeyboardButton("📦 Buyurtma berish", callback_data=basket_callback.new(item_id="order", action="order")))
        markup.insert(InlineKeyboardButton("❌ Bekor qilish", callback_data=basket_callback.new(item_id="cancel", action="cancel")))
    elif language == 'en':
        markup.insert(InlineKeyboardButton("🛒 Basket", callback_data=basket_callback.new(item_id="basket", action="basket")))
        markup.insert(InlineKeyboardButton("📦 Order", callback_data=basket_callback.new(item_id="order", action="order")))
        markup.insert(InlineKeyboardButton("❌ Cancel", callback_data=basket_callback.new(item_id="cancel", action="cancel")))
    else:
        markup.insert(InlineKeyboardButton("🛒 Корзина", callback_data=basket_callback.new(item_id="basket", action="basket")))
        markup.insert(InlineKeyboardButton("📦 Заказ", callback_data=basket_callback.new(item_id="order", action="order")))
        markup.insert(InlineKeyboardButton("❌ Отменить", callback_data=basket_callback.new(item_id="cancel", action="cancel")))
    return markup


def order(language):
    markup = InlineKeyboardMarkup(row_width=2)
    if language == 'uz':
        markup.insert(InlineKeyboardButton("📦 Buyurtma berish", callback_data=basket_callback.new(item_id="order", action="order")))
        markup.insert(InlineKeyboardButton("❌ Bekor qilish", callback_data=basket_callback.new(item_id="cancel", action="cancel")))
    elif language == 'en':
        markup.insert(InlineKeyboardButton("📦 Order", callback_data=basket_callback.new(item_id="order", action="order")))
        markup.insert(InlineKeyboardButton("❌ Cancel", callback_data=basket_callback.new(item_id="cancel", action="cancel")))
    else:
        markup.insert(InlineKeyboardButton("📦 Заказ", callback_data=basket_callback.new(item_id="order", action="order")))
        markup.insert(InlineKeyboardButton("❌ Отменить", callback_data=basket_callback.new(item_id="cancel", action="cancel")))
    return markup

