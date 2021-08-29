# The data we need to retrieve.

# Add our dependencies (i.e. import os and csv modules)
import os
import csv

# Assing a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read and analyze data.

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)





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



