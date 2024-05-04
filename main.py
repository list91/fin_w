import os
import datetime

class FinancialTracker:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return file.readlines()
        return []

    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            file.writelines(data)

    def add_record(self, category, amount, description):
        today = datetime.date.today()
        record = f"Дата: {today}\nКатегория: {category}\nСумма: {amount}\nОписание: {description}\n\n"
        data = self.load_data()
        data.append(record)
        self.save_data(data)

    def edit_record(self, index, category=None, amount=None, description=None):
        lines = self.load_data()
        data = "".join(lines).split("\n\n")
        if 0 <= index < len(data):
            record = data[index].split('\n')
            if category:
                record[1] = f"Категория: {category}"
            if amount:
                record[2] = f"Сумма: {amount}"
            if description:
                record[3] = f"Описание: {description}"
            data[index] = '\n'.join(record)
            self.save_data('\n\n'.join(data))
        else:
            print("Неверный индекс записи")

    def search_records(self, category=None, date=None, amount=None):
        lines = self.load_data()
        data = "".join(lines).split("\n\n")
        found_records = []
        for record in data:
            if category != "" and f"Категория: {category}" in record or date != "" and f"Дата: {date}" in record or amount != "" and f"Сумма: {amount}" in record:
                found_records.append(record)
        return found_records

    def calculate_balance(self):
        data = self.load_data()
        income = 0
        expenses = 0
        i = 0
        for record in data:
            if "Доход" in record:
                income += int(data[i+1].split(": ")[-1])
            elif "Расход" in record:
                expenses += int(data[i+1].split(": ")[-1])
            i+=1
        return income, expenses, income - expenses

def main():
    file_path = "finance_data.txt"
    tracker = FinancialTracker(file_path)
    while True:
        print("\nЛичный финансовый кошелек")
        print("1. Вывод баланса")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск по записям")
        print("5. Выход")
        print("#"*20)
        choice = input("Выберите действие: \n")

        if choice == '1':
            income, expenses, balance = tracker.calculate_balance()
            print(f"Доход: {income}")
            print(f"Расход: {expenses}")
            print(f"Баланс: {balance}")

        elif choice == '2':
            category = input("Введите категорию (Доход/Расход): ")
            if category == "Доход" or category == "Расход":
                amount = input("Введите сумму: ")
                if amount.isdigit():
                    description = input("Введите описание: ")
                    tracker.add_record(category, amount, description)
                    print("Запись добавлена успешно!")
                else:
                    print("Неверный ввод")
            else:
                print("Неверный ввод")

        elif choice == '3':
            index = int(input("Введите индекс записи для редактирования: "))
            category = input("Введите новую категорию (если не хотите менять, оставьте пустым): ")
            amount = input("Введите новую сумму (если не хотите менять, оставьте пустым): ")
            description = input("Введите новое описание (если не хотите менять, оставьте пустым): ")
            if category == "Доход" or category == "Расход" or category == "" and amount.isdigit or amount == ""():
                tracker.edit_record(index, category, amount, description)
                print("Запись отредактирована успешно!")
            else:
                print("Неверный ввод")

        elif choice == '4':
            category = input("Введите категорию для поиска (если не хотите искать по категории, оставьте пустым): ")
            date = input("Введите дату для поиска (если не хотите искать по дате, оставьте пустым): ")
            amount = input("Введите сумму для поиска (если не хотите искать по сумме, оставьте пустым): ")
            found_records = tracker.search_records(category, date, amount)
            if found_records:
                print("Найденные записи:")
                for record in found_records:
                    print(record.strip())
            else:
                print("Записи не найдены.")

        elif choice == '5':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")

if __name__ == "__main__":
    main()