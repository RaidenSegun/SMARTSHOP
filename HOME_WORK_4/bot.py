import asyncio 
import logging
import sqlite3

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import token

valid_articuls = {'001', '002', '003', '004'}


bot = Bot(token=token)
dp = Dispatcher()



connection = sqlite3.connect("users.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER,
full_name VARCHAR (30),
username VARCHAR (30),
articul VARCHAR (3)
)
""")

@dp.message(CommandStart()) 
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.full_name}")
    await message.answer(""" 
        Мы рады вас видеть в нашем онлайн магазине по 
        продаже смартфонов, для того чтобы продолжить выберите нужную вам категорию:""", reply_markup=start_keyboard01,)

start_buttons01 = [
    [KeyboardButton(text="О нас 🔍"), KeyboardButton(text="Товары 📱")],
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Контакты 📞")],
]
start_keyboard01 = ReplyKeyboardMarkup(keyboard=start_buttons01, resize_keyboard=True)


@dp.message(F.text == "О нас 🔍") 
async def backend(message: Message):
    await message.answer("""

Добро пожаловать в SmartShop! 
Мы – команда, которая делает покупку смартфонов удобной, быстрой и приятной.

Наша миссия
Мы стремимся предоставить каждому покупателю качественные и современные смартфоны по доступным ценам. 
Наша цель – сделать так, чтобы технологии были доступны каждому, кто хочет быть на шаг впереди и 
получать удовольствие от использования своего устройства.

Почему выбирают нас?
Широкий ассортимент. Мы предлагаем новейшие модели смартфонов от ведущих мировых производителей.
Гарантия качества. Все наши товары проходят строгий контроль перед продажей и имеют официальную гарантию от производителя.
Конкурентные цены. Мы делаем всё возможное, чтобы вы могли приобрести нужное устройство по лучшей цене.
Профессиональная поддержка. Наша команда всегда готова помочь вам выбрать смартфон, подходящий именно вам, 
и ответить на любые вопросы.

Наши преимущества
Быстрая доставка по всей стране
Простые условия возврата и обмена
Гибкие способы оплаты
Постоянные акции и специальные предложения

Контакты
Если у вас возникли вопросы, наша служба поддержки всегда готова помочь. 
Вы можете связаться с нами по телефону +996220772428 или написать на email arzymamatuulub@gmail.com. 
Мы также доступны в мессенджерах и социальных сетях.
Спасибо, что выбираете SmartShop!
""" )

@dp.message(F.text == "Товары 📱") 
async def backend(message: Message):
    await message.answer("Категория Смартфонов:", reply_markup=start_keyboard002)

@dp.message(F.text == "Заказать 📥") 
async def zakaz(message: Message):
    await message.answer("Выберите смартфонов по артикулу:", reply_markup=start_keyboard003)

@dp.message()
async def artic(message:Message):
    cursor.execute("INSERT INTO users (id, full_name, username, articul) VALUES (?, ?, ?, ?)", (message.from_user.id, message.from_user.full_name, message.from_user.username, message.text,))
    connection.commit()
    await message.answer("Спасибо за заказ!")
                         
@dp.message(F.text == "Контакты 📞") 
async def backend(message: Message):
    await message.answer("""
Если у вас есть вопросы то звоните по номеру +996220772428 или можете обратиться к нашим мессенджерам:
""", reply_markup=start_keyboard0001,)
    
start_buttons0001 = [
    [KeyboardButton(text="INSTAGRAM"), KeyboardButton(text="WHATSAPP")], 
                      [KeyboardButton(text="МЕНЮ")],
]
start_keyboard0001 = ReplyKeyboardMarkup(keyboard=start_buttons0001, resize_keyboard=True)


@dp.message(F.text == "INSTAGRAM") 
async def insta(message: Message):
    await message.answer("https://www.linkedin.com/company/geekskg/")

@dp.message(F.text == "WHATSAPP") 
async def whats(message: Message):
    await message.answer("https://api.whatsapp.com/send/?phone=996507052018&text&type=phone_number&app_absent=0")

@dp.message(F.text == "МЕНЮ") 
async def menu(message: Message):
    await message.answer(""" 
        Мы рады вас видеть в нашем онлайн магазине по 
        продаже смартфонов, для того чтобы продолжить выберите нужную вам категорию:""", reply_markup=start_keyboard01,)

start_buttons002 = [
    [KeyboardButton(text="Apple"), KeyboardButton(text="Xiaomi")],
    [KeyboardButton(text="Samsung"), KeyboardButton(text="OnePlus")],
]
start_keyboard002 = ReplyKeyboardMarkup(keyboard=start_buttons002, resize_keyboard=True) 

@dp.message(F.text == "Apple") 
async def iphone(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Apple/iPhone%2016%20Pro/4-500x400.webp")
    await message.answer("""
