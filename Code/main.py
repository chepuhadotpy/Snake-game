from move import bot1, bot2, userkeyboard, show


print('Выберите режим игры: \n 1: Автоматическая не оптимизированная \n 2: Автоматическая оптимизированная \n 3: С',
      'помощью стрелочек на клавиатуре')
user = int(input("Ваш ответ: "))

show()
if user == 1:
    bot1()

if user == 2:
    bot2()

if user == 3:
    userkeyboard()
