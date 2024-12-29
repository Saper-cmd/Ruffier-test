import pandas as pd

# Uploading dataframe 
df = pd.read_csv('GoogleApps.csv')


# What is the name of the first application containing in the dataset?
    
    #Photo Editor & Candy Camera & Grid & ScrapBook

# What is the category of the last application containing in the dataset?
    #LIFESTYLE

# How many columns are there in the dataset?

    #12

# What is the type of data stored in each column?
    #int ; str ;float



# Specify the arithmetic mean and median for the size of the applications.
a= df["Size"].median()
print(a)
d= df["Size"].mean()
print(d)


# How much does the most expensive application cost?
e = df["Price"].max()
# *Specify the arithmetic mean and median for the number of application installs.
b= df["Installs"].median()
print(b)
c= df["Installs"].mean()
print(c)