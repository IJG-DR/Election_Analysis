# Election Analysis

## Project Overview

Tom, an employee of the Colorado Board of Elections, has asked us to assist him in an election audit of the tabulated votes for a U.S. congressional district in Colorado. Our task includes reporting:

* Total number of votes cast.
* A complete list of candidates who received votes.
* Total number of votes for each candidate.
* Percentage number of votes for each candidate.
* The winner of the election based on popular vote.

Tom's manager, Seth, hopes to use the python code we develop to automate the audit process not only for other congressional districts but also for senatorial districts and local elections. To complete the audit, the Colorado Board of Elections commission has requested additional data, which include:

* The voter turnout for each county.
* The percentage of votes from each county out of the total count.
* The county with the highest turnout.

## Methodology

We have been provided with the tabulated election results in a comma delimited text file (csv file). The data is included in the file *election_results.csv*.

Using Python, we created code to read the data-file and sift through the data to capture the information of interest for the electoral commission. This was achieved using *if* conditionals, *for* loops, *lists* and *dictionaries* to hold the data, and calls to files to open the data and write the results to a text file with the results. The code and working files were uploaded to a GitHub repository for easy access by the electoral commission. The audit results are contained in the file *election_results.txt* located in the *Analysis* folder of the GitHub repository.

## Election Audit Results 

Running our Python code on the data file, we were able to obtain the following results which address the objectives required by the electoral board.

* The election produced a total of 369,711 casted votes.
* The election was conducted in three counties:
    - Jefferson
    - Denver
    - Arapahoe
* The total number of votes and percentage of votes cast in each county is shown in the print readout of our Python program as seen below:

![Printout of votes by county.](Resources/Votes_by_County.png)

* With 82.8% of the total votes, Denver was the county with the largest number of votes.
* Three candidates ran for election: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
* The total number of votes and percentages cast for each candidate is shown in the print readout of our Python program as shown below:

![Printout of votes by candidate.](Resources/Candidate_Results.png)

* With 272,892 votes representing 73.8% of total votes cast, Diana DeGette was the winning candidate.

The final report produced by our code printed in terminal as follows:

![Printout in terminal of final results.](Resources/Terminal_printout.png)

And the information was recorded in a text file as follows:

![Text file of final results.](Resources/Final_election_results.png)


## Election Audit Summary: 

By automating the election audit with Python code, it is easy to apply the same methodology to future elections or to other elections, providing for an efficient and timely process. With minor modifications, the code can be used to capture other important data or to handle a different set of conditions.

For example, the code can be modified to tally votes not only for running candidates, but also for which office they are running, if the election involves more than one office (for example, secretary or vice-president). Also, the code can be modified to cover the election for the whole state (or for the whole country), by tallying totals for all counties to determine the results at the state level, or further tallying the votes for all states to determine the results at the national level.