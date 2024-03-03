import os
from datetime import datetime
from config import ROOT_DIR
from utils import read_from_file_json, filtered_data_json, sorted_data_json, account_disguise

OPERATIONS_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')


def main():
    file_operation = sorted_data_json(filtered_data_json(read_from_file_json(OPERATIONS_PATH)))
    operations_for_output = file_operation[-5:]
    for operation in operations_for_output:
        date = datetime.fromisoformat(operation['date'])
        date = date.strftime('%d.%m.%Y')
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
            print(f"{account_disguise(away_from)} -> {account_disguise(to_where)}")
        else:
            print(f"{account_disguise(to_where)}")
        print(f"{amount} {currency}\n")


if __name__ == "__main__":
    main()
