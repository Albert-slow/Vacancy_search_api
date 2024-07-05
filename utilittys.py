def generator(link, page):

    try:
        url = f'https://tashkent.hh.uz/search/vacancy?text={link}'
        return url
    except:
        return "Произошла ошибка, попробуйте ещё раз"
