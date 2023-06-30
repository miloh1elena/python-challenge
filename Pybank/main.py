# Change the current directory to 'Resources' to locate the CSV file
import os
import csv 

# Define the path to the CSV file
os.chdir('Resources')

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Variables for analysis

Total_Months = 0
Total = 0
Profits_Losses = []
Months_List = []
Monthly_Changes = []

# Read the CSV file

with open("budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
# Calculate total months, net total, and store data in lists
    for row in csvreader:
        Total_Months += 1
        Total += int(row[1])
        Profits_Losses.append(row[1])
        Months_List.append(row[0])

# Find the starting point for calculations

firstProfits_Losses = int(Profits_Losses[0])

# Calculate monthly changes

for i in range(1, len(Profits_Losses)):
    Monthly_Changes.append(int(Profits_Losses[i]) - firstProfits_Losses)
    firstProfits_Losses = int(Profits_Losses[i])
    i += 1
# Calculate average change
AvgChange = round(int(sum(Monthly_Changes)) / int(len(Monthly_Changes)), 2)

# Find greatest increase and decrease in profits
MaxIncrease = max(Monthly_Changes)
MaxDecrease = min(Monthly_Changes)

# Find corresponding months for greatest increase and decrease

for i in range(len(Monthly_Changes)):
    if Monthly_Changes [i] == MaxIncrease:
        maxIndex = (i + 1)
    elif Monthly_Changes[i] == MaxDecrease:
        minIndex = (i + 1)
    else:
        i += 1

MaxMonth = Months_List[maxIndex]
MinMonth = Months_List[minIndex]

# Print the analysis results

print("Financial Analysis")
print("-"*50)
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${AvgChange}")
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")

# Export the results to a text file
outputfile = 'analysis_summary.txt'
with  open(outputfile, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-"*50 + "\n")
    output.write(f"Total Months: {Months_List}\n")
    output.write(f"Total: ${Total}\n")
    output.write(f"Average Change: ${AvgChange}")
    output.write(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})\n")
    output.write(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
