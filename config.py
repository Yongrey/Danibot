import os
from pytz import timezone
from datetime import date
from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from dotenv import load_dotenv
import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

load_dotenv()
scheduler = AsyncIOScheduler()
bot_token = os.getenv('TOKEN')
id = os.getenv('CHAT_ID')
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
day = date.today()
TZ = timezone('Asia/Bishkek')
pics_catalog = '/data/danibot_files/pics/'
vids_catalog ='/data/danibot_files/vids/'
