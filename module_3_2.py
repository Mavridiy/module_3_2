
def send_email (messange, recipient, sender='university.help@gmail.com'):
    while True:
        check = ['.com', '.ru', '.net']
        res_ch = [ele for ele in check if (ele in recipient)] and [ele for ele in check if (ele in sender)]
        if '@' not in recipient or '@' not in sender:
            break
        if bool(res_ch) == False:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break
        else:
            if sender == recipient:
                print("Нельзя отправить письмо самому себе!")
                break
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                break
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
                break


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
