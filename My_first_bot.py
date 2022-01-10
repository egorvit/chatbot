import telebot
from telebot import types
import random

bot = telebot.TeleBot(' ') #Token


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id, 'Усем Прувет!')
    sti = open('файлики для бота/screen-0.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    sti.close()
    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    key_yes = types.KeyboardButton('Спросить')
    key_no = types.KeyboardButton('Боюсь...')
    key_reboot = types.KeyboardButton('Перезагрузить')
    keyboard.add(key_yes, key_no)
    keyboard.add(key_reboot)
    bot.send_message(message.from_user.id, '''Я Магический Шар судьбы, бот созданный для ответа на волнующие тебя вопросы.
    Имей ввиду, формулировать свои вопросы надо так, чтобы ответом на них было только ДА или НЕТ.
    Если ты,конечно, не хочешь испортить всю магию...
    Если готов, нажми 'Спросить', соответсвенно, если боишься, нажми сам догадайся что...
    ''', parse_mode='Markdown', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def dialog(message):
    if message.chat.type == 'private':
        if message.text == 'Спросить':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item = types.InlineKeyboardButton("Получить ответ", callback_data='answer')
            markup.add(item)
            bot.send_message(message.chat.id, '''OK, Тогда задай свой вопрос  и нажми кнопку.
            Вопрос задай про себя, а то колеги, соседи или кто там у тебя, услышат...''', reply_markup=markup)
        elif message.text == 'Боюсь...':
            bot.send_message(message.chat.id, 'Тогда отбой')
            bot.send_message(message.chat.id, '-------------------')
            bot.send_message(message.chat.id, 'Powered by Egor_v_it')
        elif message.text == 'Перезагрузить':
            try:
                for i in range(0, 100):
                    bot.delete_message(message.chat.id, message.message_id - i)
            except Exception:
                pass


        else:
            list_of_phrases = {1: 'Кнопки для кого придуманы..', 2: 'Ну ты, интеллектуал, на кнопки жмякай!',
                               3: 'К сожадению, не могу обработать ваш запрос', 4: 'Ну точно, кнопки, Алеша',
                               5: 'Моя-твоя не понимает, кнопки'}
            x = random.randint(1, 5)
            bot.send_message(message.chat.id, list_of_phrases[x])


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'answer':
        magik_number = random.randint(1, 11)
        list_of_phrases = {1: 'Мне кажется — «да»', 2: 'Мой ответ — «нет»', 3: 'Вероятнее всего',
                           4: 'Перспективы не очень хорошие',
                           5: 'Бесспорно', 6: 'Даже не думай', 7: 'Определённо да', 8: 'Весьма сомнительно',
                           9: 'Сконцентрируйся и спроси опять', 10: 'Пока не ясно, попробуй снова',
                           11: 'Лучше не рассказывать', 12: 'Да!', 13: 'Нет!'}

        bot.send_message(call.message.chat.id, '-------------------')
        bot.send_message(call.message.chat.id, list_of_phrases[magik_number])
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='''OK, Тогда задай свой вопрос  и нажми кнопку''',
                              reply_markup=None)



bot.polling(none_stop=True, interval=0)