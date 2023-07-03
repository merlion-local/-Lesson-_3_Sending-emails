import smtplib
import os


friend_name = "Иван"
website = "https://dvmn.org/referrals/ZrywWY269gDOBwt07LUO3z6R0RFWKe7vzGuzS3Rf/"
my_name = "Алексей"

letter = '''
From:ssdd7772006@mail.ru
To:smockotnin@yandex.ru
Subject: python
Content-Type: text/plain; charset="UTF-8";


Привет, {1}! {3} приглашает тебя на сайт {2}!

{2} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {2}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {2}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

formatted_letter = letter.format(friend_name, my_name, website, website, website)
server = smtplib.SMTP_SSL('smtp.mail.ru:465')
login = os.environ['SMTP_LOGIN']
password = os.environ['SMTP_PASSWORD']
server.login(login, password)
server.sendmail('ssdd7772006@mail.ru', 'smockotnin@yandex.ru', formatted_letter.encode("UTF-8"))
server.quit()
