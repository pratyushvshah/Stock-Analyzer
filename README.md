# Stock Analyzer

This python project is aimed at automating the process of analyzing a company's financials.

## Disclaimer

### Do Your Own Research

This program is intended to be used and must be used for information and education purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances. You should take independent financial advice from a professional in connection with, or independently research and verify, any information that you find on this program and wish to rely upon, whether for the purpose of making an investment decision or otherwise.

## Requirements

Go to `requirements.txt` to install all the modules required to run `main.py`.

For example, run this in your terminal and replace `yfinance` with each item in `requirements.txt` -

```bash
pip install yfinance
```

## Features

1. Gives a company overview.
2. Pulls the key financials of the company.
3. Calculates all the important ratios to understand a company's financials.
4. Gives an option to save the screen in a file named `companyticker.csv` which can be opened through Microsoft Excel.

*The program does not take OTC stocks and most penny stocks.*

## Usage

1. Go to [AlphaVantage](https://www.alphavantage.co/support/#api-key) and claim your free API key.
2. Download the code to your system and unzip the folder.
3. Create a python file in the same folder with the name `filekeys.py` and assign your API key to a variable called `apikey`. Alternatively, just replace all the `{filekeys.apikey}` with your API key in the `apirequests.py` file and remove line 3 which says:

 ```python
 import filekeys
 ```

4. Run `main.py`.

## Demo

https://user-images.githubusercontent.com/89347300/173899146-3f516a69-be25-4067-9060-6c4d88ec7659.mp4

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://github.com/pratyushvshah/Preliminary-Stock-Analysis/blob/main/LICENSE)
