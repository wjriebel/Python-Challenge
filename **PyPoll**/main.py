import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('Resources', 'election_data.csv')

# Open CSV and read
with open(pypoll_csv, 'r') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the first line
    header = next(csvreader)

    # declaring my list and variables
    canidate_list = []
    candidate_copy = []

    # For Loop to fill lists
    for row in csvreader:
        candidate_copy.append(row[2])
    candidate_list =set(candidate_copy) # remove duplicates using set properties
    candidate_list = list(candidate_list) # convert to list
    number_of_candidates = len(candidate_list) # number of candidates

    # Total number of votes cast
    total_votes = len(candidate_copy)
    print('')
    print('Election Results')
    print('---------------------')
    print('Total Votes:   ' + str(total_votes))
    print('---------------------')

    # Store Candidates and Votes to Dictionoary
    pypoll = {}

    # For Loop to go through dictionary
    for i in range(number_of_candidates):
        pypoll[candidate_list[i]] = candidate_copy.count(candidate_list[i])

        #print vote count for eacah candidate
        (float(pypoll[candidate_list[i]])/total_votes*100)
        print("")
        print((candidate_list[i])+'  '+str(float(pypoll[candidate_list[i]])/total_votes*100))
        print((pypoll[candidate_list[i]]))
        print("----------------------")
        #iterate through dictionary
        #have a placeholder for Max
        poll_win = 0

        for x, y in pypoll.items():
            if y > poll_win:
                poll_win_vote_count = y
                poll_win_name = x

print("")
print("------------------------")
print("Winner!:")
print(f'{poll_win_name}')
print("------------------------")
print("")

    #iterate through dictionary (make placeholder for max)
    #for x, y in pypoll.items():
    #poll_vote_list = (pollvote_list[1])
    #print(poll_vote_list[1])



# Set variable for output file
output_file = os.path.join("pypoll_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Election Results'])
    writer.writerow(['---------------------'])
    writer.writerow([''])
    writer.writerow([(candidate_list[i])+'  '+str(float(pypoll[candidate_list[i]])/total_votes*100)])
    writer.writerow([(pypoll[candidate_list[i]])])
    writer.writerow(['----------------------'])


