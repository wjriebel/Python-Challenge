import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('Resources', 'election_data.csv')
# declaring my list and variables

# Read in the CSV file
with open(pypoll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Loop through the data







# Set variable for output file
output_file = os.path.join("pypoll_final.csv")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
   
