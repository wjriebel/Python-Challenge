import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join('Resources', 'budget_data.csv')
# declaring my list and variables
total_months = []
profit_loss = []
change_profit_loss = []

# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        total_months.append(row[0])
        profit_loss.append(int(row[1]))
    
    for i in range (1, len(profit_loss)):
        change_profit_loss.append(profit_loss[i]- profit_loss[i - 1])
        average_change = sum(change_profit_loss) / len(change_profit_loss)


        greatest_profit = max(change_profit_loss)
        greatest_loss = min(change_profit_loss)
print(f'total months:{len(total_months)}')
print(f'total profit loss:${sum(profit_loss)}')
print(f'average change:$ {round(average_change,2)}')
print(f'greatest increase in profit is: ${greatest_profit}')
print(f'greatest loss in profit is: ${greatest_loss}')

# Set variable for output file
output_file = os.path.join("pybank_final.csv")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Financial Analysis'])
    writer.writerow([f'total months:{len(total_months)}'])


