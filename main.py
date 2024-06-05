from aiogram.utils import executor
from config import *
from sending import *


if __name__ == "__main__":
    print(f'{day} -- date of start')
    executor.start_polling(dp, skip_updates=True)
