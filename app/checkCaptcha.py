import re
from io import BytesIO

from PIL import Image

from constants import SEARCH_PATTERN, URL_AND_FILEPATH


def check1_get_captcha(session) -> str:
    '''
    Ищет капчу и id капчи.
    Капчу сохраняет в указанную папку,
    как картинку. Id капчи возвращает.
    '''

    response = session.get(URL_AND_FILEPATH["url"], verify=False)
    response.raise_for_status()

    response_text = response.text

    # Поиск URL капчи
    captcha_image_match = re.search(
        SEARCH_PATTERN["captcha_image_pattern"],
        response_text
    )
    captcha_id = 'None'
    if captcha_image_match:
        captcha_image_url = (
            f'{URL_AND_FILEPATH["url"]}{captcha_image_match.group(1)}'
        )
        captcha_id_match = re.search(
            SEARCH_PATTERN["captcha_id_pattern"],
            response_text
        )

        if captcha_id_match:
            captcha_id = captcha_id_match.group(1)

            # Загрузка капчи
            captcha_response = session.get(captcha_image_url, verify=False)
            captcha_image = Image.open(BytesIO(captcha_response.content))
            captcha_image.save(URL_AND_FILEPATH["filepath"])
        else:
            print("ID капчи не найден")
    else:
        print("URL капчи не найден")

    return captcha_id
