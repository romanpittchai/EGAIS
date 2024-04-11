def write_file(ttn, fsrar, status) -> None:
    ''' Writes the result of the USAIS request to a file.'''

    with open('DataFileOut.txt', 'a') as file:
        line = f'TTN-{ttn} {fsrar} {status}\n'
        file.write(line)


def write_logs(balance) -> None:
    ''' Writes the account balance to the file. '''

    with open('balance.txt', 'a') as file:
        line = f'Balance: {balance} rubles\n'
        file.write(line)
