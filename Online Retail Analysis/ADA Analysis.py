import sys
import csv

customers = []
goods = []

with open('Data Sets/Online Retail CSV File.csv', "r+", encoding="Latin1") as inputFile:
    csvReader = csv.reader(inputFile, dialect='excel')
    for row in csvReader:
        print("Running Search")

        # Get all customers
        if row[0] not in customers:
            if row[0][0] != "C":
                customers.append(row[0])
                print("Added new customer")
            else:
                print("Cancelled")

    # RESULTS
    print("Customer Invoice List: ", customers)
    print("NUM CUSTOMERS?UNIQUE INVOICES: ", len(customers)-1)



