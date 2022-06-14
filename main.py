from calculations import StockDetails
from apirequests import getOverview
import sys
import csv


def main():

    # Assigns the company ticker to a variable 
    company = getCompany()

    # Creates variables for the methods from the StockDetails class
    stock = StockDetails(company)
    co = stock.companyOverview()
    ma = stock.marginAnalysis()
    pr = stock.profitabilityRatios()
    cfr = stock.cashFlowRatios()
    sr = stock.solvencyRatios()
    lr = stock.liquidityRatios()

    # Generates the screen results in terminal window
    getScreen(co, ma, pr, cfr, sr, lr)

    # Asks user if they wish to save the screen in a file and reprompts incase of an invalid input
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

    # Prompts user to input ticker, checks if the ticker is valid, and returns the ticker
    company = input("Enter Company Ticker (example: MSFT): ")
    while company == "" or len(company) > 5 or getOverview(company) == {}:
        print("Invalid Ticker")
        company = input("Enter Company Ticker (example: MSFT): ")
    return company


def getScreen(co, ma, pr, cfr, sr, lr):

    # Loop for printing out the results of the screen
    for a in [co, ma, pr, cfr, sr, lr]:

        # Assigning the main key in a variable to be used for indexing the dictionary
        title = list(a.keys())

        # Prints for formatting the output and printing the main key
        print()
        print(title[0])
        print()

        # Nested loop for printing out the sub keys which are values of the main key and formatting the output
        for i in a[title[0]]:
            print()
            print(i)
            print()

            # Nested loop for printing out the values of the sub keys in the dictionary
            for j, k in a[title[0]][i].items():
                print(j, k, sep="\t")


def saveScreen(company, co, ma, pr, cfr, sr, lr):

        # Saves the screen in a csv file through a loop
        with open(f"{company}.csv", "w", newline='') as f:
            file = csv.writer(f, delimiter=",")
            for a in [co, ma, pr, cfr, sr, lr]:

                # Assigning the main key in a variable to be used for indexing the dictionary
                title = list(a.keys())

                # Writes the main key
                file.writerow(title)

                # Nested loop for writing the sub keys which are values of the main key
                for i in a[title[0]]:
                    file.writerow([i])

                    # Nested loop for writing the values of the sub keys in the dictionary
                    for j, k in a[title[0]][i].items():
                        file.writerow([j, k])


if __name__ == "__main__":
    main()