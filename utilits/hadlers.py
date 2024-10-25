from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
import utilits.keybords as keyboard

router = Router()
linkGgTable = ''
@router.message(CommandStart())
async def cmdStart (message: Message):
    await message.answer ("Бот запущен...")

@router.message(F.text == 'Синхронизировать')
async def s (message: Message):
    await message.answer ("Синхронизация прошла успешно", reply_markup=keyboard.main)

@router.message(F.text == 'Последний комментарий')
async def getLastComment (message: Message):
    await message.answer ("Гугл таблица: ...")

@router.message(F.text == 'Текущие баллы и оценка')
async def getStatistics (message: Message):
    await message.answer ("Гугл таблица: ...")

@router.message(F.text == 'Изменить таблицу')
async def changeTable (message: Message):
    await message.answer ("Гугл таблица: ...")
