from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'Ваш токен бота'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class ToBishFilter(BaseFilter):
    def __init__(self) -> None:
        pass

    async def check(self, message: Message) -> bool:
        tb_count = message.text.lower().count('то бишь')
        print(f"Сообщение '{message.text}' содержит {tb_count} раз(а) слово 'то бишь'")
        return tb_count >= 2

@dp.message()
async def word_tb(message: Message):
    tb_count = message.text.lower().count('то бишь')
    if tb_count >= 2:
        await message.answer(text=f"{message.from_user.username}, Ваше сообщение содержит {tb_count} слов(а)-паразита(-ов) 'то бишь'. Досадно :(")


if __name__ == '__main__':
    dp.run_polling(bot)