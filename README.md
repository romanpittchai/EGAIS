# Request for TTN statuses from the EGAIS
## Basic description

The script is designed to request TTN statuses in the USAIS system. Captcha bypass is performed using the captcha bypass service [rucaptcha](https://rucaptcha.com) using a ready-made module from this service.

In order to use the script, you need to download it to your PC, then install a virtual environment:
- windows `python -m venv venv`
- linux/macOS `python3 -m venv venv`

Then you need to activate the virtual environment:
- windows `...Dev/yatube_project$ source venv/Scripts/activate`
- linux/macOS `...Dev/yatube_project$ source venv/bin/activate`

Update pip and install all necessary packages:
- `python3 -m pip install --upgrade pip`
- `pip install -r requirements.txt`

After that, you should already have the data file(`DataFile.txt`), a sample of which will be in the repository - `DataFilExample.txt`. The format should be as follows - ttn number(`TTN-0699868064`) and fsrar number(`030000015637`). Then you can run the script and it will gradually download the captcha, send it for decryption, make a request with all this data to the EGAIS.

The result will be written to a file `DataFileOut.txt`.
You must also create an `.env` file with your access key to the service to decrypt the captcha. An example file is `.envExample`

### Author

_Bogatyrev Roman_

> ***_Note:_*** _The project uses the MIT License.