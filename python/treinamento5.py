#this program determiners whether a person is a child, an adolescent, an adult, or an elderly person.
age = int(input('How old are you?:\n'))
if age < 12: #aqui significa que idades MENORES do que 12 (11 para baixo, serão crianças)
    print('You are a child!')
elif age < 18: #aqui significa que idades MENORES DO QUE 18 (do 17 ao número 12), serão ditos como adolescentes
    print('You are a adolescent')
elif age < 60: #aqui significa que idades MENORES que sessenta (59 ao n 18), serão adultos
    print('you are a adult')
else: #basicamente idades apartir de 60 serão ditos como velhos :D
    print('you are a veryy oldddd bro')