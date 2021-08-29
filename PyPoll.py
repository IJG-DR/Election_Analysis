# The data we need to retrieve.

# Add our dependencies (i.e. import os and csv modules)
import os
import csv

# Assing a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Initialize a counter for the total number of votes
candidate_options =[]

# Initialize a dicitonary to hold the votes for each candidate.
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read and analyze data.

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # For each row in the CSV file.
    for row in file_reader:
        
        # 2. Add to the total vote count.
        total_votes += 1        
        
        # Read the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate, then add it to the list of running option
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the list of running options.
            candidate_options.append(candidate_name)

            # Begin tracking the added candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's vote count.
        candidate_votes[candidate_name] +=1

# 3. Print the total votes.
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) *100
    
    # TO DO: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = float(winning_count) / float(total_votes) * 100
        # Set the winning_candidate equela to the candidate's name
        winning_candidate = candidate_name
    
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

    # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")




# ## OUTPUT BLOCK
# ## Method 1
# ## Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")

# ## Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# ## Write some data to the file.
# outfile.write("Hello World")

# ## Close the file
# outfile.close()


## OUTPUT BLOCK
## Method 2 (cleaner)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Hello World")

     # Write three counties to the file.
     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# csvreader = csv.reader(data_in_csvfile, delimiter=',')

#1. The total number of votes cast.


#2. A complete lis of candidates who received votes.


#3. The percentage of votes each candidate won.



#4. The total numbe of votes each candidate won.



#5. The winner of the election based on popular vote.



