# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidateList = []

#Initializes dictionary to count the number of votes - Key = Candidate Name, Value = Count
candidateCount = {}

# Winning Candidate and Winning Count Tracker
winningCount = 0
winner = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        #print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1 

        # Get the candidate's name from the row
        candidateName = row[2]
        

        # check to see if the candidate  is in candidateList and if not add it 
        if candidateName not in candidateList:
            candidateList.append(candidateName )

            #add the value to dictionary ("key" : Value)
            candidateCount[candidateName ] = 1  #starts the count of at 1 
        else: 
            # Add a vote to the candidate's count
             candidateCount[candidateName] += 1 

#initializes output
output = ""

# Loop through the candidates to determine vote percentages and identify the winner
for candidateList in candidateCount: 
     # Get the vote count and calculate the percentage
    votes = candidateCount.get(candidateList)
    votePercent = (float(votes)/float(total_votes)) * 100 

    # Print and save each candidate's vote count and percentage
    output += f"{candidateList}: {votePercent:.3f}% ({votes}) \n"

    #compare vote to winning count
    if votes > winningCount: 
        winningCount = votes
        Winner = candidateList

#Winner Output
WinnerOutput = f"Winner: {Winner}"


#Prints out the output summary 
outputText = (
    f"\nElection Results \n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{output}"
    f"-------------------------\n"
    f"{WinnerOutput}\n"
    f"-------------------------\n"

)

#Prints the output text in text file
print(outputText) 



# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Save the winning candidate summary to the text file
    txt_file.write(outputText)


