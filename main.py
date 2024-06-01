import random
import pickle

paper_list = []

# load data
inputFile = 'main.data'
fd = open(inputFile, 'rb')
paper_list = pickle.load(fd)
# print(paper_list) Check what papers are left in the list

papers_done = 35 - len(paper_list)
print(f"Past papers done: {papers_done}")

run = True
while run == True:
    if len(paper_list) == 0:
       print("You have finished all the past papers for this year\nHere is a past paper for your next year")
       paper_list = ["Abbotsleigh", "Ascham", "Barker", "Baulkham Hills", "Blacktown Boys", "Caringbah", "Cheltenham Girls", "Cherrybrook Tech", "Cranbrook", "Fort St", "Girraween", "Glenwood", "Gosford", "Hills Grammar", "Hornsby Girls", "Hunters Hill", "Hurlstone", "International Grammar", "James Ruse", "Killara", "Kinross Wolaroi", "Knox", "Manly", "Moriah", "Normanhurst Boys", "North Sydney Boys", "North Sydney Girls", "Penrith", "Pymble", "Shore", "St George Girls", "Sydney Boys", "Sydney Girls", "Sydney Grammar", "Sydney Tech"]

    else:
        run = False

# let x be a random number that corresponds to a random index in paper_list
x = random.randint(0, len(paper_list) - 1)
       
print(paper_list[x])
paper_list.pop(x)
# print(len(paper_list)) Check how many papers are left in the list

# store data
outputFile = 'main.data'
fw = open(outputFile, 'wb')
pickle.dump(paper_list, fw)
fw.close()

