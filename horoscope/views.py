import http.client

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}
types_dict = {'water': ['cancer', 'scorpio', 'pisces'],
              'earth': ['taurus', 'virgo', 'capricorn'],
              'air': ['gemini', 'libra', 'aquarius'],
              'fire': ['aries', 'leo', 'sagittarius']
              }


def types(request):
    url_types_dict = get_response(types_dict, 'types-name')
    return HttpResponse(f'<ul> {url_types_dict} <ul> ')


def get_info_types(request, value: str):
    if value.lower() in types_dict:
        response = get_response(types_dict[value])
        return HttpResponse(f'<ul> {response} <ul> ')
    return HttpResponseNotFound('Not found')


def index(request):
    zodiacs = list(signs)
    context = {
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/index.html', context=context)


def beautiful_table(request):
    return render(request, 'horoscope/table.html')


def get_info_horoscope(request, value: str):
    description = signs.get(value)
    zodiacs = list(signs)

    data = {
        'description_key': description,
        'value_key': value,
        'zodiacs': signs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_horoscope_int(request, value: int):
    zodiacs = list(signs)
    if value >= len(signs):
        return HttpResponseNotFound(f'Неверный порядковый номер знака {value}')
    name_horoscope = zodiacs[value - 1]
    redirect_url = reverse('horoscope-name', args=[name_horoscope])
    return HttpResponseRedirect(redirect_url)


def get_response(value: str, name='horoscope-name'):
    """
    Value: список значений, которые будут выстроены в html таблицу. Каждому будет присвоена ссылка-редирект
    name: имя URL на которую будут вести значения
    """
    url_types_dict = ''
    for i in value:
        redirect_url = reverse(name, args=[i])
        url_types_dict += f'<li><h3> <a href="{redirect_url}"> {i.title()} </a> </h3> </li>'
    return url_types_dict
