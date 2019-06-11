# import modules
import os, csv

# set csv path
csv_path = os.path.join("election_data.csv")

# create lists to store values
candidates = []
vote_percentage = []
vote_count = []
unique_candidate = []
counter = 0


# open and read csv file
with open(csv_path, newline="", encoding="utf8") as csv_file:
    # initialize and read
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skips header
    csv_header = next(csv_reader)

    # total candidates
    for row in csv_reader:
        candidates.append(row[2])
        counter += 1
        
    # find unique list of candidates
    for unique_number in candidates:
        unique_candidate.append(unique_number)

        # find total votes
        total_votes = candidates.count(unique_number)
        vote_count.append(total_votes)

        # find vote percentage
        total_percentage = (total_votes/

    # winner
    winner = vote_count.max()

# print results
print("----------------------------")
print("Election Results")
print(-----------------------------")
print(f"Total Votes: {len(candidates)]")


# set csv path
output_txt = ("new_election_data.txt")

# open and write txt file
with open(output_txt, "w", newline="", encoding="utf8") as txt_file:
      # initialize
      csv_writer = csv.writer(txt_file, delimiter=",")

      # write data into txt file
      csv_writer.writerow("----------------------------")
      csv_writer.writerow("Election Results")
      csv_writer.writerow(-----------------------------")
      csv_writer.writerow(f"Total Votes: {len(candidates)]")
      
        
        

    
        
    
