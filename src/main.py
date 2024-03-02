from utils import read_from_file_json, filtered_data_json, sorted_data_json

FILE_PATH = "../operations.json"


def main():
    file_operation = sorted_data_json(filtered_data_json(read_from_file_json(FILE_PATH)))
    operations_for_output = file_operation[-5:]
    for operation in operations_for_output:
        date = operation['date'][:10].replace("-", ".")
        description = operation["description"]
        if 'from' in operation.keys():
            away_from = operation['from']
        else:
            away_from = None
        to_where = operation['to']
        amount = operation["operationAmount"]["amount"]
        currency = operation["operationAmount"]["currency"]["name"]
        print(f"{date} {description}")
        if away_from:
            print(f"{away_from} -> {to_where}")
        else:
            print(f"{to_where}")
        print(f"{amount} {currency}\n")


# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.

if __name__ == "__main__":
    main()
