def filter_by_state(incoming_list: list, state: str ="EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    new_list = []
    for dictionary in incoming_list:
        if "state" in dictionary and dictionary["state"].lower() == state.lower():
            new_list.append(dictionary)
    return new_list

