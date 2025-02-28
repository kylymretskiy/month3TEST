from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)

ADMINS = [691406306]
STAFF = [691406306, ]

storage = MemoryStorage()
database = Database("database.sqlite3")
dp = Dispatcher(bot , storage=storage)
