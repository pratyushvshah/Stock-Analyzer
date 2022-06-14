# Preliminary Stock Analysis

This python project is aimed at automating the process of analysing a company's financials.

## Disclaimer

#### Do Your Own Research

Our content is intended to be used and must be used for information and education purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances. You should take independent financial advice from a professional in connection with, or independently research and verify, any information that you find on our Website and wish to rely upon, whether for the purpose of making an investment decision or otherwise.

## Requirements

Go to requirements.txt to install all the modules required to run `main.py`.

For example, run this in your terminal -
```bash
pip install yfinance
```
## Features

1. Gives a company overview.
2. Pulls the key financials of the company.
3. Calculates all the important ratios to understand a company's financials.
4. Gives an option to save the screen in a `.csv` file.

*The program does not take OTC stocks and most penny stocks.*

## Usage

1. Go to [AlphaVantage](https://www.alphavantage.co/support/#api-key) and claim your free API key.
2. Download the code to your system and unzip the folder.
3. Create a python file in the same folder with the name `filekeys.py` and assign your API key to a variable called `apikey`. Alternatively, just replace all the `{filekeys.apikey}` with your API key in the `apirequests.py` file and remove line 3 which says:
 ```python 
 import filekeys
 ```
4. Run `main.py`.

#### Optional  

If you wish to bypass authentication for testing purposes -

1. Open `main.py`
2. Enter a new line after line 36.
3. With the correct indentation, type in the following:
```python
        elif userID == "test":
            break
```
4. Save the file and run `main.py`
5. When prompted for "Username" and "Password", respond with "test" for both prompts in the terminal window.

## TODO

1. Document the code.
2. Make terminal output more comprehensible.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://github.com/pratyushvshah/Preliminary-Stock-Analysis/blob/main/LICENSE)
