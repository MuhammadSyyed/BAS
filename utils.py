import json

def save_response(data, func_name):
    with open(f"./responses/{func_name}.json", "w") as outfile:
        json.dump(data, outfile, indent=6)


def dict_factory(cursor, row):
    data = {}
    for idx, col in enumerate(cursor.description):
        data[col[0]] = row[idx]
    return data
