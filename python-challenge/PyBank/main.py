# import modules
import os, csv

# set csv path
budget_csv = os.path.join("budget_data.csv")

# create lists to store values
month_count = []
net_amount = []
profit_change = []

# open and read csv
with open(budget_csv, newline="", encoding="utf8") as csv_file:
    # initialize (for computer use)
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_reader)
    
    
    # Total number of months
    for row in csv_reader:
        month_count.append(row[0])
     # Net total amount of Profit/Losses
        net_amount.append(row[1])
        

    # Average of changes in Profit/Losses

    # Greatest increase in profits (date and amount) over period

    # Greatest decrease in losses (date and amount) over period



# create output path
output_txt = os.path.join("newbudget.txt")

# open and write
with open(output_txt, "w", newline="", encoding="utf8") as txt_file:
    # initialize writer
    csv_writer = csv.writer(txt_file, delimiter=",")

    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["--" * 6])
    csv_writer.writerow(f"Total Months: {len(month_count)}")
    csv_writer.writerow(f"Total: {net_amount.sum()})
                        
