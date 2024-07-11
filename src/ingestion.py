from requests import get

def get_ingestion(url, params):

    response = get(url, params = params).json()

    all_records = [data["attributes"] for data in response["features"]]
    records_with_only_valid_values = []

    for i in all_records:
        records_with_only_valid_values.append({key: value for key, value in i.items() if value is not None and value != " "})

    return standardize_dicts(records_with_only_valid_values)


def standardize_dicts(dict_list):

    common_keys = set(dict_list[0].keys()).intersection(*[d.keys() for d in dict_list])

    for d in dict_list:
        for key in list(d.keys()):
            if key not in common_keys:
                del d[key]

    return dict_list