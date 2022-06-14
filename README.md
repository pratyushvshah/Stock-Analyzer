# Preliminary Stock Analysis

This python project is aimed at automating the process of analysing a company's financials.

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

## Usage

1. Go to [AlphaVantage](https://www.alphavantage.co/support/#api-key) and claim your free API key.
2. Download the code to your system and unzip the folder.
3. Create a python file in the same folder with the name `filekeys.py` and assign your API key to a variable called `apikey`. Alternatively, just replace all the `{filekeys.apikey}` with your API key in the `apirequests.py` file.
4. Run `main.py`.

### Optional  

If you wish to bypass authentication for testing purposes -

1. Open `main.py`
2. Enter a new line after line 36.
3. With the correct indentation, type in the following:
```python
        elif userID == "test":
            break
```
4. Save the file and run `main.py`
5. When prompted for "Username" and "Password", respond with "test" in the terminal window.

## TODO

1. Document the code.
2. Make terminal output more comprehensible.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://github.com/pratyushvshah/Preliminary-Stock-Analysis/blob/main/LICENSE)
