# Личный финансовый кошелек

Программа **Личный финансовый кошелек** представляет собой консольное приложение для учета личных доходов и расходов. Пользователь может добавлять новые записи о доходах или расходах, редактировать существующие записи, выполнять поиск по записям и просматривать текущий баланс.

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/list91/fin_w
    ```

2. Перейдите в каталог приложения:

    ```bash
    cd fin_w
    ```

3. Запустите программу:

    ```bash
    python main.py
    ```

## Использование

1. **Вывод баланса**: Показывает текущий баланс, а также отдельно доходы и расходы.

2. **Добавление записи**: Позволяет добавить новую запись о доходе или расходе.

3. **Редактирование записи**: Изменяет существующие записи о доходах и расходах.

4. **Поиск по записям**: Позволяет выполнять поиск записей по категории, дате или сумме.

5. **Выход**: Завершает выполнение программы.

## Структура данных в файле

Каждая запись в файле содержит следующие поля:
- Дата
- Категория (Доход/Расход)
- Сумма
- Описание

