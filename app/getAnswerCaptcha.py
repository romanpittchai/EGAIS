import os
import sys

from dotenv import load_dotenv
from twocaptcha import TwoCaptcha

from constants import URL_AND_FILEPATH
from writeFile import write_logs


def get_solved_captcha():
    '''
    Отправка капчи на сервис
    для расшифровки и возврат результата
    (rucaptcha.com).
    '''

    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
    load_dotenv()
    api_key = os.getenv('API_KEY')
    solver = TwoCaptcha(api_key)
    balance = solver.balance()
    print(balance)
    write_logs(balance)
    try:
        result = solver.normal(URL_AND_FILEPATH["filepath"])
    except Exception as error:
        sys.exit(error)
    return result['code']
