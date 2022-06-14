from calculations import StockDetails
from apirequests import getOverview
import re
import sys
import csv


def main():
    authenticate()
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


def authenticate():
    while True:
        userID = input("Username: ")
        if userID == "":
            print("Username cannot be blank!")
            continue
        elif not re.search("^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$", userID):
            print("Invalid Username!\nUsername must follow the following criteria:\n1. Username consists of alphanumeric characters (a-zA-Z0-9), lowercase, or uppercase.\n2. Username allowed of the dot (.), underscore (_), and hyphen (-).\n3. The dot (.), underscore (_), or hyphen (-) must not be the first or last character.\n4. The dot (.), underscore (_), or hyphen (-) does not appear consecutively, e.g., java..regex\n5. The number of characters must be between 5 to 20.")
            continue
        else:
            break
    while True:
        password = input("Password: ")
        if password == "":
            print("Password cannot be blank!")
            continue
        else:
            break
    with open("authentication.txt","r") as file:
        lines = file.readlines()
        totalcount = 0
        for line in lines[1:]:
            totalcount += 1
        while True:
            count = 0
            for line in lines[1:]:
                row = line.strip().split(",")
                if userID == row[0] and password == row[1]:
                    print("You've signed in successfully!")
                    return False
                elif userID != row[0]:
                    count += 1
                    if count == totalcount:
                        newuserID = input("That username does not exist, would you like to create a new user by that name? (Y/N): ")
                        while newuserID not in ["Y", "N"]:
                            newuserID = input("That is not an input, please try again! \nWould you like to create a new user by that name? (Y/N): ")
                        if newuserID == "Y":
                            with open("authentication.txt", "a") as file:
                                while True:
                                    newpassword = input("Please enter your password?: ")
                                    if not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,32})", newpassword):
                                        print("Invalid Password!\nPassword must follow the following criteria:\n1. At least one digit [0-9]\n2. At least one lowercase character [a-z]\n3. At least one uppercase character [A-Z]\n4. At least one special character [*.!@#$%^&(){}[]:;<>,.?/~_+-=|\]\n5. At least 8 characters in length, but no more than 32.)")
                                        continue
                                    else:
                                        break
                                file.write("\n" + userID + "," + newpassword)
                                sys.exit("New username and password registered, please run the program again!")
                        else:
                            sys.exit("Try running program again with the right username!")
                    else:
                        continue
                elif password != row[1]:
                    password = input("Invalid password! Please try again! \nPassword: ")
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
