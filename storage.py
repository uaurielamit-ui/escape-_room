import json


def load_data(addres):
    with open (addres, "r") as file:
        data = json.load(file)
    return data


def dump_data(data, addres):
    with open (addres, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)