# Homework19
1) У командному рядку на комп'ютері необхідно виконати таку команду:

 docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres

В результаті створиться контейнер.

2) Cтворіть базу даних postgres з паролем 1234.

3) Створіть нову базу даних з назвою web971.

4) Скопіюйте вміст файлу env.py з папки migrations в окремий файл або куди зручно. Папку з міграціями видаліть!!!.

5) Запустіть наступну команду в терміналі PyCharm наступну команду:

  alembic init migrations

6) У створені папці замініть вміст файлу env.py на той, що раніше був скопійований (пункт 4).

7) Виконайте по черзі команди:

alembic revision -m "init"

alembic upgrade head

alembic revision --autogenerate -m 'Init'

alembic upgrade head

8) Запустьтіть код в файлі seed.py. В результаті створяться шість таблиць, п'ять з яких будуть заповнені фейковими даними (крім Users).

10) Запустьтіть код в файлі signup.py. В результаті отримаємо відповіді на 12 запитів (разом з логами, які можна відключити).

Додатково:
1) У файлі main.py можна додавати, змінювати, видаляти, створювати записи в таблицях.

2) Для цього в консолі введіть команди на Ваш вибір:

py main.py -a create -m Student -fn 'Василь' -idg 1 -l asd
py main.py -a create -m Group -n '4_В' -l asd
py main.py -a create -m Teacher -fn 'Іван Степанович' --l asd
py main.py --a create -m Discipline -n "Фізика" -idt 1 -l asd
py main.py -a create -m Grade -g 2 -d "2021-10-01"  -ids 1 -idd 1 -l asd

py main.py -a list -m Student -l asd
py main.py -a list -m Group -l asd
py main.py -a list -m Teacher -l asd
py main.py -a list -m Discipline -l asd
py main.py -a list -m Grade -l asd


py main.py -a update -m Student -id 1 -fn "Марія" -idg 1 -l asd
py main.py -a update -m Group -id 1 n "10В"-l asd
py main.py -a update -m Teacher -id 1 -fn "Баль Олена" -l asd
py main.py -a update -m Discipline -id 1 -n "Історія України" -idt 1 -l asd
py main.py -a update -m Grade -id  -g 3 -d "2021-10-01"  -ids 1 -idd 1 -l asd


py main.py -a remove -m Student -id 1 -l asd
py main.py -a remove -m Group -id 1 -l asd
py main.py -a remove -m Teacher -id 1 -l asd
py main.py -a remove -m Discipline -id 1 -l asd
py main.py -a remove -m Grade -id 1 -l asd
