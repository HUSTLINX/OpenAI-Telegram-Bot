# Telegram Bot OpenAI ChatGPT version Python by Wannazid
import openai
from aiogram import Bot, Dispatcher, types, executor

bot_tkn = '6206807123:AAFZXbFQ4C40-CciYKsuevdPa8Pus1x7IXg'
openai.api_key = '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'

bot = Bot(token=bot_tkn)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start','help'])
async def user_come(pesan: types.Message):
	await pesan.answer('Selamat Datang, silahkan tanyakan apa saja yang ingin anda ketahui')
	
@dp.message_handler(lambda message: message.text)
async def ai_answer(message: types.Message):
	respon = openai.Completion.create(model='text-davinci-003', prompt=message.text, temperature=0, max_tokens=1000)
	parse = respon['choices'][0]['text']
	await message.reply(parse)
	
print('Bot berjalan !')	
executor.start_polling(dp)
