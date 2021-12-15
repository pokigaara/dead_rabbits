import config
import requests

import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def info(message: types.Message):
    print('бронь')
    await  message.reply('ррррр')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
# def send_telegram(text: str):
#     token = config.TOKEN
#     url = "https://api.telegram.org/bot"
#     channel_id = '@undefined'
#     url += token
#     method = url + '/sendMessage'
#
#     r = requests.post(method, data={
#         'chat_id': channel_id,
#         'text': text
#     })
#
#     if r.status_code != 200:
#         raise Exception('post_text error')
#
#
# if __name__ == '__main__':
#     send_telegram('hello world')
