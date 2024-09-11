import pandas as pd #Pandas Read CSV
import os # so i dont list data/ each time ill join directory with os

#directory of my data
data_directory = 'data'

#list like an array and has similaer methods in py
files = [
      'credits.csv',
    'keywords.csv',
    'links_small.csv',#cant read
      'links.csv',
    'movies_metadata.csv',
    'ratings_small.csv',
    'ratings.csv'
]


#define a function to retrun cols
def get_columns(file_path):
    try:
        dataFrame = pd.read_csv(file_path, nrows=1)#read file , just first row to get cols
        return dataFrame.columns.tolist() #cols names of the DataFrame,.tolist(): Converts the column names into a Python list
    except FileNotFoundError:
        return "File not found: " + file_path

    


# loop over each file and print the column names
for fileName in files:
    filePath = os.path.join(data_directory, fileName)
    columns = get_columns(filePath)
    print(fileName + " Columns: " + str(columns)) #its coming as a list cant concat unless str