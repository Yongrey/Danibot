from config import *
from datetime import datetime
from aiogram import types
import random
import yaml



# read codenames from external codenames.yaml
with open('codenames.yaml', 'r', encoding='utf8') as code_file:
    code_words = yaml.safe_load(code_file)

# read dictionary files from external dictfiles.yaml
with open('dictfiles.yaml', 'r', encoding='utf8') as config_file:
    config = yaml.safe_load(config_file)
    file_names = config['files']

lines = {}

for file_name in file_names:
    with open(f'dict/{file_name}', encoding="utf8") as file:
        lines[file_name] = file.readlines()



# propability_all = 80
propability_keywords = 80



def is_message_contains_any_word(message, words):
    lower_message = message.text.lower()
    return any(word in lower_message for word in words)

@dp.message_handler()
async def any_message_text2(message: types.Message):
    for key, words in code_words.items():
        if is_message_contains_any_word(message, words):
            file_name = f'{key[5:]}.txt'  # Получаем имя файла из ключа
            if file_name in lines:
                if random.randint(1, 100) <= propability_keywords:
                    await message.reply(random.choice(lines[file_name]))
            else:
                print(f"File {file_name} not found in lines dictionary")
            break



# send video block

async def send_video(chat_id: int):
    all_files = os.listdir(vids_dir)

    with open('usedvids.txt', 'r') as used:
        used_files = used.read().splitlines()
        available_files = list(set(all_files) - set(used_files))
        if not available_files:
            print(f"{datetime.now(TZ)} - No available files to send.")
            return
        video_file = random.choice(available_files)
    video_path = os.path.join(vids_dir, video_file)
    print(f"{datetime.now(TZ)} - Sending video: {video_path}")
    video = open(video_path, 'rb')

    while True:
        try:
            await bot.send_video(chat_id, video)
            with open('usedvids.txt', 'a') as used:
                used.write(video_file + '\n')
            print(f"{datetime.now(TZ)} - Video sent: {video_file}")
            break
        except Exception as e:
            print(f"{datetime.now(TZ)} - Failed to send elpepe: {e}")
            continue
    video.close()



# send photo block

async def send_photo(chat_id: int):
    all_files = os.listdir(pics_dir)

    with open('usedpics.txt', 'r') as used:
        used_files = used.read().splitlines()
        available_files = list(set(all_files) - set(used_files))
        if not available_files:
            print(f"{datetime.now(TZ)} - No available files to send.")
            return
        photo_file = random.choice(available_files)
    photo_path = os.path.join(pics_dir, photo_file)
    print(f"{datetime.now(TZ)} - Sending photo: {photo_path}")
    photo = open(photo_path, 'rb')

    while True:
        try:
            await bot.send_photo(chat_id, photo)
            with open('usedpics.txt', 'a') as used:
                used.write(photo_file + '\n')
            print(f"{datetime.now(TZ)} - Photo sent: {photo_file}")
            break
        except Exception as e:
            print(f"{datetime.now(TZ)} - Failed to send tyan: {e}")
            continue
    photo.close()

# scheduler.add_job(send_photo, CronTrigger(hour=17, minute=25, timezone=TZ), kwargs={'chat_id': id})
# scheduler.add_job(send_text, CronTrigger(hour=17, minute=46, timezone=TZ), kwargs={'chat_id': id})
# scheduler.add_job(send_video, CronTrigger(hour=17, minute=26, timezone=TZ), kwargs={'chat_id': id})

# scheduler.start()

