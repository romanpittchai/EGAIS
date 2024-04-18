import json


def write_file(ttn, fsrar, status) -> None:
    ''' Writes the result of the EGAIS request to a file.'''

    with open('DataFileOut.txt', 'a') as file:
        line = f'TTN-{ttn} {fsrar} {status}\n'
        file.write(line)


def write_logs(balance) -> None:
    ''' Writes the account balance to the file. '''

    with open('balance.txt', 'a') as file:
        line = f'Balance: {balance} rubles\n'
        file.write(line)


def write_error(response_json) -> None:
    with open('Error.json', 'a') as outfile:
        json.dump(response_json, outfile)
        outfile.write('\n' * 2)
        outfile.write('*' * 20)
        outfile.write('\n' * 2)
