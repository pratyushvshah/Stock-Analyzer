import requests
import yfinance as yf
import filekeys


def getOverview(company):
    api = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getIncomeStatement(company):
    api = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getBalanceSheet(company):
    api = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getCashFlow(company):
    api = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={company}&apikey={filekeys.apikey}"
    return requests.get(api).json()


def getInfo(company):
    ticker = yf.Ticker(company.upper())
    return ticker.info