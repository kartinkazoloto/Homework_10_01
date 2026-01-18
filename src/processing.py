def filter_by_state(incoming_list: list[dict], state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    new_list: list = []
    for dictionary in incoming_list:
        if "state" not in dictionary:
            continue
        if not isinstance(dictionary["state"], str):
            continue
        if dictionary["state"].upper() == state.upper():
            new_list.append(dictionary)
    return new_list


def sort_by_date(incoming_list: list, ascending: bool) -> list:
    """
    Функция возвращает новый список, отсортированный по дате.
    """
    sorted_date_list: list = []
    for dictionary in incoming_list:
        sorted_date_list = sorted(incoming_list, key=lambda x: x.get("date", 0), reverse=ascending)
    return sorted_date_list
