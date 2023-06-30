import os
import csv

# Change the current directory to 'Resources'
os.chdir('Resources')

# Define the path to the CSV file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

totalVotes = 0  # Total number of votes (excluding the header)

# Dictionary to store the votes per candidate
# votesPerCandidate = {
#   "candidate_one": votes as an integer
# }
votesPerCandidate = {}

# Open the 'election_data.csv' file
with open("election_data.csv", newline='') as csvfile:

    # Create a CSV reader object with ',' as the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1

print("Election Results")
print("-"*50)
print("Total Votes: " + str(totalVotes))
print("-"*50)

# Print the percentage of votes and the total votes for each candidate
for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" + str(votes) + ")")

print("-"*50)

# Determine the candidate with the highest number of votes
winner = max(votesPerCandidate, key=votesPerCandidate.get)

print(f"Winner: {winner}")


# Export the results to a text file 
outputfile = 'analysis_summary.txt'
with  open(outputfile, 'w') as output:
    output.write("Election Results\n")
    output.write("-"*50 + "\n")
    output.write(f"Total Votes: {totalVotes}\n")
    output.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" + str(votes) + ")")
    output.write("-"*50 + "\n")
    output.write(f"Winner: {winner}")