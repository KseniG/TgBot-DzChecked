import asyncio
from aiogram import Bot, Dispatcher
from utilits.hadlers import router
import utilits.parser as parser

token = '7726626930:AAGplpCMsTPSGvBcBj0ulMsRvCt0s-ODe_Q'

async def main():
    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

async def setGgTable():
    print('Отправьте ссылку таблицы')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен...')

    """while True:
        newComment = parser.parsing
        if (newComment != lastComment):
            print(newComment)
            lastComment = newComment"""

# В чём суть и что надо
# 1)БД с комментами пользователей и их номером в таблице
#   Для этого подключается mongo (посмотреть видосы)
# 2)Парсинг гугл таблицы
#   Ещё раз посмотреть про гугл клауд и
# 3)  !!! узнать, как писать переодические функции (одна из habr статей упоминула о сущ-ии этих ф-ций)
# 4)Понять, в какие файлы раскидать весь функционал, приведённый выше
# 5)Разобраться с хостингом (+- понятно, только ? с подгрузкой) P.S Дойти бы до 5го шага
#
