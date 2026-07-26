import pandas as pd
import string

#series = a pandas 1D labeled array 
#data = [100, 102, 104, 109, 5, 6]
#data2 = {"day1": 10, "day2": 20, "day3": 23}
#index = list(string.ascii_lowercase[:len(data)])

#series = pd.Series(data, index=index)
#print(series)

# locating values in a letter-indexed series
#print(series.loc["c"])

# separate series for dict data
#series2 = pd.Series(data2)
#print(series2.loc["day3"])

# update a value in the dict-based series
#series2.loc["day2"] += 2
#print(series2.loc["day2"])

#dataframe = tabular data structure w rows and coloums(2D)
#data = {"name": ["sponge", "patric", "squid"],
        #"age": [30, 35, 50]}

#df = pd.DataFrame(data)  # can use iloc by indexing dataframe similar to in series(line 9)

# add new row with ignore_index=True so the row label is sequential
#new_row = pd.DataFrame([{"name": "sandy", "age": 28, "job": "engineer"}]) # to add more rows, add more dicts within the list
#df = pd.concat([df, new_row], ignore_index=True)

# add job column values for every row in df
# now there are 4 rows, so the list must also have 4 values
#df["job"] = ["cook", "new", "cashier", "engineer"]
#print(df)

df = pd.read_csv("customerscsv.csv")
#print(df.to_string())

#for selection by col
#print(df["first_name"].to_string())
#for multiple: just add more coloumns within the list right after df

#for selection by row
#print(df.loc[1])

#use set_index to set diff coloumns as index to use their data for locs

#print(df.iloc[0:11:2, 0:3]) the 0:11 is just selecting first 10 rows, the :2 selects every SECOND row, the 0:3 selects the first 3 coloumns

#user input for selection
#df = df.set_index("first_name")
#name = input("enter name: ")
#try:
#    print(df.loc[name])
#except KeyError:
#    print(f"{name} not found")

#filtering = keeping rows that match a condition
#country = df[df["country"] == "USA"]
#print(country)

#aggregate func = reduce a set of values into a single summary value
#print(df.mean(numeric_only=True)) #this is for the whole dataset

#for single coloumn
#print(df["customer_id"].mean())

#using group by objects
#group = df.groupby("first_name")
#print(group["customer_id"].mean())

#data cleaning
#df = df.drop(coloumns=["last_name"]) #drops the coloumn
#df = df.dropna(subset=["country"]) dropna = drop rows with missing data. use subset for particular coloumn
#df = df.fillna({"first_name": "None"}) fillna = replace missing values with "none" in that particular coloumn

#fixing inconsistent values
#df["last_name"] = df["last_name"].replace({"grass": "GRASS"}) #replace all values of "grass" found in coloumn last_name with "GRASS"

#standardize text
#df["first_name"] = df["first_name"].str.lower() this lowercases all str values in first_name.

#use astype() to fix data types

#remove duplicates by
#df = df.drop_duplicates()