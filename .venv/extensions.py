import requests
import config
import json
from config import cur_list

api_key = config.API_KEY

class APIException(Exception):
    pass

class APIWork():
    @staticmethod
    def get_price(base, quote, amount):
        try:

            if base not in cur_list or quote not in cur_list:
                raise APIException(f"Одна из введенных валют недоступна. Доступные валюты: {', '.join(cur_list)}")
            try:
                amount = float(amount)
            except ValueError:
                raise APIException("Некорректная сумма. Пожалуйста, введите число.")
            url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base}/{quote}/{amount}"

            # выполняем запрос к API
            response = requests.get(url)
            result = json.loads(response.text)
            if "conversion_result" not in result:
                raise APIException("Нет правильного ответа от API сервиса")
            total_amount = result["conversion_result"]
            return f"Операция прошла успешно. Сумма после обмена: {total_amount}"

        except APIException as e:
            return f"Ошибка: {e}"

        except Exception as e:
            return f"Произошла ошибка при обработке запроса. Проверьте правильность ввода.{e} "





