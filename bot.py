# bot.py
import asyncio
from aiogram import Bot, Dispatcher
from config import token
from app.handler import router
from app.db import close_db

async def main():
    bot = Bot(token=token)
    dp = Dispatcher()

    # Добавляем маршрутизатор
    dp.include_router(router)

    # Устанавливаем вебхук и запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    # Закрываем соединение с базой данных при завершении
    await close_db()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот был остановлен.")