Iphone 16 pro max
Мобильный CPU            ---   Apple A18 Pro
Тактовая частота (МГц):  ---   4040
Производитель:           ---   Apple
Модель:                  ---   iPhone 16 Pro Max
Год выпуска:             ---   2024
Операционная система:    ---   iOS 18
Габариты (ШхВхТ, мм):    ---   163 x 77.6 x 8.3
Вес (г):                 ---   227
Оперативная память (Гб): ---   8
Встроенная память (Гб):  ---   256
Телефон:                 ---   GSM / CDMA / HSPA / EVDO / LTE / 5G
Bluetooth:               ---   5.3
Wi-Fi:                   ---   Wi-Fi 802.11 a/b/g/n/ac/6/7
Другое:                  ---   GPS, A-GPS, GLONASS, GALILEO,

АРТИКУЛ:  ---   001                 

    ЦЕНА ТОВАРА: 177400 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True) 


@dp.message(F.text == "001") 
async def iphone(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Apple/iPhone%2016%20Pro/4-500x400.webp")
    await message.answer("""
Iphone 16 pro max
Мобильный CPU            ---   Apple A18 Pro
Тактовая частота (МГц):  ---   4040
Производитель:           ---   Apple
Модель:                  ---   iPhone 16 Pro Max
Год выпуска:             ---   2024
Операционная система:    ---   iOS 18
Габариты (ШхВхТ, мм):    ---   163 x 77.6 x 8.3
Вес (г):                 ---   227
Оперативная память (Гб): ---   8
Встроенная память (Гб):  ---   256
Телефон:                 ---   GSM / CDMA / HSPA / EVDO / LTE / 5G
Bluetooth:               ---   5.3
Wi-Fi:                   ---   Wi-Fi 802.11 a/b/g/n/ac/6/7
Другое:                  ---   GPS, A-GPS, GLONASS, GALILEO,

АРТИКУЛ:  ---   001                 

    ЦЕНА ТОВАРА: 177400 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True) 



@dp.message(F.text == "Xiaomi") 
async def xiaomi14(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Xiaomi/Xiaomi%2014/2-500x400.webp")
    await message.answer("""
                         Xiaomi 14
Мобильный CPU               ---   Qualcomm Snapdragon 8 Gen 3
Тактовая частота (МГц):     ---   3300
Количество ядер:            ---   8
Производитель:              ---   Xiaomi
Модель:                     ---   14
Год выпуска:                ---   2023
Операционная система:       ---   Android 14, HyperOS
Габариты (ШхВхТ, мм):       ---   152.8 x 71.5 x 8.2
Вес (г):                    ---   188
Оперативная память (Гб):    ---   12
Встроенная память (Гб):     ---   256
                         
АРТИКУЛ:  ---   002   

    ЦЕНА ТОВАРА: 59900 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True) 



@dp.message(F.text == "002") 
async def xiaomi14(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Xiaomi/Xiaomi%2014/2-500x400.webp")
    await message.answer("""
                         Xiaomi 14
Мобильный CPU               ---   Qualcomm Snapdragon 8 Gen 3
Тактовая частота (МГц):     ---   3300
Количество ядер:            ---   8
Производитель:              ---   Xiaomi
Модель:                     ---   14
Год выпуска:                ---   2023
Операционная система:       ---   Android 14, HyperOS
Габариты (ШхВхТ, мм):       ---   152.8 x 71.5 x 8.2
Вес (г):                    ---   188
Оперативная память (Гб):    ---   12
Встроенная память (Гб):     ---   256
                         
АРТИКУЛ:  ---   002   

    ЦЕНА ТОВАРА: 59900 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True) 



@dp.message(F.text == "Samsung") 
async def sumsung(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Samsung/S24%20Ultra/1-500x400.webp")
    await message.answer("""
                         Samsung Galaxy S24 Ultra 5G
Мобильный CPU               ---   Qualcomm Snapdragon 8 Gen 3
Тактовая частота (МГц):     ---   3390
Количество ядер:            ---   8
Производитель:              ---   Samsung
Модель:                     ---   Galaxy S24 Ultra 5G
Год выпуска:                ---   2024
Операционная система:       ---   Android 14, One UI 6.1
Габариты (ШхВхТ, мм):       ---   162.3 x 79 x 8.6
Вес (г):                    ---   232
Оперативная память (Гб):    ---   12
Встроенная память (Гб):     ---   522

АРТИКУЛ:  ---   003                               

    ЦЕНА ТОВАРА: 101700 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True)    
    
@dp.message(F.text == "003") 
async def sumsung(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Samsung/S24%20Ultra/1-500x400.webp")
    await message.answer("""
                         Samsung Galaxy S24 Ultra 5G
Мобильный CPU               ---   Qualcomm Snapdragon 8 Gen 3
Тактовая частота (МГц):     ---   3390
Количество ядер:            ---   8
Производитель:              ---   Samsung
Модель:                     ---   Galaxy S24 Ultra 5G
Год выпуска:                ---   2024
Операционная система:       ---   Android 14, One UI 6.1
Габариты (ШхВхТ, мм):       ---   162.3 x 79 x 8.6
Вес (г):                    ---   232
Оперативная память (Гб):    ---   12
Встроенная память (Гб):     ---   522

АРТИКУЛ:  ---   003                               

    ЦЕНА ТОВАРА: 101700 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True) 



@dp.message(F.text == "OnePlus") 
async def oneplus(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Oneplus/Open/1-500x400.webp")
    await message.answer("""
                         OnePlus Open
Мобильный CPU               ---   Qualcomm Snapdragon 8 Gen 2
Тактовая частота (МГц):     ---   3200
Количество ядер:            ---   8
Производитель:              ---   OnePlus
Модель:                     ---   Open
Год выпуска:                ---   2023
Операционная система:       ---   Android 13, OxygenOS 13.2
Габариты (ШхВхТ, мм):       ---   В разложенном виде: 153.4 х 143.1 х 5.8 В сложенном виде: 153.4 х 73.3 х 11.7
Вес (г):                    ---   239
Оперативная память (Гб):    ---   16
Встроенная память (Гб):     ---   512
                         
АРТИКУЛ:  ---   004   
                         
    ЦЕНА ТОВАРА: 125000 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True) 


@dp.message(F.text == "004") 
async def oneplus(message: Message):
    await message.answer_photo("https://login.kg/image/cache/webp/catalog/new/Phones/Oneplus/Open/1-500x400.webp")
    await message.answer("""
                         OnePlus Open
Мобильный CPU               ---   Qualcomm Snapdragon 8 Gen 2
Тактовая частота (МГц):     ---   3200
Количество ядер:            ---   8
Производитель:              ---   OnePlus
Модель:                     ---   Open
Год выпуска:                ---   2023
Операционная система:       ---   Android 13, OxygenOS 13.2
Габариты (ШхВхТ, мм):       ---   В разложенном виде: 153.4 х 143.1 х 5.8 В сложенном виде: 153.4 х 73.3 х 11.7
Вес (г):                    ---   239
Оперативная память (Гб):    ---   16
Встроенная память (Гб):     ---   512
                         
АРТИКУЛ:  ---   004   
                         
    ЦЕНА ТОВАРА: 125000 сом
""", reply_markup=start_keyboard003,)

start_buttons003 = [
    [KeyboardButton(text="Заказать 📥"), KeyboardButton(text="Назад")],
]
start_keyboard003 = ReplyKeyboardMarkup(keyboard=start_buttons003, resize_keyboard=True) 

@dp.message(F.text == "Назад") 
async def sumsung01(message: Message):
    await message.answer("Категория Смартфонов:", reply_markup=start_keyboard002,)


@dp.message(F.text == "1") 
async def help3(message: Message):
    await message.answer(""" 
        Мы рады вас видеть в нашем онлайн магазине по 
        продаже смартфонов, для того чтобы продолжить выберите нужную вам категорию:""", reply_markup=start_keyboard01,)

@dp.message(F.text == "2") 
async def help4(message: Message):
    await message.answer("""
Если у вас есть вопросы то звоните по номеру +996220772428 или можете обратиться к нашим мессенджерам:
""", reply_markup=start_keyboard0001,)


@dp.message(F.text == "1") 
async def help3(message: Message):
    await message.answer(""" 
        Мы рады вас видеть в нашем онлайн магазине по 
        продаже смартфонов, для того чтобы продолжить выберите нужную вам категорию:""", reply_markup=start_keyboard01,)

@dp.message(F.text == "2") 
async def help4(message: Message):
    await message.answer("""
Если у вас есть вопросы то звоните по номеру +996220772428 или можете обратиться к нашим мессенджерам:
""", reply_markup=start_keyboard0001,)




@dp.message()
async def echo(message: Message):
    await message.answer("Чем мы вам можем помочь? Чтобы вернутся в главное меню нажмите '1', Если хотите связаться с поддержкой то '2'")



async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")