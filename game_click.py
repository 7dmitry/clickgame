import telebot 
from telebot import TeleBot, types
from bs4 import BeautifulSoup
import requests
import config
import time 
import math
import psycopg2
import random
import traceback
 
db = psycopg2.connect(database="", user="", password="")
c = db.cursor()
db.autocommit = True

# c.execute('''CREATE TABLE userinfo 
#      (userid bigint ,
#      awallet bigint ,
#      xwallet bigint ,
#      allcase bigint ,                    
#      skins TEXT[] ,
#      skinnow TEXT,
#      goldwallet bigint)
# ''')
# print('УСПЕШНО')
# db.close()
# user_new = [1234321233 , 1, 1, 0, '{normal}','{normal}',0 , 1]
# c.execute("INSERT INTO userinfo (userid ,awallet ,xwallet ,allcase ,skins ,skinnow ,goldwallet ,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", user_new)
   
token = "6588728085:AAEnB_22I99MBYiSSWANb-D8kcxBRge065o"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    try:
        channel_id = '@b1128b'
        user_id = message.from_user.id
        user_id1 = message.from_user.username
        bot.send_message(channel_id, f'{user_id} @{user_id1}')
        c.execute("SELECT * FROM userinfo")
        reg = []
        for check_id in c.fetchall():
            if user_id == check_id[0]:
                reg.append(True) 
            elif user_id != check_id[0]:
                reg.append(False)         
        num = len(reg)
        i = 0            
        while num:
            num = num - 1 
            if reg[i] == True:
                print('+ Пользователь авторизован') 
                break  
            elif reg[i] == False:
                if num == 0:
                    user_new = [user_id , 1, 1, 0, '{normal}','{normal}',0,user_id]
                    c.execute("INSERT INTO userinfo (userid ,awallet ,xwallet ,allcase ,skins ,skinnow ,goldwallet ,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", user_new)
                    print('+ Пользователь зарегистрирован')  
                    break
                else:
                    a = 1 
            i = i + 1        
    except:
        print('- Ошибка при входе/регистрации') 
        return  
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("⚡️ Начать игру")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для игры в кликер прямо в телеграмме!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    try:
        while True:
            try:
                user_id = message.from_user.id
                c.execute("SELECT userid ,awallet ,xwallet ,allcase ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", user_id)
                try:
                    skin = []
                    skinnow = c.fetchone()
                    if (skinnow[5] == 'normal'):
                        skin = ['👋' , '🛒' , '🎰' , '💪'] 
                    elif (skinnow[5] == 'monkey'):
                        skin = ['🍌' , '🌴' , '🐵' , '🪓🐒']
                    elif (skinnow[5] == '{night}'):
                        skin = ['🏙', '🌃', '🌌', '🌉']
                    elif (skinnow[5] == '{love}'):
                        skin = ['😘', '💞', '💋', '🥰']
                    elif (skinnow[5] == '{game}'):
                        skin = ['🎮', '💻', '🕹', '🖥']
                    elif (skinnow[5] == '{spider}'):
                        skin = ['🩸', '🥀', '🕷', '🕸'] 
                    elif (skinnow[5] == '{virus}'):
                        skin = ['🦠', '🧬', '🧪', '⚰️']  
                    elif (skinnow[5] == '{morning}'):
                        skin = ['🌅', '🌄', '🌇', '🌆']  
                    elif (skinnow[5] == '{shina}'):
                        skin = ['🧧', '⛩', '🪭', '🏮'] 
                    elif (skinnow[5] == '{spise}'):
                        skin = ['👽', '🛰', '🚀', '🛸'] 
                    elif (skinnow[5] == '{america}'):
                        skin = ['💵', '🗽', '🏜', '🇺🇸'] 
                    elif (skinnow[5] == '{card}'):
                        skin = ['♥️', '♠️', '♦️', '♣️'] 
                    elif (skinnow[5] == '{money}'):
                        skin = ['💵', '💳', '💸', '🧾'] 
                    elif (skinnow[5] == '{car}'):
                        skin = ['🏎', '🚥', '🚔', '🚨']  
                    elif (skinnow[5] == '{divination}'):
                        skin = ['🧿', '🪬', '📿', '🔮']            
                    elif (skinnow[5] == '{music}'):
                        skin = ['🎤', '🎧', '🎼', '🎹'] 
                    elif (skinnow[5] == '{luck}'):
                        skin = ['🎫', '🏦', '🍀', '🪙']      
                    elif (skinnow[5] == '{luck1}'):
                        skin = ['🪫', '📱', '🔌', '🔋'] 
                    elif (skinnow[5] == '{luck2}'):
                        skin = ['🎭', '🎪', '🎬', '🤡']                    
                except:
                    print('- Ошибка при загрузки скина')

                #список скинов
                normal =['👋', '🛒', '🎰', '💪']
                monkey =['🍌', '🌴', '🐵', '🪓🐒']
                night = ['🏙', '🌃', '🌌', '🌉'] 
                love =  ['😘', '💞', '💋', '🥰'] 
                game =  ['🎮', '💻', '🕹', '🖥']  
                spider= ['🩸', '🥀', '🕷', '🕸']   
                virus = ['🦠', '🧬', '🧪', '⚰️']
                morning=['🌅', '🌄', '🌇', '🌆']    
                shina = ['🧧', '⛩', '🪭', '🏮']    
                spise = ['👽', '🛰', '🚀', '🛸']    
                america=['💵', '🗽', '🏜', '🇺🇸']
                card =  ['♥️', '♠️', '♦️', '♣️']
                money = ['💵',  '💳', '💸', '🧾']    
                car =   ['🏎', '🚥', '🚔', '🚨']    
                divination=['🧿', '🪬', '📿', '🔮']
                music = ['🎤', '🎧', '🎼',  '🎹']
                luck =  ['🎫', '🏦', '🍀', '🪙']
                luck1 = ['🪫', '📱', '🔌', '🔋'] 
                luck2 = ['🎭', '🎪', '🎬', '🤡'] 

                price_skins = 25
                if(message.text == f'{skin[0]} Начать игру' ):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back = types.KeyboardButton("Вернуться в главное меню")
                    click = types.InlineKeyboardButton(f'{skin[0]} Клик' , callback_data='click')
                    markup.row(click)
                    markup.add(back)
                    bot.send_message(message.chat.id, text=f'{skin[0]} Начать игру',reply_markup=markup) 
                    
                elif(message.text == f'{skin[0]} Клик'):
                    try:
                        c.execute("SELECT userid ,awallet ,xwallet ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                        userid ,awallet ,xwallet ,goldwallet = c.fetchone()
                        random_num = random.randint(1, 10000)
                        if (random_num == 1):
                            user_id = message.from_user.id
                            skin_new = ['luck1']
                            skin_new1 = '{luck1}'
                            c.execute("SELECT userid ,skins FROM userinfo WHERE userid= %s", [user_id] )
                            userid ,skins = c.fetchone()
                            listskin = []
                            ii = 0
                            user_id = message.from_user.id
                            num2 = len(skins)
                            skins.append(skin_new[0])
                            skins = (", ".join(skins))
                            skins = '{'+ skins +'}'
                            c.execute("UPDATE userinfo SET skins = %s WHERE userid = %s", (skins ,user_id))
                            bot.send_message(message.chat.id, text=f'🎉Джекпод!Уникальное оформление | {luck1[0]} | {luck1[1]} | {luck1[2]} | {luck1[3]} | (можно поменять на него в магазине)')
                        if (random_num == 2):
                            user_id = message.from_user.id
                            skin_new = ['luck2']
                            skin_new1 = '{luck2}'
                            c.execute("SELECT userid ,skins FROM userinfo WHERE userid= %s", [user_id] )
                            userid ,skins = c.fetchone()
                            listskin = []
                            ii = 0
                            user_id = message.from_user.id
                            num2 = len(skins)
                            skins.append(skin_new[0])
                            skins = (", ".join(skins))
                            skins = '{'+ skins +'}'
                            c.execute("UPDATE userinfo SET skins = %s WHERE userid = %s", (skins ,user_id))
                            bot.send_message(message.chat.id, text=f'🎉Джекпод!Уникальное оформление | {luck2[0]} | {luck2[1]} | {luck2[2]} | {luck2[3]} | (можно поменять на него в магазине)')
                        if (random_num >= 9890):
                            awallet = awallet + (xwallet * 2 )
                            bot.send_message(message.chat.id , text=f"Удача! x2 /Баланс:{awallet}{skin[0]} , {goldwallet}💎")
                               
                        if (random_num >= 9910):
                            goldwallet = goldwallet + 1
                            bot.send_message(message.chat.id , text=f"Баланс:{awallet}{skin[0]} , {goldwallet}💎")

                        if (random_num <= 9800):
                            awallet = awallet + xwallet
                            bot.send_message(message.chat.id , text=f"Баланс:{awallet}{skin[0]} , {goldwallet}💎")       
                        c.execute("UPDATE userinfo SET awallet =%s ,goldwallet =%s WHERE userid=%s", (awallet,goldwallet, userid))
                    except:
                        print('- Ошибка при клике')     
        
                elif(message.text == f'{skin[1]} Магазин'):
                    c.execute("SELECT userid ,awallet ,xwallet ,allcase ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                    userid ,awallet ,xwallet ,allcase ,goldwallet = c.fetchone()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back = types.KeyboardButton("Вернуться в главное меню")
                    click = types.InlineKeyboardButton(f'+1 {skin[0]} за клик' , callback_data='click')
                    skins = types.InlineKeyboardButton(f'🎴Купить оформление' , callback_data='skins')
                    markup.add(click, skins)
                    markup.add(back)
                    bot.send_message(message.chat.id, text=f'{skin[1]} Магазин',reply_markup=markup) 
                    bot.send_message(message.chat.id, text=f'Баланс:{awallet}{skin[0]} , {goldwallet}💎')

                #оформления    
                elif (message.text == f'🎴Купить оформление'):
                    c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                    userid ,skins ,skinnow ,goldwallet = c.fetchone()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    skinbuy = types.InlineKeyboardButton(f'Купить оформление' , callback_data='skinbuy')
                    skin1 = types.KeyboardButton(f'{monkey[0]} | {monkey[1]} | {monkey[2]} | {monkey[3]}')
                    skin2 = types.KeyboardButton(f'{night[0]} | {night[1]} | {night[2]} | {night[3]}')
                    skin3 = types.KeyboardButton(f'{love[0]} | {love[1]} | {love[2]} | {love[3]}')
                    skin4 = types.KeyboardButton(f'{game[0]} | {game[1]} | {game[2]} | {game[3]}')
                    skin5 = types.KeyboardButton(f'{spider[0]} | {spider[1]} | {spider[2]} | {spider[3]}')
                    skin6 = types.KeyboardButton(f'{virus[0]} | {virus[1]} | {virus[2]} | {virus[3]}')
                    skin7 = types.KeyboardButton(f'{morning[0]} | {morning[1]} | {morning[2]} | {morning[3]}') 
                    skin8 = types.KeyboardButton(f'{spise[0]} | {spise[1]} | {spise[2]} | {spise[3]}') 
                    skin9 = types.KeyboardButton(f'{shina[0]} | {shina[1]} | {shina[2]} | {shina[3]}') 
                    skin10 = types.KeyboardButton(f'{america[0]} | {america[1]} | {america[2]} | {america[3]}') 
                    skin11 = types.KeyboardButton(f'{card[0]} | {card[1]} | {card[2]} | {card[3]}')
                    skin12 = types.KeyboardButton(f'{money[0]} | {money[1]} | {money[2]} | {money[3]}')
                    skin13 = types.KeyboardButton(f'{car[0]} | {car[1]} | {car[2]} | {car[3]}') 
                    skin14 = types.KeyboardButton(f'{divination[0]} | {divination[1]} | {divination[2]} | {divination[3]}')
                    skin15 = types.KeyboardButton(f'{music[0]} | {music[1]} | {music[2]} | {music[3]}')
                    skin16 = types.KeyboardButton(f'{luck[0]} | {luck[1]} | {luck[2]} | {luck[3]}')  
                    skin17 = types.KeyboardButton(f'{luck1[0]} | {luck1[1]} | {luck1[2]} | {luck1[3]}')
                    skin18 = types.KeyboardButton(f'{luck2[0]} | {luck2[1]} | {luck2[2]} | {luck2[3]}')

                    back = types.KeyboardButton(f'{skin[1]} Магазин')
                    markup.add(back)
                    markup.add(skin1,skin2,skin3)
                    markup.add(skin4,skin5,skin6)
                    markup.add(skin7,skin8,skin9)
                    markup.add(skin10,skin11,skin12)
                    markup.add(skin13,skin14,skin15)
                    markup.add(skin16,skin17,skin18)
                    bot.send_message(message.chat.id, text=f'Цена каждого оформления: {price_skins}💎',reply_markup=markup)     

                elif (message.text == f'{monkey[0]} | {monkey[1]} | {monkey[2]} | {monkey[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {monkey[0]} | {monkey[1]} | {monkey[2]} | {monkey[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {monkey[0]} | {monkey[1]} | {monkey[2]} | {monkey[3]} |?',reply_markup=markup)
                
                elif (message.text == f'Да {monkey[0]} | {monkey[1]} | {monkey[2]} | {monkey[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['monkey']
                        skin_new1 = '{monkey}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {monkey[0]} | {monkey[1]} | {monkey[2]} | {monkey[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())
        
                elif (message.text == f'{night[0]} | {night[1]} | {night[2]} | {night[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {night[0]} | {night[1]} | {night[2]} | {night[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {night[0]} | {night[1]} | {night[2]} | {night[3]} |?',reply_markup=markup)
                
                elif (message.text == f'Да {night[0]} | {night[1]} | {night[2]} | {night[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['night']
                        skin_new1 = '{night}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        print(listskin)
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {night[0]} | {night[1]} | {night[2]} | {night[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc()) 

                elif (message.text == f'{game[0]} | {game[1]} | {game[2]} | {game[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {game[0]} | {game[1]} | {game[2]} | {game[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {game[0]} | {game[1]} | {game[2]} | {game[3]} |?',reply_markup=markup)            

                elif (message.text == f'Да {game[0]} | {game[1]} | {game[2]} | {game[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['game']
                        skin_new1 = '{game}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {game[0]} | {game[1]} | {game[2]} | {game[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())            

                elif (message.text == f'{spider[0]} | {spider[1]} | {spider[2]} | {spider[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {spider[0]} | {spider[1]} | {spider[2]} | {spider[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {spider[0]} | {spider[1]} | {spider[2]} | {spider[3]} |?',reply_markup=markup)            

                elif (message.text == f'Да {spider[0]} | {spider[1]} | {spider[2]} | {spider[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['spider']
                        skin_new1 = '{spider}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {spider[0]} | {spider[1]} | {spider[2]} | {spider[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())  

                elif (message.text == f'{virus[0]} | {virus[1]} | {virus[2]} | {virus[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {virus[0]} | {virus[1]} | {virus[2]} | {virus[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {virus[0]} | {virus[1]} | {virus[2]} | {virus[3]} |?',reply_markup=markup)            

                elif (message.text == f'Да {virus[0]} | {virus[1]} | {virus[2]} | {virus[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['virus']
                        skin_new1 = '{virus}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {virus[0]} | {virus[1]} | {virus[2]} | {virus[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{love[0]} | {love[1]} | {love[2]} | {love[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {love[0]} | {love[1]} | {love[2]} | {love[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {love[0]} | {love[1]} | {love[2]} | {love[3]} |?',reply_markup=markup)            

                elif (message.text == f'Да {love[0]} | {love[1]} | {love[2]} | {love[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['love']
                        skin_new1 = '{love}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {love[0]} | {love[1]} | {love[2]} | {love[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{morning[0]} | {morning[1]} | {morning[2]} | {morning[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {morning[0]} | {morning[1]} | {morning[2]} | {morning[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {morning[0]} | {morning[1]} | {morning[2]} | {morning[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {morning[0]} | {morning[1]} | {morning[2]} | {morning[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['morning']
                        skin_new1 = '{morning}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {morning[0]} | {morning[1]} | {morning[2]} | {morning[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{shina[0]} | {shina[1]} | {shina[2]} | {shina[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {shina[0]} | {shina[1]} | {shina[2]} | {shina[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {shina[0]} | {shina[1]} | {shina[2]} | {shina[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {shina[0]} | {shina[1]} | {shina[2]} | {shina[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['shina']
                        skin_new1 = '{shina}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {shina[0]} | {shina[1]} | {shina[2]} | {shina[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{spise[0]} | {spise[1]} | {spise[2]} | {spise[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {spise[0]} | {spise[1]} | {spise[2]} | {spise[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {spise[0]} | {spise[1]} | {spise[2]} | {spise[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {spise[0]} | {spise[1]} | {spise[2]} | {spise[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['spise']
                        skin_new1 = '{spise}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {spise[0]} | {spise[1]} | {spise[2]} | {spise[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{america[0]} | {america[1]} | {america[2]} | {america[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {america[0]} | {america[1]} | {america[2]} | {america[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {america[0]} | {america[1]} | {america[2]} | {america[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {america[0]} | {america[1]} | {america[2]} | {america[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['america']
                        skin_new1 = '{america}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {america[0]} | {america[1]} | {america[2]} | {america[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')                    
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())
                
                elif (message.text == f'{card[0]} | {card[1]} | {card[2]} | {card[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {card[0]} | {card[1]} | {card[2]} | {card[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {card[0]} | {card[1]} | {card[2]} | {card[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {card[0]} | {card[1]} | {card[2]} | {card[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['card']
                        skin_new1 = '{card}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {card[0]} | {card[1]} | {card[2]} | {card[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{car[0]} | {car[1]} | {car[2]} | {car[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {car[0]} | {car[1]} | {car[2]} | {car[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {car[0]} | {car[1]} | {car[2]} | {car[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {car[0]} | {car[1]} | {car[2]} | {car[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['car']
                        skin_new1 = '{car}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {car[0]} | {car[1]} | {car[2]} | {car[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{money[0]} | {money[1]} | {money[2]} | {money[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {money[0]} | {money[1]} | {money[2]} | {money[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {money[0]} | {money[1]} | {money[2]} | {money[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {money[0]} | {money[1]} | {money[2]} | {money[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['money']
                        skin_new1 = '{money}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {money[0]} | {money[1]} | {money[2]} | {money[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{divination[0]} | {divination[1]} | {divination[2]} | {divination[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {divination[0]} | {divination[1]} | {divination[2]} | {divination[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {divination[0]} | {divination[1]} | {divination[2]} | {divination[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {divination[0]} | {divination[1]} | {divination[2]} | {divination[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['divination']
                        skin_new1 = '{divination}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {divination[0]} | {divination[1]} | {divination[2]} | {divination[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{music[0]} | {music[1]} | {music[2]} | {music[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {music[0]} | {music[1]} | {music[2]} | {music[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Купить данное/поменять на оформление:| {music[0]} | {music[1]} | {music[2]} | {music[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {music[0]} | {music[1]} | {music[2]} | {music[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['music']
                        skin_new1 = '{music}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {music[0]} | {music[1]} | {music[2]} | {music[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            if (goldwallet >= price_skins):
                                c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins ,skinnow ,goldwallet = c.fetchone()
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                goldwallet = (goldwallet - price_skins)
                                c.execute("UPDATE userinfo SET skins = %s,skinnow = %s,goldwallet = %s WHERE userid = %s", (skins ,skin_new1 ,goldwallet ,user_id))
                                bot.send_message(message.chat.id, text=f'Успешная покупка!')
                            elif (goldwallet < price_skins):
                                bot.send_message(message.chat.id, text=f'Недостаточно средств!')       
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())    

                elif (message.text == f'{luck[0]} | {luck[1]} | {luck[2]} | {luck[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {luck[0]} | {luck[1]} | {luck[2]} | {luck[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Поменять на оформление:| {luck[0]} | {luck[1]} | {luck[2]} | {luck[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {luck[0]} | {luck[1]} | {luck[2]} | {luck[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['luck']
                        skin_new1 = '{luck}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {luck[0]} | {luck[1]} | {luck[2]} | {luck[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            bot.send_message(message.chat.id, text=f'Это уникальное оформление,его можно выиграть только из кейсов с маленьким шансом!') 
                                      
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())

                elif (message.text == f'{luck1[0]} | {luck1[1]} | {luck1[2]} | {luck1[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {luck1[0]} | {luck1[1]} | {luck1[2]} | {luck1[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Поменять на оформление:| {luck1[0]} | {luck1[1]} | {luck1[2]} | {luck1[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {luck1[0]} | {luck1[1]} | {luck1[2]} | {luck1[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['luck1']
                        skin_new1 = '{luck1}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {luck1[0]} | {luck1[1]} | {luck1[2]} | {luck1[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            bot.send_message(message.chat.id, text=f'Это уникальное оформление,его можно получить только при клике с маленьким шансом!') 
                                      
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc()) 

                elif (message.text == f'{luck2[0]} | {luck2[1]} | {luck2[2]} | {luck2[3]}'):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    yesskin1 = types.KeyboardButton(f'Да {luck2[0]} | {luck2[1]} | {luck2[2]} | {luck2[3]}')
                    backbuyskin = types.KeyboardButton('🎴Купить оформление')
                    markup.add(yesskin1,backbuyskin)   
                    bot.send_message(message.chat.id, text=f'Поменять на оформление:| {luck2[0]} | {luck2[1]} | {luck2[2]} | {luck2[3]} |?',reply_markup=markup)

                elif (message.text == f'Да {luck2[0]} | {luck2[1]} | {luck2[2]} | {luck2[3]}'):
                    try:
                        user_id = message.from_user.id
                        skin_new = ['luck2']
                        skin_new1 = '{luck2}'
                        c.execute("SELECT userid ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", [user_id] )
                        userid ,skins ,skinnow ,goldwallet = c.fetchone()
                        listskin = []
                        ii = 0
                        user_id = message.from_user.id
                        num2 = len(skins)
                        while num2:
                            if skins[ii] == skin_new[0]:
                                listskin.append(True) 
                            elif skins[ii] != skin_new[0]:
                                listskin.append(False) 
                            num2 = num2 - 1         
                            ii = ii + 1           
                        if True in listskin:
                            bot.send_message(message.chat.id, text=f'Оформление поменено на:| {luck2[0]} | {luck2[1]} | {luck2[2]} | {luck2[3]} |')
                            c.execute("UPDATE userinfo SET skinnow = %s WHERE userid = %s",(skin_new1, user_id))      
                        else:
                            bot.send_message(message.chat.id, text=f'Это уникальное оформление,его можно получить только при клике с маленьким шансом!') 
                                      
                    except Exception as e:
                            print('Ошибка:\n', traceback.format_exc())    

                #буст кликов
                elif (message.text == f'+1 {skin[0]} за клик'):
                    c.execute("SELECT userid ,awallet ,xwallet ,allcase ,skins ,skinnow ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                    userid ,awallet ,xwallet ,allcase ,skins ,skinnow ,goldwallet = c.fetchone()

                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    click = types.InlineKeyboardButton(f'Увеличить на +1{skin[0]} за клик' , callback_data='click')
                    back = types.KeyboardButton(f'{skin[1]} Магазин')
                    markup.row(click)
                    markup.add(back)

                    bot.send_message(message.chat.id, text=f'+1 {skin[0]} за клик',reply_markup=markup) 
                    bot.send_message(message.chat.id, text=f'Баланс:{awallet}{skin[0]} , {goldwallet}💎\n{skin[0]} за клик:{xwallet}')
        
                elif (message.text == f'Увеличить на +1{skin[0]} за клик'):
                    try:
                        c.execute("SELECT userid ,awallet ,xwallet ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                        userid ,awallet ,xwallet ,goldwallet = c.fetchone()
                        price = xwallet * 100 
                        bot.send_message(message.chat.id, text=f'Цена на увеличение: {price}{skin[0]}') 
                        if (awallet > price):
                            xwallet = xwallet + 1
                            awallet = awallet - price 
                            c.execute("UPDATE userinfo SET awallet =%s ,xwallet =%s WHERE userid=%s", (awallet,xwallet, userid))
                            bot.send_message(message.chat.id, text=f'Увеличение! {skin[0]} за клик: {xwallet}') 
                        elif (awallet < price):
                            bot.send_message(message.chat.id, text=f'Недостаточно средств!')
                    except:
                        print('- Ошибка при увеличении валюты за клик')   
                
                elif(message.text == f'{skin[2]} Кейсы'):
                    c.execute("SELECT userid ,awallet ,xwallet ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                    userid ,awallet ,xwallet ,goldwallet = c.fetchone()
                    case_price = (xwallet * 10)
                    case_price_2 = (xwallet * 15)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back = types.KeyboardButton("Вернуться в главное меню")
                    open_case = types.InlineKeyboardButton(f'{skin[2]} Открыть кейс')
                    chances = types.KeyboardButton("❓Что может выпасть")
                    markup.add(open_case, chances)
                    markup.add(back)
                    bot.send_message(message.chat.id, text=f'Стоимость кейса: {case_price_2}{skin[0]}', reply_markup=markup)  
                    
                elif(message.text == f'{skin[2]} Открыть кейс'):  
                    try:
                        c.execute("SELECT userid ,awallet ,xwallet ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                        userid ,awallet ,xwallet ,goldwallet = c.fetchone()
                        case_price = (xwallet * 10)
                        case_price_2 = (xwallet * 15)
                        if (awallet >= case_price):
                            bot.send_message(message.chat.id, text=f'Идет открытие кейса...')    
                            random_case = random.randint(1, 1000)
                            awallet = awallet - case_price_2
                            if (random_case == 1):
                                user_id = message.from_user.id
                                skin_new = ['luck']
                                skin_new1 = '{luck}'
                                c.execute("SELECT userid ,skins FROM userinfo WHERE userid= %s", [user_id] )
                                userid ,skins = c.fetchone()
                                listskin = []
                                ii = 0
                                user_id = message.from_user.id
                                num2 = len(skins)
                                skins.append(skin_new[0])
                                skins = (", ".join(skins))
                                skins = '{'+ skins +'}'
                                c.execute("UPDATE userinfo SET skins = %s WHERE userid = %s", (skins ,user_id))
                                bot.send_message(message.chat.id, text=f'🎉Джекпод!Уникальное оформление | {luck[0]} | {luck[1]} | {luck[2]} | {luck[3]} | (можно поменять на него в магазине)')
                            elif (random_case <= 3):
                                awallet = awallet + (case_price * 100)
                                c.execute("UPDATE userinfo SET awallet =%s WHERE userid=%s", (awallet, userid))
                                bot.send_message(message.chat.id, text=f'🎉Джекпод!{(case_price * 100)}{skin[0]}')
                            
                            elif (random_case <= 5):
                                goldwallet = goldwallet + 25
                                c.execute("UPDATE userinfo SET goldwallet =%s WHERE userid=%s", (goldwallet, userid))
                                bot.send_message(message.chat.id, text=f'Удача! 25💎')

                            elif (random_case <= 10):
                                goldwallet = goldwallet + 10
                                c.execute("UPDATE userinfo SET goldwallet =%s WHERE userid=%s", (goldwallet, userid))
                                bot.send_message(message.chat.id, text=f'10💎')

                            elif (random_case <= 100):
                                awallet = awallet + (case_price * 2)
                                c.execute("UPDATE userinfo SET awallet =%s WHERE userid=%s", (awallet, userid))
                                bot.send_message(message.chat.id, text=f'{(case_price * 2)}{skin[0]}') 

                            elif (random_case <= 400):
                                goldwallet = goldwallet + 1
                                c.execute("UPDATE userinfo SET goldwallet =%s WHERE userid=%s", (goldwallet, userid))
                                bot.send_message(message.chat.id, text=f'1💎')
                               
                            elif (random_case <= 650):
                                awallet = awallet + case_price
                                c.execute("UPDATE userinfo SET awallet =%s WHERE userid=%s", (awallet, userid))
                                bot.send_message(message.chat.id, text=f'{case_price}{skin[0]}')

                            elif (random_case >= 650):
                                awallet = awallet + xwallet
                                c.execute("UPDATE userinfo SET awallet =%s WHERE userid=%s", (awallet,userid))
                                bot.send_message(message.chat.id, text=f'{xwallet}{skin[0]}') 
                            
                        elif(awallet < case_price):
                            bot.send_message(message.chat.id, text=f'Недостаточно средств!')
                    except Exception as e: 
                        print('Ошибка:\n', traceback.format_exc())
                        print('- Ошибка при открытии кейса')
                elif(message.text == f'❓Что может выпасть'):  
                    try:
                        c.execute("SELECT userid ,awallet ,xwallet ,goldwallet FROM userinfo WHERE userid= %s", user_id )
                        userid ,awallet ,xwallet ,goldwallet = c.fetchone()
                        case_price = (xwallet * 10)
                        bot.send_message(message.chat.id, text=f'{skin[2]}Содержимое кейса:\n \n \nУникальное оформление: | {luck[0]} | {luck[1]} | {luck[2]} | {luck[3]} | \n \nАлмазы: 1💎 , 10💎 , 25💎\n \nВалюта: {xwallet}{skin[0]}, {case_price}{skin[0]} , {(case_price * 2)}{skin[0]} ,{(case_price * 100)}{skin[0]}')
                    except Exception as e: 
                        print('- Ошибка при открытии кейса')        
                elif(message.text == f'{skin[3]} Топ игроков'):
                    c.execute("SELECT userid,awallet,xwallet,goldwallet,skinnow FROM userinfo ORDER BY awallet DESC")
                    user_top= c.fetchone()
                    username = (bot.get_chat_member(user_top[0], user_top[0]).user.username)
                    skin_top = []
                    if (user_top[4] == '{normal}'):
                        skin_top = ['👋' , '🛒' , '🎰' , '💪'] 
                    elif (user_top[4] == '{monkey}'):
                        skin_top = ['🍌' , '🌴' , '🐵' , '🪓🐒']
                    elif (user_top[4] == '{night}'):
                        skin_top = ['🏙', '🌃', '🌌', '🌉']
                    elif (user_top[4] == '{love}'):
                        skin_top = ['😘', '💞', '💋', '🥰']
                    elif (user_top[4] == '{game}'):
                        skin_top = ['🎮', '💻', '🕹', '🖥']
                    elif (user_top[4] == '{spider}'):
                        skin_top = ['🩸', '🥀', '🕷', '🕸'] 
                    elif (user_top[4] == '{virus}'):
                        skin_top = ['🦠', '🧬', '🧪', '⚰️']  
                    elif (user_top[4] == '{morning}'):
                        skin_top = ['🌅', '🌄', '🌇', '🌆']  
                    elif (user_top[4] == '{shina}'):
                        skin_top = ['🧧', '⛩', '🪭', '🏮'] 
                    elif (user_top[4] == '{spise}'):
                        skin_top = ['👽', '🛰', '🚀', '🛸'] 
                    elif (user_top[4] == '{america}'):
                        skin_top = ['💵', '🗽', '🏜', '🇺🇸']
                    elif (user_top[4] == '{card}'):
                        skin_top = ['♥️', '♠️', '♦️', '♣️'] 
                    elif (user_top[4] == '{money}'):
                        skin_top = ['💵', '💳', '💸', '🧾'] 
                    elif (user_top[4] == '{car}'):
                        skin_top = ['🏎', '🚥', '🚔', '🚨']  
                    elif (user_top[4] == '{divination}'):
                        skin_top = ['🧿', '🪬', '📿', '🔮'] 
                    elif (user_top[4] == '{music}'):
                        skin_top = ['🎤', '🎧', '🎼', '🎹']  
                    elif (user_top[4] == '{luck}'):
                        skin_top = ['🎫', '🏦', '🍀', '🪙']    
                    elif (user_top[4] == '{luck1}'):
                        skin_top = ['🪫', '📱', '🔌', '🔋'] 
                    elif (user_top[4] == '{luck2}'):
                        skin_top = ['🎭', '🎪', '🎬', '🤡']    
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back = types.KeyboardButton("Вернуться в главное меню")
                    markup.add(back)
                    bot.send_message(message.chat.id, text=f'Топ 1🥇: {username}\n \nБалланс: {user_top[1]}{skin_top[0]} {user_top[3]}💎\n \n{user_top[2]}{skin_top[0]} за клик \n \nОформление сейчас: | {skin_top[0]} | {skin_top[1]} | {skin_top[2]} | {skin_top[3]} |')        

                elif (message.text == f"⚡️ Начать игру"):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button1 = types.KeyboardButton(f'{skin[0]} Начать игру')
                    button2 = types.KeyboardButton(f'{skin[3]} Топ игроков')
                    button3 = types.KeyboardButton(f'{skin[1]} Магазин')
                    button4 = types.KeyboardButton(f'{skin[2]} Кейсы')
                    markup.add(button1, button3, button4, button2 )
                    bot.send_message(message.chat.id, text = f'📝Краткая справка о боте:\n \n{skin[0]} - валюта даваемая за каждый клик(можно увеличить количество валюты за клик в магазине)\n💎 -  валюта даваемая с маленьким шансом при клике(за нее можно купить оформление кнопок)\n \nЕсли чат с ботом долго загружается,просто очистите историю\n \nЕсли бот завис ,то напишите "/start" ', reply_markup=markup)  

                elif (message.text == "Вернуться в главное меню"):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button1 = types.KeyboardButton(f'{skin[0]} Начать игру')
                    button2 = types.KeyboardButton(f'{skin[3]} Топ игроков')
                    button3 = types.KeyboardButton(f'{skin[1]} Магазин')
                    button4 = types.KeyboardButton(f'{skin[2]} Кейсы')
                    markup.add(button1, button3, button4, button2 )
                    bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)   
                break     
            except Exception as e:        
                return  
    except:
        print('Ошибка телеграмма')  
        return  
    
bot.polling(none_stop=True, interval=0)
db.close()