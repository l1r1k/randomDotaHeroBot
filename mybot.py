from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputFile,
)
import random
import json
import os

TOKEN_BOT = "6385833131:AAFp8iJPIfb4JjsQz1fgojnKLMpeLSU26M4"

NAME_BOT = "lirstickerbot"

btn_create_stickerpack = KeyboardButton('/select')
btn_add_sticker = KeyboardButton('/refresh')

main_menu = ReplyKeyboardMarkup(resize_keyboard= True).add(btn_create_stickerpack, btn_add_sticker)

dotaHero = {'heros':['Dawnbreaker', 'Venga', 'Treant', 'Invoker', 'Phantom Assassin', 'Pangolier', 'Sven', 'Gyrocopter', 'Earthshaker', 'Rubick', 'Primal Beast', 'Warlock', 'Brewmaster', 'Skywrath Mage', 'Earth Spirit', 'Faceless Void', 'Legion Commander', 'Ember Spirit', 'Grimstroke', 'Natures Prophet', 'Queen of Pain', 'Slark', 'Dark Willow', 'Templar Assasin', 'Razor', 'Lion', 'Phoenix', 'Doom', 'Keeper of the Light', 'Puck', 'Morph', 'Terrorblade', 'Pudge', 'Lina', 'Marci', 'Storm Spirit', 'Dark Seer', 'MK', 'Naga Siren', 'Io', 'Beastmaster', 'Tusk', 'Bounty Hunter', 'Venomancer', 'Undying', 'Tidehunter', 'Spirit Breaker','Bloodseeker', 'Night Stalker', 'Bane', 'Troll Warlord', 'Muerta', 'Shadow Shaman', 'Outworld Destroyer', 'Mars', 'Bristleback', 'Clockwerk', 'Axe', 'Mirana', 'Nyx Assassin', 'Witch Doctor', 'Timbersaw', 'Clinkz', 'Zeus', 'Windranger','Ancient Apparition', 'Techies', 'Jakiro', 'Huskar', 'Batrider', 'Shadow Demon', 'Shadow Fiend', 'Lone Druid', 'Dazzle', 'Phantom Lancer', 'Snapfire', 'Silencer', 'Kunkka', 'Necrophos', 'Chen', 'Oracle', 'Ursa', 'Disraptor', 'Slardar', 'Death Prophet', 'Lich', 'Visage', 'Hoodwink', 'Drow Ranger', 'Lycan', 'Tinker', 'Viper', 'Leshrac', 'Crystal Maiden', 'Wraith King', 'Elder Titan', 'Enchantress', 'Tiny', 'Pugna', 'Anti-Mage', 'Sand King', 'Riki', 'Winter Wyvern', 'Weaver', 'Luna', 'Omniknight', 'Spectre', 'Centaur Warrunner', 'Chaos Knight', 'Magnus', 'Sniper', 'Dragon Knight', 'Juggernaut', 'Medusa', 'Abaddon', 'Ogre Magi', 'Alchemist', 'Arc Warden', 'Underlord', 'Broodmother', 'Meepo', 'Enigma', 'Lifestealer']}
position = ['1 - Carry', '2 - Mid', '3 - Offlane', 'Pos 4', 'Pos 5']

def randomHero():
    randomNumber = random.randint(0, len(dotaHero['heros']) - 1)
    selectedHero = dotaHero.get('heros')[randomNumber]
    dotaHero.get('heros').remove(selectedHero)
    return selectedHero

def randomPos():
    getPosition = position[random.randint(0, len(position) - 1)]
    return getPosition

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome_message(message: types.Message):
    global dotaHero
    username = message.from_user.full_name
    if (not os.path.exists(os.path.abspath('heros.json'))):
        with open('heros.json', 'w') as file:
            json.dump(dotaHero, file)
    if(os.path.exists(os.path.abspath('changedHeros.json'))):
        with open('changedHeros.json', 'r') as f:
            dotaHero = json.load(f)
    await bot.send_message(message.from_user.id, f"Привет, {username}!\nЭто бот для выбора случайного перса и позиции в доте\nДлина листа{len(dotaHero.get('heros'))}", reply_markup=main_menu)

@dp.message_handler(commands=['select'])
async def select_hero(message: types.Message):
    global dotaHero
    await bot.send_message(message.from_user.id, f"Персонаж: {randomHero()}\nПозиция: {randomPos()}\nДлина листа: {len(dotaHero.get('heros'))}")
    with open('changedHeros.json', 'w') as f:
        json.dump(dotaHero, f)

@dp.message_handler(commands=['refresh'])
async def refreshList(message: types.Message):
    global dotaHero
    with open('heros.json', 'r') as f:
        dotaHero = json.load(f)
    with open('changedHeros.json', 'w') as file:
        json.dump(dotaHero, file)
    await bot.send_message(message.from_user.id, f"Лист перезагружен\nДлина листа: {len(dotaHero.get('heros'))}")
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   