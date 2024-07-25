from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def link_bt():
    """func create buttons"""
    inline_kb_list = [
        [InlineKeyboardButton(text="Company", url='https://journal.tinkoff.ru/guide/bluechips/')],
        [InlineKeyboardButton(text="Currency", url='https://journal.tinkoff.ru/news/what-ruble-depend-on/')],
        [InlineKeyboardButton(text="Main information",
                              url="https://www.tinkoff.ru/invest/help/educate/how-it-works/what-is"
                                  "-exchange/how-it-works/")],
        [InlineKeyboardButton(text="Indexes", url='https://ru.investing.com/indices/russia-indices')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
