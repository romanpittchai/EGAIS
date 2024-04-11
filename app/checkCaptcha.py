import re
from io import BytesIO

from PIL import Image

from constants import SEARCH_PATTERN, URL_AND_FILEPATH


def check1_get_captcha(session) -> str:
    '''
    Searches for captcha and captcha id.
    Saves the captcha to the specified folder,
    like a picture. Returns the captcha id.
    '''

    response = session.get(URL_AND_FILEPATH["url"], verify=False)
    response.raise_for_status()

    response_text = response.text

    # Search for the captcha URL
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

            # Uploading a captcha
            captcha_response = session.get(captcha_image_url, verify=False)
            captcha_image = Image.open(BytesIO(captcha_response.content))
            captcha_image.save(URL_AND_FILEPATH["filepath"])
        else:
            print("Captcha ID not found")
    else:
        print("The captcha URL was not found")

    return captcha_id
