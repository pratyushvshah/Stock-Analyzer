import requests
import yfinance as yf
import filekeys


def getOverview(company):

    # Pulls and returns the company overview from AlphaVantage
    api = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getIncomeStatement(company):

    # Pulls and returns the company's Income Statement from AlphaVantage
    api = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getBalanceSheet(company):

    # Pulls and returns the company's Balance Sheet from AlphaVantage
    api = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getCashFlow(company):

    # Pulls and returns the company's Cash Flows from AlphaVantage
    api = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getInfo(company):

    # Pulls and returns the company's overview from Yahoo Finance
    ticker = yf.Ticker(company.upper())
    return ticker.info