import re
import urllib.parse

from constants import DATA_FOR_THE_REQUEST
from writeFile import write_error


def send_request_with_captcha(
        ttn, fsrar, captcha_id,
        code_captcha, session
) -> str:
    '''
    Makes a request to the EGAIS
    and returns the status of the document.
    '''

    data = {
        'id': ttn,
        'owner_id': fsrar,
        'CaptchaId': DATA_FOR_THE_REQUEST['captcha_Id'],
        'InstanceId': captcha_id,
        'UserInput': code_captcha
    }
    TextRequest = urllib.parse.urlencode(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "Accept": "application/json",
    }
    response = session.post(
        DATA_FOR_THE_REQUEST['url'],
        data=TextRequest,
        headers=headers
    )
    response.raise_for_status()

    response_json = response.json()

    status_pattern = re.search(DATA_FOR_THE_REQUEST['status'], response_json)
    status_value = 'None'
    if status_pattern is not None:
        status_value = status_pattern.group(1)
    else:
        write_error(response_json)
    return status_value
