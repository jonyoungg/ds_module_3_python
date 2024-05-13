import csv

# csv file
csvpath = "Resources/election_data.csv"

# Variables to store total votes and candidate votes
total_votes = 0
candidate_votes = {}

# Open the csv (github reference)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

    # go through each row in csv
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # count votes for each candidate
        candidate = row[2]
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# output (using xpert)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# calculate percentage (using xpert)
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# find the winner
winner = max(candidate_votes, key=candidate_votes.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

