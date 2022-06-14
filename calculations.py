from apirequests import *


class StockDetails:

    def __init__(self, company):
        self.company = company
        self.overview = getOverview(company)
        self.income = getIncomeStatement(company)
        self.balance = getBalanceSheet(company)
        self.cash = getCashFlow(company)
        self.info = getInfo(company)

    def marginAnalysis(self):

        def grossMargin(self):
            gm = {}
            for i in (0, 1, 2, 3, 4):
                gm[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.income["annualReports"][i]["grossProfit"]) / int(self.income["annualReports"][i]["totalRevenue"]) * 100:.2f}%'
            return gm

        def ebitdaMargin(self):
            em ={}
            for i in (0, 1, 2, 3, 4):
                em[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.income["annualReports"][i]["ebitda"]) / int(self.income["annualReports"][i]["totalRevenue"]) * 100:.2f}%'
            return em

        def ebitMargin(self):
            eb = {}
            for i in (0, 1, 2, 3, 4):
                eb[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.income["annualReports"][i]["ebit"]) / int(self.income["annualReports"][i]["totalRevenue"]) * 100:.2f}%'
            return eb

        def netIncomeMargin(self):
            nim = {}
            for i in (0, 1, 2, 3, 4):
                nim[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.income["annualReports"][i]["netIncome"]) / int(self.income["annualReports"][i]["totalRevenue"]) * 100:.2f}%'
            return nim

        return {"Margin Analysis": {"Gross Margin": grossMargin(self), "EBITDA Margin": ebitdaMargin(self), "EBIT Margin": ebitMargin(self), "Net Income Margin": netIncomeMargin(self)}}

    def profitabilityRatios(self):

        def returnOnEquity(self):
            roe = {}
            for i in (0, 1, 2, 3):
                roe[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.income["annualReports"][i]["netIncome"]) / ((int(self.balance["annualReports"][i]["totalShareholderEquity"]) + int(self.balance["annualReports"][i + 1]["totalShareholderEquity"])) / 2) * 100:.2f}%'
            roe[f'FY{self.income["annualReports"][4]["fiscalDateEnding"].split("-")[0]}'] = 'n/m'
            return roe

        def returnOnAsset(self):
            roa = {}
            for i in (0, 1, 2, 3):
                roa[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.income["annualReports"][i]["netIncome"]) / ((int(self.balance["annualReports"][i]["totalAssets"]) + int(self.balance["annualReports"][i + 1]["totalAssets"])) / 2) * 100:.2f}%'
            roa[f'FY{self.income["annualReports"][4]["fiscalDateEnding"].split("-")[0]}'] = 'n/m'
            return roa

        def returnOnInvestedCapital(self):
            roic = {}
            for i in (0, 1, 2, 3, 4):
                roic[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{(int(self.income["annualReports"][i]["operatingIncome"]) - int(self.income["annualReports"][i]["incomeTaxExpense"])) / (int(self.balance["annualReports"][i]["totalCurrentAssets"]) - int(self.balance["annualReports"][i]["totalCurrentLiabilities"]) - int(self.balance["annualReports"][i]["cashAndCashEquivalentsAtCarryingValue"]) + int(self.balance["annualReports"][i]["totalNonCurrentAssets"])) * 100:.2f}%'
            return roic

        return {"Profitability Ratios" : {"Return on Equity": returnOnEquity(self), "Return on Asset": returnOnAsset(self), "Return on Invested Capital": returnOnInvestedCapital(self)}}

    def cashFlowRatios(self):

        def operatingCashFlowRatio(self):
            cfr = {}
            for i in (0, 1, 2, 3, 4):
                cfr[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.cash["annualReports"][i]["operatingCashflow"]) / int(self.balance["annualReports"][i]["totalCurrentLiabilities"]):.2f}'
            return cfr

        def cashFlowReturnOnInvestment(self):
            cfroic = {}
            for i in (0, 1, 2, 3):
                cfroic[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{(int(self.cash["annualReports"][i]["operatingCashflow"]) - int(self.cash["annualReports"][i]["capitalExpenditures"])) / ((int(self.balance["annualReports"][i]["totalLiabilities"]) + int(self.balance["annualReports"][i]["totalShareholderEquity"]) + int(self.balance["annualReports"][i + 1]["totalLiabilities"]) + int(self.balance["annualReports"][i + 1]["totalShareholderEquity"])) / 2) * 100:.2f}%'
            cfroic[f'FY{self.income["annualReports"][4]["fiscalDateEnding"].split("-")[0]}'] = 'n/m'
            return cfroic

        def freeCashFlowToTotalFundedDebt(self):
            fcftfd = {}
            for i in (0, 1, 2, 3, 4):
                fcftfd[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{(int(self.cash["annualReports"][i]["operatingCashflow"]) - int(self.cash["annualReports"][i]["capitalExpenditures"])) / (int(self.balance["annualReports"][i]["totalNonCurrentLiabilities"]) - int(self.balance["annualReports"][i]["totalShareholderEquity"])) * 100:.2f}%'
            return fcftfd

        return {"Cash Flow Ratios": {"Operating Cash Flow Ratio": operatingCashFlowRatio(self), "Cash Flow Return on Investment": cashFlowReturnOnInvestment(self), "FCF / Total Funded Debt": freeCashFlowToTotalFundedDebt(self)}}

    def solvencyRatios(self):

        def debtToEquityRatio(self):
            dter = {}
            for i in (0, 1, 2, 3, 4):
                dter[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{(int(self.balance["annualReports"][i]["shortTermDebt"]) + int(self.balance["annualReports"][i]["longTermDebt"])) / int(self.balance["annualReports"][i]["totalShareholderEquity"]) * 100:.2f}%'
            return dter

        def debtToCapitalRatio(self):
            dtcr = {}
            for i in (0, 1, 2, 3, 4):
                dtcr[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{(int(self.balance["annualReports"][i]["shortTermDebt"]) + int(self.balance["annualReports"][i]["longTermDebt"])) / (int(self.balance["annualReports"][i]["totalShareholderEquity"]) + int(self.balance["annualReports"][i]["shortTermDebt"]) + int(self.balance["annualReports"][i]["longTermDebt"])) * 100:.2f}%'
            return dtcr

        def debtToAssetRatio(self):
            dtar = {}
            for i in (0, 1, 2, 3, 4):
                dtar[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{(int(self.balance["annualReports"][i]["shortTermDebt"]) + int(self.balance["annualReports"][i]["longTermDebt"])) / int(self.balance["annualReports"][i]["totalAssets"]) * 100:.2f}%'
            return dtar

        def interestCoverageRatio(self):
            icr = {}
            for i in (0, 1, 2, 3, 4):
                icr[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.income["annualReports"][i]["ebit"]) / int(self.income["annualReports"][i]["interestExpense"]):.2f}x'
            return icr

        return {"Solvency Ratios": {"Debt to Equity Ratio": debtToEquityRatio(self), "Debt to Capital Ratio": debtToCapitalRatio(self), "Debt to Asset Ratio": debtToAssetRatio(self), "Interest Coverage Ratio": interestCoverageRatio(self)}}

    def liquidityRatios(self):

        def currentRatio(self):
            cr = {}
            for i in (0, 1, 2, 3, 4):
                cr[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{int(self.balance["annualReports"][i]["totalCurrentAssets"]) / int(self.balance["annualReports"][i]["totalCurrentLiabilities"]):.2f}x'
            return cr

        def quickRatio(self):
            qr = {}
            for i in (0, 1, 2, 3, 4):
                qr[f'FY{self.income["annualReports"][i]["fiscalDateEnding"].split("-")[0]}'] = f'{(int(self.balance["annualReports"][i]["totalCurrentAssets"]) - int(self.balance["annualReports"][i]["inventory"])) / int(self.balance["annualReports"][i]["totalCurrentLiabilities"]):.2f}x'
            return qr

        return {"Liquidity Ratios": {"Current Ratio": currentRatio(self), "Quick Ratio": quickRatio(self),}}

    def companyOverview(self):

        def details(self):
            d = {
                    'Name': f'{self.info["longName"]}',
                    'Ticker': f'{self.info["symbol"]}',
                    'Country': f'{self.info["country"]}',
                    'Sector': f'{self.info["sector"]}',
                    'Industry': f'{self.info["industry"]}',
                    '52 Week High': f'{int(self.info["fiftyTwoWeekHigh"]):.2f}',
                    'Current Price': f'{int(self.info["currentPrice"]):.2f}',
                    '52 Week Low': f'{int(self.info["fiftyTwoWeekLow"]):.2f}',
                    'Analyst Recommendation': f'{self.info["recommendationKey"].title()}',
                    'Analyst Target Price': f'{int(self.info["targetMedianPrice"]):.2f}'
                }
            return d

        def keyFinancials(self):
            kf = {
                    'Market Capitalization': f'{int(self.info["marketCap"]):,}',
                    'Enterprise Value': f'{int(self.info["enterpriseValue"]):,}',
                    'Revenue': f'{int(self.info["totalRevenue"]):,}',
                    'Total Debt': f'{int(self.info["totalDebt"]):,}',
                    'Total Cash': f'{int(self.info["totalCash"]):,}',
                    'Gross Profit': f'{int(self.info["grossProfits"]):,}',
                    'EBITDA': f'{int(self.info["ebitda"]):,}',
                    'Net Income': f'{int(self.info["netIncomeToCommon"]):,}',
                    'Free Cash FLow': f'{int(self.info["freeCashflow"]):,}',
                    'Shares Outstanding': f'{int(self.info["sharesOutstanding"]):,}',
                    'Dividend Rate': f'{self.info["dividendRate"]}%'
                }

            return kf

        def valuationMultiples(self):
            vm = {
                    'Trailing PE': f'{int(self.info["trailingPE"]):.2f}x',
                    'Forward PE': f'{int(self.info["forwardPE"]):.2f}x',
                    'Price to Cash Flow': f'{int(self.info["currentPrice"]) / (int(self.cash["annualReports"][0]["operatingCashflow"]) / int(self.info["sharesOutstanding"])):.2f}x',
                    'Price to Sales': f'{int(self.info["priceToSalesTrailing12Months"]):.2f}x',
                    'Price to Book': f'{int(self.info["priceToBook"]):.2f}x',
                    'EV / Revenue': f'{int(self.info["enterpriseToRevenue"]):.2f}x',
                    'EV / EBITDA': f'{int(self.info["enterpriseToEbitda"]):.2f}x',
                    'EV / EBIT': f'{int(self.info["enterpriseValue"]) / int(self.income["annualReports"][0]["ebit"]):.2f}x'
                }

            return vm

        return {"Company Overview": {"Details": details(self), "Key Financials": keyFinancials(self), "Valuation Multiples": valuationMultiples(self)}}
