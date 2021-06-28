#The Data We need to retrieve
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes


#Using Datetime Module
#Import the datetime class from datetime module
import datetime
#Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
#Print the present time
print("The time right now is", now)

#To shorten you could use an abbreviated alias for datetime
import datetime as dt
now = dt.datetime.now()
print("The time right now is", now)

#Opening a CSV file
#Assign a variable for the file to load and the path
file_to_load= 'Resources/election_results.csv'

#Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

#To Do: Perform Analysis

#Close the File
election_data.close()

#Indirect Path
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


#import os first
#Write a File to Directory on Computer
#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")
#there must be a folder named "analysis" for this to not have an IO error

#import os first
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

#always import OS first!!
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

#Use txt_file.write("Arapahoe")  to add arapahoe denver and jefferson
txt_file.write("Arapahoe")

#above has no spaces or commas and we must add them manually
txt_file.write("Arapahoe, ")

#add all 3 by joining on same line
txt_file.write("Arapahoe, Denver, Jefferson")

# To do on separate lines do "new line escape" /n

txt_file.write("Arapahoe\nDenver\nJefferson")

#Or add some formatting
txt_file.write("-------------------------\nArapahoe\nDenver\nJefferson")


#Time to Read the Election Results
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Read the file object with the reader function(Reader function found in CSV Module)
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
    for row in file_reader:
        print(row)

# Ex: Print first row      
     for row in file_reader:   
        print(row[0])
 

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row. #We can skip the first row(header) w/next()/ Printing them to make sure its the headers
    headers = next(file_reader)
    print(headers)

   
   

  ####FULL CODE BLOCK CURRENTLY 
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)