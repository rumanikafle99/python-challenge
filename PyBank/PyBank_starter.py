# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data

#initializes the previous row to be none - at first there is no previous row 
prevValue = None

#Initializes list for differences in rows 
changesList = []

#Initializes list for tracking months 
months = [] 

maxInc = 0 
maxDec = 0 

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)


    # Process each row of data
    for row in reader:

        # Track the total months 
        total_months += 1 

        #Track the total of all months  
        column2 = float(row[1] ) #defines a variable for 2nd column 
        total_net += (column2)  
       
        # Track the net change - add the index one from row (totalNet += rowname)
        #(second row - first row) and add those values to list as you go
   
        if prevValue is not None: 
            changes = column2 - prevValue
            changesList.append(changes)

        #assigns prevValue to the value of current rows column 2 
        #returns None for first row but continues calculation for rest
        prevValue = column2

    # Calculate the greatest increase in profits (month and amount) 
    maxInc = max(changesList)
    if total_net >= maxInc: 
       greatesInc =  maxInc 
    

    # Calculate the greatest decrease in losses (month and amount)
    maxDec = min(changesList)
    if total_net <= maxDec: 
        maxDec 


# Calculate the average net change across the months

    sumChanges = sum(changesList) #Adds up values in changesList
    count = len(changesList) #Gets the count of the list
    averageList = sumChanges/count #performs the Average calculation


# Generate the output summary
outputSummary = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_net}\n"
    f"Average Change: {averageList:.2f}\n"
    f"Greatest Increase: {greatesInc}\n"
    f"Greatest Decrease: {maxDec}\n"

)


# Print the output to terminal
print(outputSummary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(outputSummary)
