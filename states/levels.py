from aiogram.dispatcher.filters.state import StatesGroup, State

class Level(StatesGroup):
    level = State()
    services = State()
    article = State()
    patent = State()
    journal = State()
    conference = State()
    document = State()
    confirm = State()
    comment = State()
    contact = State()
    order = State()
    order_confirm = State()
    order_cancel = State()
    file_confirm = State()
    file_cancel = State()
