import requests
from django import http

base_url = 'http://api.exchangeratesapi.io/v1/latest?access_key=95d29b472f6ec45a2040705ca9a606a7'


def convert(from_currency, to_currency, amount):
    response = requests.get(base_url).json()['rates']

    try:
        return round(float(amount) / response[from_currency] * response[to_currency], 2)
    except KeyError:
        return http.HttpResponseBadRequest('Moeda não encontrada')
    except ValueError:
        return http.HttpResponseBadRequest('Valor inválido')
    except TypeError:
        return http.HttpResponseBadRequest('Valor inválido')

print(convert('BRL', 'USD', 100))
