from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("📅 Записаться на мастер-класс"))
    kb.add(KeyboardButton("📄 Посмотреть свои записи"))
    kb.add(KeyboardButton("ℹ️ О мастер-классах"), KeyboardButton("❌ Отменить запись"))
    return kb