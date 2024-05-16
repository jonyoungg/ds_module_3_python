# Import required module
import csv
# Set path for the file
csvpath = "Resources/budget_data.csv"
#variables
month_count = 0
total_profit = 0
last_month_profit = None #used none instead of 0
changes = []
#open the csv (debugged using xpert)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print csv header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    #read each row of data after the header
    for row in csvreader:
        #add or equal 1 with month count
        month_count += 1
        #calculate total profit
        current_month_profit = int(row[1])
        total_profit += current_month_profit
        # calculate monthly changes #source (xpert)
        if last_month_profit is not None:
            change = current_month_profit - last_month_profit
            changes.append(change)
        #update last month's profit
        last_month_profit = current_month_profit
    #print results
    print(month_count)
    print(total_profit)
    #calculate and print average change
    #(debugged using xpert)
    if changes:
        avg_change = sum(changes) / len(changes)
        print(avg_change)


 # Find the greatest increase in profits
if changes:
    greatest_increase = max(changes)
    print(greatest_increase)
# Find the greatest decrease in profits
if changes:
    greatest_decrease = min(changes)
    print(greatest_decrease)



