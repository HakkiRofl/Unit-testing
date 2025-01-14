import locale
locale.setlocale(locale.LC_ALL, 'RUS')
def price_formating(price_from: int | None, price_to: int | None) -> str:
    add_line_from = ""
    add_line_to = ""
    overflow_flag = True if (price_from and price_to) and price_to // price_from <= 10 else False
    if price_from:
        if 10e2 < price_from < 10e5 and not overflow_flag:
            add_line_from = "тыс "
            price_from = price_from / 10e2
        if 10e5 < price_from < 10e8 and not overflow_flag:
            add_line_from = "млн "
            price_from = price_from / 10e5
        if 10e8 < price_from < 10e11 and not overflow_flag:
            add_line_from = "млрд "
            price_from = price_from / 10e8
        if 10e11 < price_from:
            return None
        if price_to is None:
            price_from = round(price_from, 1) if int(price_from) != price_from else int(price_from)
            return f"от {locale.str(price_from)} {add_line_from}₽"
    if price_to:
        if 10e2 < price_to < 10e5:
            add_line_to = "тыс "
            price_to = price_to / 10e2
            if overflow_flag:
                price_from = price_from / 10e2
        if 10e5 < price_to < 10e8:
            add_line_to = "млн "
            price_to = price_to / 10e5
            if overflow_flag:
                price_from = price_from / 10e5
        if 10e8 < price_to < 10e11:
            add_line_to = "млрд "
            price_to = price_to / 10e8
            if overflow_flag:
                price_from = price_from / 10e8
        if 10e11 < price_to:
            return None
        if price_from is None:
            price_to = round(price_to, 1) if int(price_to) != price_to else int(price_to)
            return f"до {locale.str(price_to)} {add_line_to}₽"
    if price_from and price_to:
        return f"{int(price_from)} {add_line_from}- {int(price_to)} {add_line_to}₽"
    else:
        return "Цена"