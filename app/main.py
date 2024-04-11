import requests
from checkCaptcha import check1_get_captcha
from getAnswerCaptcha import get_solved_captcha
from sendAndGetAnswerFromEgais import send_request_with_captcha
from writeFile import write_file


def main() -> None:
    ''' Главная функция. '''

    with open('DataFile.txt', 'r') as file:
        while True:
            session = requests.Session()
            line = file.readline()            
            if not line:
                break
            ttn = line.split()[0][4:]
            fsrar = line.split()[-1]
            
            captcha_id = check1_get_captcha(session)
            code_captcha = get_solved_captcha()
            status_value = send_request_with_captcha(
                ttn, fsrar, captcha_id, 
                code_captcha, session
            )
            session.close()
            write_file(ttn, fsrar, status_value)

if __name__ == '__main__':
    main()
