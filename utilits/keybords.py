from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

#start = ReplyKeyboardMarkup(keyboard = [])
main = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = 'Последний комментарий')],
                                       [KeyboardButton(text = 'Изменить таблицу')]],
                                        #[KeyboardButton(text = 'Текущие баллы и оценка')],   Maybe, maybe....
                                        resize_keyboard = True,
                                        input_field_placeholder='Выберите команду')
