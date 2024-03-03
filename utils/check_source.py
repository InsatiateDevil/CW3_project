def print_source_correct(info_about_source):
    """
    :param info_about_source: содержит строку с описанием источника(карта или счет) и его номер
    :return: готовое, отредактированное сообщение с замаскированными элементами номера
    """
    count = 0
    for symbol in info_about_source:
        if symbol.isdigit():
            count += 1
    if count == 16:
        number = info_about_source[-16:]
        first_block = f"{number[:4]}"
        second_block = f"{number[4:6]}**"
        third_block = f"****"
        fourth_block = f"{number[-4:]}"
        return f"{info_about_source[:-16]}{first_block} {second_block} {third_block} {fourth_block}"
    elif count == 20:
        return f"Счет **{info_about_source[-4:]}"
