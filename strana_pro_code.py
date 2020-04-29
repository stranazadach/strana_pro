import telebot
from array import *
from collections import Counter

bot=telebot.TeleBot('1143459865:AAFyuK43CwKX8wdSx87bF1jdDbDp2EIcraI')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('Хорошо, задавай вопросы')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard2.row('Да', 'Нет')

with open('questions.txt', 'r',encoding="utf-8") as f:
    ques = f.read().splitlines()

counter=100
result=array('i',[0,0,0,0,0])

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Ты в Стране профессий!\n'
                     'Ответь на 30 простых вопросов и я помогу выбрать профессию.',
                     reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def ask(message):
    global counter
    global result

    if message.text == 'Хорошо, задавай вопросы':
        bot.send_message(message.chat.id, 'Ок, поехали...')
        counter=0
        result = array('i', [0, 0, 0, 0, 0])
        bot.send_message(message.chat.id, ques[counter],reply_markup=keyboard2)
        #print('Вопрос', counter + 1, ques[counter * 2])
        #print('counter=', counter)
    elif message.text == 'Да' and counter != 100 and counter!=len(ques)/2-1:
        s=ques[counter*2+1]
        #print('s=',s)
        result[int(s[1])]= result[int(s[1])]+int(s[0])
        counter+=1
        bot.send_message(message.chat.id, ques[counter*2],reply_markup=keyboard2)
        print('Вопрос', counter+1, ques[counter*2])
        print('counter=', counter,'/',len(ques)/2-1)
        print(result)
    elif message.text == 'Нет' and counter != 100 and counter!=len(ques)/2-1:
        s = ques[counter * 2 + 1]
        # print('s=',s)
        result[int(s[1])] = result[int(s[1])] - int(s[0])
        counter += 1
        bot.send_message(message.chat.id, ques[counter * 2], reply_markup=keyboard2)
        print('Вопрос', counter+1, ques[counter*2])
        print('counter=', counter)
        print(result)
    elif message.text == 'Да' and counter == len(ques)/2-1:
        print('мы в последнем ответе')
        s = ques[counter * 2 + 1]
        result[int(s[1])] = result[int(s[1])] + int(s[0])
        bot.send_message(message.chat.id, 'Это был последний вопрос.')
        count=Counter(result)
        print(result)
        print('max =',max(result))
        print('одинаковые максимумы:', max(result), 'всего:', count[max(result)])
        if count[max(result)]>2:
            bot.send_message(message.chat.id, 'Ого! У вас редкое сочетание!'
                                              'Либо вы талантливы во всём, либо еще не разобрались в своих предпочтениях.'
                                              'Попробуйте пройти тест позже или более строго отвечать на вопросы.'
                                              'Для повтора теста отправьте /start')
        if count[max(result)]==2 and result[4]!=max(result):
            bot.send_message(message.chat.id, 'Ого! У вас редкое сочетание!'
                                              'Либо вы талантливы во всём, либо еще не разобрались в своих предпочтениях.'
                                              'Попробуйте пройти тест позже или более строго отвечать на вопросы.'
                                              'Для повтора теста отправьте /start')
        if count[max(result)] == 2 and result[4] == max(result):
            bot.send_message(message.chat.id, 'Ваш тип 4-4')
        if count[max(result)] == 1:
            with open('p'+str(result.index(max(result)))+'.txt', 'r', encoding="utf-8") as f:
                prof1 = f.read().splitlines()
            for text in prof1:
                bot.send_message(message.chat.id, text)
    elif message.text == 'Нет' and counter == len(ques) / 2 - 1:
            print('мы в последнем ответе')
            s = ques[counter * 2 + 1]
            result[int(s[1])] = result[int(s[1])] + int(s[0])
            bot.send_message(message.chat.id, 'Это был последний вопрос.')
            count = Counter(result)
            print(result)
            print('max =', max(result))
            print('одинаковые максимумы:', max(result), 'всего:', count[max(result)])
            if count[max(result)] > 2:
                bot.send_message(message.chat.id, 'Ого! У вас редкое сочетание!'
                                                  'Либо вы талантливы во всём, либо еще не разобрались в своих предпочтениях.'
                                                  'Попробуйте пройти тест позже или более строго отвечать на вопросы.'
                                                  'Для повтора теста отправьте /start')
            if count[max(result)] == 2 and result[4] != max(result):
                bot.send_message(message.chat.id, 'Ого! У вас редкое сочетание!'
                                                  'Либо вы талантливы во всём, либо еще не разобрались в своих предпочтениях.'
                                                  'Попробуйте пройти тест позже или более строго отвечать на вопросы.'
                                                  'Для повтора теста отправьте /start')
            if count[max(result)] == 2 and result[4] == max(result):
                bot.send_message(message.chat.id, 'Ваш тип 4-4')
            if count[max(result)] == 1:
                with open('p' + str(result.index(max(result))) + '.txt', 'r', encoding="utf-8") as f:
                    prof1 = f.read().splitlines()
                for text in prof1:
                    bot.send_message(message.chat.id, text)

bot.polling()
