URL_AND_FILEPATH: dict = {
    "url": "https://check1.fsrar.ru/MobileApi/",
    "filepath": 'captcha_image.jpg'
}

SEARCH_PATTERN: dict = {
    "captcha_image_pattern": 'SampleCaptcha_CaptchaImage.*?src="(.*?)"',
    "captcha_id_pattern": (
        r"BotDetect.Init\('SampleCaptcha', '(.*?)', 'CaptchaCode'"
    )
}

DATA_FOR_THE_REQUEST: dict = {
    "captcha_Id": "SampleCaptcha",
    "url": "https://check1.fsrar.ru/MobileApi/transportwb",
    "status": r'Статус: (.+?)<'
}
