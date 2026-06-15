import asyncio
import logging
from config import TOKEN
from aiogram import Bot, Dispatcher
#router
from handlers import cmd_handler, inline


async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Подключаем роутер с нашими обработчиками к главному диспетчеру
    dp.include_routers(
        cmd_handler.router,
        inline.router
        )
    
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())