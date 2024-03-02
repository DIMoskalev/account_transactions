import json

file_path = "../operations.json"


def read_from_file_json(file_path):
    """
    Функция считывает данные из файла file_path, сортирует операции, которые выполнены
    и возвращает отсортированный список с полной информацией по операциям
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def filtered_data_json(unfiltered_data):
    """
    Функция фильтрует операции, которые выполнены и возвращает отфильтрованный список с полной
    информацией по операциям
    """
    filtered_data = []
    for content in unfiltered_data:
        for k, v in content.items():
            if k == "state" and v == "EXECUTED":
                filtered_data.append(content)
    return filtered_data


def sorted_data_json(filtered_data):
    """
    Функция сортирует операции по дате, и возвращает отсортированный список операций
    """
    sorted_data = sorted(filtered_data, key=lambda x: x['date'])
    return sorted_data

def account_disguise(account):
    numbers = []
    for number in account:
        if number.isdigit():
            numbers.append(number)
    if len(numbers) == 16:
        return (f'{account[:-16]}'
                f'{"".join(numbers)[:4]} {"".join(numbers)[5:7]}** **** {"".join(numbers)[-4:]}')

    elif len(numbers) == 20:
        return f'Счет **{"".join(numbers)[-4:]}'
    return numbers
