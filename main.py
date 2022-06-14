from calculations import StockDetails
from apirequests import getOverview
import sys
import csv


def main():
    company = getCompany()
    stock = StockDetails(company)
    co = stock.companyOverview()
    ma = stock.marginAnalysis()
    pr = stock.profitabilityRatios()
    cfr = stock.cashFlowRatios()
    sr = stock.solvencyRatios()
    lr = stock.liquidityRatios()
    getScreen(co, ma, pr, cfr, sr, lr)
    while True:
        ss = input("Do you wish to save this screen? (Y/N) ").lower().strip()
        if ss == 'y':
            saveScreen(company, co, ma, pr, cfr, sr, lr)
            sys.exit("Thank you for using the screen")
        elif ss == 'n':
            sys.exit("Thank you for using the screen")
        else:
            print("Invalid input")
            continue


def getCompany():
    company = input("Enter Company Ticker (example: MSFT): ")
    while company == "" or len(company) > 5 or getOverview(company) == {}:
        print("Invalid Ticker")
        company = input("Enter Company Ticker (example: MSFT): ")
    return company


def getScreen(co, ma, pr, cfr, sr, lr):
    for a in [co, ma, pr, cfr, sr, lr]:
        title = list(a.keys())
        print()
        print(title[0])
        print()
        for i in a[title[0]]:
            print()
            print(i)
            print()
            for j, k in a[title[0]][i].items():
                print(j, k, sep="\t")


def saveScreen(company, co, ma, pr, cfr, sr, lr):
        with open(f"{company}.csv", "w", newline='') as f:
            file = csv.writer(f, delimiter=",")
            for a in [co, ma, pr, cfr, sr, lr]:
                title = list(a.keys())
                file.writerow(title)
                for i in a[title[0]]:
                    file.writerow([i])
                    for j, k in a[title[0]][i].items():
                        file.writerow([j, k])


if __name__ == "__main__":
    main()