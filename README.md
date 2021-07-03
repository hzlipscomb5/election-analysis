# Election-Analysis

## Overview of Election Audit
**We've been asked to complete the following tasks to audit a recent Colorado congressional election**
1. Calculate the total number of votes cast
2. Get a complete list of the candidates who received votes
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the total votes from each county
7. Calculate the percentage of the total votes that came from each county.
8. Determine the county from which the most votes came from

## Resources
- Data Source: election_results.csv
- Software Python 3.8.10, Visual Studio Code, 1.57

## Election Audit Results
**The Grand Total of Votes Cast in the Election:**
- 369,711 Total Votes Cast

**Percentage of Total Votes and Vote Count by County**
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

**County with Largest Vote Count**
- Denver

**Three Candidates Received Votes:**
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane

**Candidate Results:**
- Charles Casper Stockham received "23%" of the votes "85,213" number of votes
- Diana DeGette  received "73.8%" of the votes "272,892" number of votes
- Raymon Anthony Doane received "3.1%" of the votes "11,606" number of votes

**The Winner of the Election was:**
- Diana DeGette received "73.8%" of the total votes and "272,892" votes in all.

## Election Audit Summary
The script used in this election audit could be modified for nearly any election. With only minor tweaks, this code could be repurposed for another election decided by the "popular vote". The first requisite adjustment would be to edit the path that the underlying data was retrieved from. This snippet of code currently reads: `file_to_load = os.path.join("Resources", "election_results.csv")`.  To adjust this code to load the proper data, the new data file should be saved to the "Resources" folder and replace the "election_results.csv" filename with new database's filename. Another potentally neccesary tweak to the script, would be to change the column number that is referenced in each row of the "for loop" that gathers the candidate names and the county names. This change would be neccesary, if the layout of the data was different than the current data file's layout. The most drastic changes to the code would be neccesary if it were repurposed to calcuate an election decided by electoral votes or by ranked choice voting. Electoral vote tabulation would require fifty separate state tabulations. The winner of each state would be awarded a value representing the electoral votes for that state. Once the states are decided, these electoral votes would be tallied to crown the winner of the election. Ranked choice voting would be significantly more challenging. This would involve an elaborate collection of decision statements; when a candidate's victory is deemed impossible that candidate would be removed from contention, and this would trigger an operation that redistributes their votes to the next active candidate in each voter's rankings. 