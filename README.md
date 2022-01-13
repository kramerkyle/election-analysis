# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
 - Data Source: election_results.csv
 - Software: Python 3.7, Visual Studio Code

## Summary
### Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The county results were as follows:
  - Arapahoe County filed 24,801 votes, which represented 6.7% of the total.
  - Jefferson County filed 38,855 votes, which represented 10.5% of the total.
  - Denver County filed the most votes at 306,055 votes, which represented 82.8% of the total.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.

The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 votes.

### Methodology
The script works by first importing csv and os dependencies. After initializing a total vote counter, empty lists and dictionaries are initiated for candidate options, candidated votes, county options, and county votes.

![Step 1](https://github.com/kramerkyle/election-analysis/blob/f87fa7f49007b7d1a41d1d4af4ddb7862c7927ba/Election-Analysis-Step-1.png)

After this, we import the election_data.csv, and extract the candidate name and county row. The script appends the candidate name and the county name to the appropriate list if they weren't previously present. Regardless of the prior status, the script adds to the appropriate counters.

Following the for and if statements, the script prints the results to a text file. The last thing printed to the terminal is the winning candidate summary. This summary includes the winning candidate, their winning count, and the percentage of the votes that the candidate won.

![Summary](https://github.com/kramerkyle/election-analysis/blob/main/Election-Analysis-Summary.png)

The broader text file results and python code are available within this repository.

### Sustainability
This analysis can be used in any election through simple adjustments. City elections could use this script by altering counties into precincts. Another modification of the script that would widen its applicability is by introducing another if statement that enables ranked voting to be implemented.
