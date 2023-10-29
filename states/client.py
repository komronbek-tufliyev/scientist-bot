from aiogram.dispatcher.filters.state import StatesGroup, State

class Client(StatesGroup):
    phone_number = State()
    full_name = State()
    maydon = State()
    JSHSHR = State()

class ONEID(StatesGroup):
    # ONEID details
    ONEID_password = State()
    ONEID_login = State()

class HuquqEgasi(StatesGroup):
    JSHSHR = State()
    ilmiy_darajasi = State()

class Muallif_malumotlari(StatesGroup):
    JSHSHR = State()
    ilmiy_darajasi = State()
    