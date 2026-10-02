from pathlib import Path

# __file__ -> absolute path to this script
# .parent -> parent directory of this script 
# / "data" -> add this directory to the path
DATA_PATH = Path(__file__).parent / "data"

#print(DATA_PATH)

#print("Reading a file")

# open up quotes.txt and print it 
with open(DATA_PATH / "quotes.txt") as file:
    print(file.read())