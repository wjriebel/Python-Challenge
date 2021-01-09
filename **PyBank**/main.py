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
max_index=change_profit_loss.index(greatest_profit)
min_index=change_profit_loss.index(greatest_loss)
# print(change_profit_loss.index(greatest_profit))
# print(total_months[max_index+1])
# print(total_months[min_index+1])
print('  ')
print('Financial Analysis')
print('---------------------------------')
print(f'Total Months: {len(total_months)}')
print(f'Total: ${sum(profit_loss)}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {total_months[max_index+1]} ${greatest_profit}')
print(f'Greatest Decrease in Profits: {total_months[min_index+1]} ${greatest_loss}')


# Set variable for output file
output_file = os.path.join("pybank_final.csv")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Financial Analysis'])
    writer.writerow(['---------------------------------'])
    writer.writerow([f'Total Months:{len(total_months)}'])
    writer.writerow([f'Total: ${sum(profit_loss)}'])
    writer.writerow([f'Average Change: ${round(average_change,2)}'])
    writer.writerow([f'Greatest Increase in Profits: {total_months[max_index+1]} ${greatest_profit}'])
    writer.writerow([f'Greatest Decrease in Profits: {total_months[min_index+1]} ${greatest_loss}'])
