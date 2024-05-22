import move as m

print('Выберите режим игры: \n 1: Автоматическая не оптимизированная \n 2: Автоматическая оптимизированная \n 3: С',
      'помощью стрелочек на клавиатуре')
user = int(input("Ваш ответ: "))

m.show()
if user == 1:
    m.bot1()

elif user == 2:
    m.bot2()

elif user == 3:
    m.userkeyboard()