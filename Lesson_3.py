import smtplib
import os


SENDER = os.environ['SENDER']
RECIPIENT = os.environ['RECIPIENT']
friend_name = "Иван"
my_name = "Алексей"
website="https://dvmn.org/referrals/ZrywWY269gDOBwt07LUO3z6R0RFWKe7vzGuzS3Rf/"

letter = '''
From: {0}
To: {1}
Content-Type: text/plain; charset="UTF-8";
\nSubject: Курсы Python

Привет, {2}! {3} приглашает тебя на сайт {4}!

{4} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {4}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {4}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

formatted_letter = letter.replace('\nSubject:', ' Subject:').replace('\nContent-Type:', ' Content-Type:').format(SENDER,RECIPIENT,friend_name, my_name, website)
server = smtplib.SMTP_SSL('smtp.mail.ru:465')
login = os.environ['SMTP_LOGIN']
password = os.environ['SMTP_PASSWORD']
server.login(login, password)
server.sendmail(SENDER,RECIPIENT,formatted_letter.encode("UTF-8"))
server.quit()




