from aiogram import Bot, Dispatcher  # type: ignore
from decouple import Config, RepositoryEnv  # type: ignore
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # type: ignore


config = Config(RepositoryEnv("../.env"))
token = config("TOKEN1")
bot = Bot(token=token)
storange = MemoryStorage()
dp = Dispatcher(bot, storage=storange)
