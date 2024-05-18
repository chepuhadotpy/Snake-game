## Snake-game
В этом репозитории я попытаюсь воссоздать классическую игру "Змейка" на Python.

* ***Я знаю, что игры на Python пишутся с помощью библиотек, подобных pygame. Моя цель написать змейку в терминале.***
* Получается не полноценная игра, а программа стремя короткими способами прохождения. Все так и задумано, не стоит
* забывать о том что это всего лишь проект для оттачивания навыков работы со списками и создания собственных функций.

# *main.py - основной файл*

___
### Введение:
Я считаю что есть множество способов написать эту простую игру на Python. Особенно обработке движения змеи можно
поступить по-разному. Я выбрал такой путь:

#### **Составные части кода:**
Я делю свой код на три части: *func.py*, *move.py* и *main.py*, которые находятся в папке *Code*. В *func.py* содержатся несколько функций, которые не
требуют глобальных переменных извне.
Это функция для мнимой отчистки экрана, которая выводит сотню пустых строк, функция для вывода списков подобно строкам
и функция для создания игрового поля вместе с яблоком. В *move.py* находится основная часть кода: функции для движения
змейки и управления клавиатурой. В *main.py* записано пару строк, которые соединяют код воедино.


___

> # ___Things to do:___
> | Задача                                                                                                                           | Статус             |
> |----------------------------------------------------------------------------------------------------------------------------------|--------------------|
> | Составить несколько простых функций, которые могут понадобиться в дальнейшем.                                                    | :white_check_mark: |
> | Составить функцию для создания игрового поля и яблока. Учесть, что яблоко должно иметь разное расположение при каждой генерации. | :white_check_mark: |
> | Создать функции для обработки всех движений змейки.                                                                              | :white_check_mark: |
> | Разделить код на несколько файлов.                                                                                               | :white_check_mark: |


___
## Про Experiment.py
Уже после того как я дописал свой код, я попросил нейросеть написать змейку в терминале на Python. У нее получился
этот код, который работает в разы лучше, чем мой вариант. На это есть две причины:
* Во-первых, я писал свой вариант змейки с целью отработать действия со строками, а не создать полноценную игру.
* Во_вторых, я попросту не знаю как сделать полноценную игру. Какие-то идеи у меня, правда, возникали, но сделать игру
не удалось. Я почти не понимаю код, написанный нейросетью.

___
## Заключение 
В ходе работы над проектом я узнал очень много полезного, особенно много я узнал про функции. Я узнал как создавать новые функции, как их импортировать и использовать. *Я знаю что мой проект, мягко говоря, не идеален.* С появлением новых знаний я специально не буду исправлять этот проект чтобы посмотреть на него в будущем.

___
## P.S.
Это мой первый опыт разметки MarkDown

[//]: # (СЛЕДУЮЩИЙ ПРОЕКТ - ТГ БОТ ДЛЯ qr-КОДОВ)