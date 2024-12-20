import telebot


name = 'Брауни'
energy = 80
satiety = 80
happiness = 80


# Функции еды
def feed(chat_id):
    bot.send_message(chat_id, 'Чем вы хотите накормить вашего питомца? /sweets = сладости, /salad = салат, /soup = суп, /steak = стейк')
    check(chat_id)

def sweets(chat_id):
    global satiety, energy, happiness
    energy += 5
    happiness += 25
    satiety += 10
    check(chat_id)

def salad(chat_id):
    global satiety, energy, happiness
    energy += 10
    happiness += 10
    satiety += 15
    check(chat_id)

def soup(chat_id):
    global satiety, energy, happiness
    energy += 20
    happiness += 5
    satiety += 25
    check(chat_id)

def steak(chat_id):
    global satiety, energy, happiness
    energy += 25
    happiness += 15
    satiety += 30
    check(chat_id)


#Функции игры
def game(chat_id):
    bot.send_message(chat_id, 'Во что вы хотите поиграть с вашим питомцем? /football = футбол, /basketball = баскетбол , /catch_up = догонялки, /chess = шахматы.')
    check(chat_id)

def football(chat_id):
    global satiety, energy, happiness
    energy -= 25
    happiness += 30
    satiety -= 20
    check(chat_id)

def basketball(chat_id):
    global satiety, energy, happiness
    energy -= 25
    happiness += 30
    satiety -= 15
    check(chat_id)

def catch_up(chat_id):
    global satiety, energy, happiness
    energy -= 15
    happiness += 15
    satiety -= 15
    check(chat_id)

def chess(chat_id):
    global satiety, energy, happiness
    energy += 0
    happiness += 10
    satiety -= 15
    check(chat_id)


#Функции сна
def sleep(chat_id):
    bot.send_message(chat_id,'Где ваш питомец будет спать? /sofa = на диване , /bed = на кровати , /floor = на полу , /friend = ночевка у друга')
    check(chat_id)

def sofa(chat_id):
    global satiety, energy, happiness
    energy += 40
    happiness += 35
    satiety -= 20
    check(chat_id)

def bed(chat_id):
    global satiety, energy, happiness
    energy += 50
    happiness += 45
    satiety -= 20
    check(chat_id)

def floor(chat_id):
    global satiety, energy, happiness
    energy += 30
    happiness += 10
    satiety -= 20
    check(chat_id)

def friend(chat_id):
    global satiety, energy, happiness
    energy += 35
    happiness += 50
    satiety -= 20
    check(chat_id)


def check(chat_id):
    global happiness, satiety, energy
    satiety = max(0,min(satiety,100))
    energy = max(0,min(energy,100))
    happiness = max(0,min(happiness,100))
    if satiety <= 20:
        bot.send_message(chat_id, 'Игра закончена. Ваш питомец умер от голода.')
    elif satiety <= 45:
        bot.send_message(chat_id, 'Ваш питомец очень голодный, не забывайте его кормить!')
    else:
        bot.send_message(chat_id, 'Все отлично, ваш питомец сыт.')

    if happiness <= 20:
        bot.send_message(chat_id, 'Игра закончена. Ваш питомец умер от скуки.')
    elif happiness <= 40:
        bot.send_message(chat_id, 'Вашему питомцу очень скучно, не забывайте играть с ним!')
    else:
        bot.send_message(chat_id, 'Все отлично, ваш питомец счастлив.')

    if energy <= 20:
        bot.send_message(chat_id, 'Игра закончена. Ваш питомец умер от усталости.')
    elif energy <= 35:
        bot.send_message(chat_id, 'Ваш питомец очень устал, не забывайте отдыхать!')
    else:
        bot.send_message(chat_id, 'Все отлично, ваш питомец полон сил.')


# Убедитесь, что ваш токен правильный
bot_token = '7508239534:AAHU1DEMaJWz0V7mXrtU8b_m07bvfcE6nik'
bot = telebot.TeleBot(bot_token)


#Команда старт
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, дорогой игрок, ты попал в бот, в котором ты можешь поиграть в Тамагочи (это электронная игрушка, которая имитирует уход за домашним питомцем). У тебя есть возможность накормить своего питомца, поиграть с ним или лечь спать. Взависимости от того, какой выбор ты сделаешь, будут менятся показатели энергии, счастья и сытости. Удачи!')

# Обработчик для команды /feed
@bot.message_handler(commands=['feed'])
def feed_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    feed(chat_id)
    bot.send_message(message.chat.id, f'{name} вкусно покушал, теперь его сытость составляет {satiety}.')

# Обработчик для команды /game
@bot.message_handler(commands=['game'])
def game_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    game(chat_id)
    bot.send_message(message.chat.id, f'{name} классно поиграл, теперь его счастье составляет {happiness}.')

# Обработчик для команды /sleep
@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    sleep(chat_id)
    bot.send_message(message.chat.id, f'{name} хорошо выспался, теперь его энергия составляет {energy}.')


# ЕДА
@bot.message_handler(commands=['sweets'])
def sweets_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    sweets(chat_id)
    bot.send_message(message.chat.id, f'{name} поел сладостей, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['salad'])
def salad_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    salad(chat_id)
    bot.send_message(message.chat.id, f'{name} поел салад, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['soup'])
def soup_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    soup(chat_id)
    bot.send_message(message.chat.id, f'{name} поел суп, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['steak'])
def steak_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    steak(chat_id)
    bot.send_message(message.chat.id, f'{name} поел стейк, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')


#ИГРЫ
@bot.message_handler(commands=['football'])
def football_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    football(chat_id)
    bot.send_message(message.chat.id, f'{name} поиграл в футбол, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['basketball'])
def basketball_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    basketball(chat_id)
    bot.send_message(message.chat.id, f'{name} поиграл в баскетбол, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['catch_up'])
def catch_up_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    catch_up(chat_id)
    bot.send_message(message.chat.id, f'{name} поиграл в догонялки, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['chess'])
def chess_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    chess(chat_id)
    bot.send_message(message.chat.id, f'{name} поиграл в шахматы, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')


#СОН
@bot.message_handler(commands=['sofa'])
def sofa_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    sofa(chat_id)
    bot.send_message(message.chat.id, f'{name} поспал на диване, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['bed'])
def bed_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    bed(chat_id)
    bot.send_message(message.chat.id, f'{name} поспал на кровати, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['floor'])
def floor_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    floor(chat_id)
    bot.send_message(message.chat.id, f'{name} поспал на полу, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')

@bot.message_handler(commands=['friend'])
def friend_handler(message):
    chat_id = message.chat.id  # Сохраняем chat_id для дальнейших сообщений
    friend(chat_id)
    bot.send_message(message.chat.id, f'{name} ночевал у друга, теперь его сытость составляет {satiety}, счастье составляет {happiness} и энергия составляет {energy}.')


# Запуск бота
bot.polling(none_stop=True)