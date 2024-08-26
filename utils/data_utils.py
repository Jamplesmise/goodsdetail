def process_single_element_to_dict(single_element):
    if single_element == "kk":
        return {}
    result_dict = {}
    for item in single_element:
        result_dict[item['k']] = item['v']
    return result_dict


def list_of_dicts_to_single_dict(list_of_dicts):
    if list_of_dicts == "kk":
        return {}
    result_dict = {}
    for i, single_dict in enumerate(list_of_dicts, start=1):
        key = f"元素{i}"
        result_dict[key] = single_dict
    return result_dict
