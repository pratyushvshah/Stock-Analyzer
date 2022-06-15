from apirequests import *


# Class for getting all the important financial metrics of a company
class StockDetails:

    def __init__(self, company):

        # Assigning the API request results to variables to use for calculations
        self.company = company
        self.overview = getOverview(company)
        self.income = getIncomeStatement(company)
        self.balance = getBalanceSheet(company)
        self.cash = getCashFlow(company)
        self.info = getInfo(company)
        # Gets gross profit for last 5 years
        self.grossprofit = []
        for i in (0, 1, 2, 3, 4):
            try:
                gp = int(self.income["annualReports"][i]["grossProfit"])
                self.grossprofit.append(gp)
            except:
                self.grossprofit.append(0)
        # Gets revenue for last 5 years
        self.revenue = []
        for i in (0, 1, 2, 3, 4):
            try:
                r = int(self.income["annualReports"][i]["totalRevenue"])
                self.revenue.append(r)
            except:
                self.revenue.append(0)
        # Gets ebitda for last 5 years
        self.ebitda = []
        for i in (0, 1, 2, 3, 4):
            try:
                ebitda = int(self.income["annualReports"][i]["ebitda"])
                self.ebitda.append(ebitda)
            except:
                self.ebitda.append(0)
        # Gets ebit for last 5 years
        self.ebit = []
        for i in (0, 1, 2, 3, 4):
            try:
                ebit = int(self.income["annualReports"][i]["ebit"])
                self.ebit.append(ebit)
            except:
                self.ebit.append(0)
        # Gets net income for last 5 years
        self.netincome = []
        for i in (0, 1, 2, 3, 4):
            try:
                ni = int(self.income["annualReports"][i]["netIncome"])
                self.netincome.append(ni)
            except:
                self.netincome.append(0)
        # Gets income tax expense for last 5 years
        self.incometax = []
        for i in (0, 1, 2, 3, 4):
            try:
                it = int(self.income["annualReports"][i]["incomeTaxExpense"])
                self.incometax.append(it)
            except:
                self.incometax.append(0)
        # Gets interest expense for last 5 years
        self.interestexpense = []
        for i in (0, 1, 2, 3, 4):
            try:
                ie = int(self.income["annualReports"][i]["interestExpense"])
                self.interestexpense.append(ie)
            except:
                self.interestexpense.append(0)
        # Gets current assets for last 5 years
        self.currentasset = []
        for i in (0, 1, 2, 3, 4):
            try:
                ca = int(self.balance["annualReports"][i]["totalCurrentAssets"])
                self.currentasset.append(ca)
            except:
                self.currentasset.append(0)
        # Gets current liabilities for last 5 years
        self.currentliability = []
        for i in (0, 1, 2, 3, 4):
            try:
                cl = int(self.balance["annualReports"][i]["totalCurrentLiabilities"])
                self.currentliability.append(cl)
            except:
                self.currentliability.append(0)
        # Gets non current assets for last 5 years
        self.noncurrentasset = []
        for i in (0, 1, 2, 3, 4):
            try:
                nca = int(self.balance["annualReports"][i]["totalNonCurrentAssets"])
                self.noncurrentasset.append(nca)
            except:
                self.noncurrentasset.append(0)
        # Gets non current libility for last 5 years
        self.noncurrentliability = []
        for i in (0, 1, 2, 3, 4):
            try:
                ncl = int(self.balance["annualReports"][i]["totalNonCurrentLiabilities"])
                self.noncurrentliability.append(ncl)
            except:
                self.noncurrentliability.append(0)
        # Gets shareholers equity for last 5 years
        self.shareholdersequity = []
        for i in (0, 1, 2, 3, 4):
            try:
                se = int(self.balance["annualReports"][i]["totalShareholderEquity"])
                self.shareholdersequity.append(se)
            except:
                self.shareholdersequity.append(0)
        # Gets total assets for last 5 years
        self.totalassets = []
        for i in (0, 1, 2, 3, 4):
            try:
                ta = int(self.balance["annualReports"][i]["totalAssets"])
                self.totalassets.append(ta)
            except:
                self.totalassets.append(0)
        # Gets total liabilities for last 5 years
        self.totalliabilities = []
        for i in (0, 1, 2, 3, 4):
            try:
                tl = int(self.balance["annualReports"][i]["totalLiabilities"])
                self.totalliabilities.append(tl)
            except:
                self.totalliabilities.append(0)
        # Gets inventory for last 5 years
        self.inventory = []
        for i in (0, 1, 2, 3, 4):
            try:
                inv = int(self.balance["annualReports"][i]["inventory"])
                self.inventory.append(inv)
            except:
                self.inventory.append(0)
        # Gets cash and cash equivalents for last 5 years
        self.cash1 = []
        for i in (0, 1, 2, 3, 4):
            try:
                c = int(self.balance["annualReports"][i]["cashAndCashEquivalentsAtCarryingValue"])
                self.cash1.append(c)
            except:
                self.cash1.append(0)
        # Gets operating cash for last 5 years
        self.operatingcash = []
        for i in (0, 1, 2, 3, 4):
            try:
                oc = int(self.cash["annualReports"][i]["operatingCashflow"])
                self.operatingcash.append(oc)
            except:
                self.operatingcash.append(0)
        # Gets capital expenditure for last 5 years
        self.capitalexpenditure = []
        for i in (0, 1, 2, 3, 4):
            try:
                ce = int(self.cash["annualReports"][i]["capitalExpenditures"])
                self.capitalexpenditure.append(ce)
            except:
                self.capitalexpenditure.append(0)
        # Gets short term debt for last 5 years
        self.shorttermdebt = []
        for i in (0, 1, 2, 3, 4):
            try:
                std = int(self.balance["annualReports"][i]["shortTermDebt"])
                self.shorttermdebt.append(std)
            except:
                self.shorttermdebt.append(0)
        # Gets long term debt for last 5 years
        self.longtermdebt = []
        for i in (0, 1, 2, 3, 4):
            try:
                ltd = int(self.balance["annualReports"][i]["longTermDebt"])
                self.longtermdebt.append(ltd)
            except:
                self.longtermdebt.append(0)
        self.currentyear = int(self.income["annualReports"][0]["fiscalDateEnding"].split("-")[0])
        try:
            self.name = f'{self.info["longName"]}'
        except:
            self.name = "n/a"
        try:
            self.ticker = f'{self.info["symbol"]}'
        except:
            self.ticker = "n/a"
        try:
            self.country = f'{self.info["country"]}'
        except:
            self.country = "n/a"
        try:
            self.sector = f'{self.info["sector"]}'
        except:
            self.sector = "n/a"
        try:
            self.industry = f'{self.info["industry"]}'
        except:
            self.industry = "n/a"
        try:
            self.highprice = f'{int(self.info["fiftyTwoWeekHigh"]):.2f}'
        except:
            self.highprice = "n/a"
        try:
            self.price = f'{int(self.info["currentPrice"]):.2f}'
        except:
            self.price = "n/a"
        try:
            self.lowprice = f'{int(self.info["fiftyTwoWeekLow"]):.2f}'
        except:
            self.lowprice = "n/a"
        try:
            self.rec = f'{self.info["recommendationKey"].title()}'
        except:
            self.rec = "n/a"
        try:
            self.target = f'{int(self.info["targetMedianPrice"]):.2f}'
        except:
            self.target = "n/a"
        try:
            self.market = f'{int(self.info["marketCap"]):,}'
        except:
            self.market = "n/a"
        try:
            self.enterprise = f'{int(self.info["enterpriseValue"]):,}'
        except:
            self.enterprise = "n/a"
        try:
            self.rev = f'{int(self.info["totalRevenue"]):,}'
        except:
            self.rev = "n/a"
        try:
            self.debt = f'{int(self.info["totalDebt"]):,}'
        except:
            self.debt = "n/a"
        try:
            self.cash2 = f'{int(self.info["totalCash"]):,}'
        except:
            self.casg2 = "n/a"
        try:
            self.grossprof = f'{int(self.info["grossProfits"]):,}'
        except:
            self.grossprof = "n/a"
        try:
            self.ebitda1 = f'{int(self.info["ebitda"]):,}'
        except:
            self.ebitda1 = "n/a"
        try:
            self.ni = f'{int(self.info["netIncomeToCommon"]):,}'
        except:
            self.ni = "n/a"
        try:
            self.fcf = f'{int(self.info["freeCashflow"]):,}'
        except:
            self.fcf = "n/a"
        try:
            self.shares = f'{int(self.info["sharesOutstanding"]):,}'
        except:
            self.shares = "n/a"
        try:
            self.div = f'{int(self.info["dividendRate"])}%'
        except:
            self.div = "n/a"
        try:
            self.trailpe = f'{int(self.info["trailingPE"]):.2f}x'
        except:
            self.trailpe = "n/a"
        try:
            self.fowpe = f'{int(self.info["forwardPE"]):.2f}x'
        except:
            self.fowpe = "n/a"
        try:
            self.pts12 = f'{int(self.info["priceToSalesTrailing12Months"]):.2f}x'
        except:
            self.pts12 = "n/a"
        try:
            self.ptb = f'{int(self.info["priceToBook"]):.2f}x'
        except:
            self.ptb = "n/a"
        try:
            self.evr = f'{int(self.info["enterpriseToRevenue"]):.2f}x'
        except:
            self.evr = "n/a"
        try:
            self.evebitda = f'{int(self.info["enterpriseToEbitda"]):.2f}x'
        except:
            self.evebitda = "n/a"
        try:
            self.evebit = f'{self.enterprise / self.ebit[0]:.2f}x'
        except:
            self.evebit = "n/a"
        try:
            self.pricetcf = f'{self.price / (self.operatingcash[0] / self.shares):.2f}x'
        except: 
            self.pricetcf = "n/a"


    def companyOverview(self):

        # Pulling the metrics required for Company Overview and storing it in a dictionary
        def details(self):
            d = {
                    'Name': self.name,
                    'Ticker': self.ticker,
                    'Country': self.country,
                    'Sector': self.sector,
                    'Industry': self.industry,
                    '52 Week High': self.highprice,
                    'Current Price': self.price,
                    '52 Week Low': self.lowprice,
                    'Analyst Recommendation': self.rec,
                    'Analyst Target Price': self.target
                }
                
            return d

        def keyFinancials(self):
            kf = {
                    'Market Capitalization': self.market,
                    'Enterprise Value': self.enterprise,
                    'Revenue': self.rev,
                    'Total Debt': self.debt,
                    'Total Cash': self.cash2,
                    'Gross Profit': self.grossprof,
                    'EBITDA': self.ebitda1,
                    'Net Income': self.ni,
                    'Free Cash Flow': self.fcf,
                    'Shares Outstanding': self.shares,
                    'Dividend Rate': self.div 
                }

            return kf

        def valuationMultiples(self):
            vm = {
                    'Trailing PE': self.trailpe,
                    'Forward PE': self.fowpe,
                    'Price to Cash Flow': self.pricetcf,
                    'Price to Sales': self.pts12,
                    'Price to Book': self.ptb,
                    'EV / Revenue': self.evr,
                    'EV / EBITDA': self.evebitda,
                    'EV / EBIT': self.evebit
                }
                
            return vm

        return {"Company Overview": {"Details": details(self), "Key Financials": keyFinancials(self), "Valuation Multiples": valuationMultiples(self)}}


    def marginAnalysis(self):

        # Calculating all the Margins and storing it in a dictionary
        def grossMargin(self):
            gm = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    gm[f"FY{self.currentyear - i}"] = f'{self.grossprofit[i] / self.revenue[i] * 100:.2f}%'
                except:
                    gm[f"FY{self.currentyear - i}"] = "n/m"
            return gm

        def ebitdaMargin(self):
            em ={}
            for i in (0, 1, 2, 3, 4):
                try:
                    em[f"FY{self.currentyear - i}"] = f'{self.ebitda[i] / self.revenue[i] * 100:.2f}%'
                except:
                    em[f"FY{self.currentyear - i}"] = "n/m"
            return em

        def ebitMargin(self):
            eb = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    eb[f"FY{self.currentyear - i}"] = f'{self.ebit[i] / self.revenue[i] * 100:.2f}%'
                except:
                    eb[f"FY{self.currentyear - i}"] = "n/m"
            return eb

        def netIncomeMargin(self):
            nim = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    nim[f"FY{self.currentyear - i}"] = f'{self.netincome[i] / self.revenue[i] * 100:.2f}%'
                except:
                    nim[f"FY{self.currentyear - i}"] = "n/m"
            return nim

        return {"Margin Analysis": {"Gross Margin": grossMargin(self), "EBITDA Margin": ebitdaMargin(self), "EBIT Margin": ebitMargin(self), "Net Income Margin": netIncomeMargin(self)}}

    def profitabilityRatios(self):

        # Calculating all the Profitability Ratios and storing it in a dictionary
        def returnOnEquity(self):
            roe = {}
            for i in (0, 1, 2, 3):
                try:
                    roe[f"FY{self.currentyear - i}"] = f'{self.netincome[i] / ((self.shareholdersequity[i] + self.shareholdersequity[i+1]) / 2) * 100:.2f}%'
                except:
                    roe[f"FY{self.currentyear - i}"] = 'n/m'
                roe[f"FY{self.currentyear - 4}"] = 'n/m'
            return roe

        def returnOnAsset(self):
            roa = {}
            for i in (0, 1, 2, 3):
                try:
                    roa[f"FY{self.currentyear - i}"] = f'{self.netincome[i] / ((self.totalassets[i] + self.totalassets[i+1]) / 2) * 100:.2f}%'
                except:
                    roa[f"FY{self.currentyear - i}"] = 'n/m'
            roa[f"FY{self.currentyear - 4}"] = 'n/m'
            return roa

        def returnOnInvestedCapital(self):
            roic = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    roic[f"FY{self.currentyear - i}"] = f'{(self.ebit[i] - self.incometax[i]) / (self.currentasset[i] - self.currentliability[i] - self.cash1[i] + self.noncurrentasset[i]) * 100:.2f}%'
                except:
                    roic[f"FY{self.currentyear - i}"] = 'n/m'
            return roic

        return {"Profitability Ratios" : {"Return on Equity": returnOnEquity(self), "Return on Asset": returnOnAsset(self), "Return on Invested Capital": returnOnInvestedCapital(self)}}

    def cashFlowRatios(self):

        # Calculating all the Cash Flow Ratios and storing it in a dictionary
        def operatingCashFlowRatio(self):
            cfr = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    cfr[f"FY{self.currentyear - i}"] = f'{self.operatingcash[i] / self.currentliability[i]:.2f}'
                except:
                    cfr[f"FY{self.currentyear - i}"] = 'n/m'
            return cfr

        def cashFlowReturnOnInvestment(self):
            cfroic = {}
            for i in (0, 1, 2, 3):
                try:
                    cfroic[f"FY{self.currentyear - i}"] = f'{(self.operatingcash[i] - self.capitalexpenditure[i]) / ((self.totalliabilities[i] + self.shareholdersequity[i] + self.totalliabilities[i+1] + self.shareholdersequity[i+1]) / 2) * 100:.2f}%'
                except:
                    cfroic[f"FY{self.currentyear - i}"] = 'n/m'
            cfroic[f"FY{self.currentyear - 4}"] = 'n/m'
            return cfroic

        def freeCashFlowToTotalFundedDebt(self):
            fcftfd = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    fcftfd[f"FY{self.currentyear - i}"] = f'{(self.operatingcash[i] - self.capitalexpenditure[i]) / (self.noncurrentliability[i] - self.shareholdersequity[i]) * 100:.2f}%'
                except:
                    fcftfd[f"FY{self.currentyear - i}"] = 'n/m'
            return fcftfd

        return {"Cash Flow Ratios": {"Operating Cash Flow Ratio": operatingCashFlowRatio(self), "Cash Flow Return on Investment": cashFlowReturnOnInvestment(self), "FCF / Total Funded Debt": freeCashFlowToTotalFundedDebt(self)}}

    def solvencyRatios(self):

        # Calculating all the Solvency Ratios and storing it in a dictionary
        def debtToEquityRatio(self):
            dter = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    dter[f"FY{self.currentyear - i}"] = f'{(self.shorttermdebt[i] + self.longtermdebt[i]) / self.shareholdersequity[i] * 100:.2f}%'
                except:
                    dter[f"FY{self.currentyear - i}"] = 'n/m'
            return dter

        def debtToCapitalRatio(self):
            dtcr = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    dtcr[f"FY{self.currentyear - i}"] = f'{(self.shorttermdebt[i] + self.longtermdebt[i]) / (self.shareholdersequity[i] + self.shorttermdebt[i] + self.longtermdebt[i]) * 100:.2f}%'
                except:
                    dtcr[f"FY{self.currentyear - i}"] = 'n/m'
            return dtcr

        def debtToAssetRatio(self):
            dtar = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    dtar[f"FY{self.currentyear - i}"] = f'{(self.shorttermdebt[i] + self.longtermdebt[i]) / self.totalassets[i] * 100:.2f}%'
                except:
                    dtar[f"FY{self.currentyear - i}"] = 'n/m'
            return dtar

        def interestCoverageRatio(self):
            icr = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    icr[f"FY{self.currentyear - i}"] = f'{self.ebit[i] / self.interestexpense[i]:.2f}x'
                except:
                    icr[f"FY{self.currentyear - i}"] = 'n/m'
            return icr

        return {"Solvency Ratios": {"Debt to Equity Ratio": debtToEquityRatio(self), "Debt to Capital Ratio": debtToCapitalRatio(self), "Debt to Asset Ratio": debtToAssetRatio(self), "Interest Coverage Ratio": interestCoverageRatio(self)}}

    def liquidityRatios(self):

        # Calculating all the Liquidity Ratios and storing it in a dictionary
        def currentRatio(self):
            cr = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    cr[f"FY{self.currentyear - i}"] = f'{self.currentasset[i] / self.currentliability[i]:.2f}x'
                except:
                    cr[f"FY{self.currentyear - i}"] = 'n/m'
            return cr

        def quickRatio(self):
            qr = {}
            for i in (0, 1, 2, 3, 4):
                try:
                    qr[f"FY{self.currentyear - i}"] = f'{(self.currentasset[i] - self.inventory[i])/ self.currentliability[i]:.2f}x'
                except:
                    qr[f"FY{self.currentyear - i}"] = 'n/m'
            return qr

        return {"Liquidity Ratios": {"Current Ratio": currentRatio(self), "Quick Ratio": quickRatio(self),}}