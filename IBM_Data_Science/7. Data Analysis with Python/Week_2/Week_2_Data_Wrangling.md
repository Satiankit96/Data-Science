Data Cleaning 
- This is also known as Wrangling 
<!-- https://www.coursera.org/learn/data-analysis-with-python/ungradedWidget/xZKrQ/module-2-cheat-sheet-data-wrangling -->
Tasks 
- Handle missing Values 
- Data Formatting
- Data normalisation (Scalling of the data)
- Data Binning
- Categorical to statistical 

1. Handle missing Values
- Check the original source of data 
- Drop the variable 
- Drop the data entry 
- Replace it with average 
- Replace with mode(Frequency)
- Replace it with other functions 
- LEAVE IT AS IT IS 

2. Data Formatting '
- Different represent for an entity in a cell.
- Incorrect dtypes(df.dtypes).  Conversion - df["Price"] = df["Price"].astype("int")

3. Data normalisation (Central data) - Manage the influence of variables on the models
- Defining a range for the data to fall in 
- To manage the ijmpact on data 
- a. Simple feature 
- b. Min Max
- c. Z score

4. Binning 
- Putting Values in a data range (age 18-24)
- more in .py

5. Categorical to statistical
- Setting a word to 0/1(Gas/Diesel)