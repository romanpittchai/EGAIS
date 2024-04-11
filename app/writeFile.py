def write_file(ttn, fsrar, status) -> None:
    ''' Записывает в файл результат запроса в ЕГАИС. '''

    with open('DataFileOut.txt', 'a') as file:
        line = f'TTN-{ttn} {fsrar} {status}\n'
        file.write(line)


def write_logs(balance) -> None:
    ''' Записывает в файл баланс счёта. '''

    with open('balans.txt', 'a') as file:
        line = f'Баланс: {balance}\n'
        file.write(line)
