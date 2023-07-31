Course content

Course 4 – Process Data from Dirty to Clean 

1. Ensuring data integrity. 
   Data integrity is necessary to ensure a successful analysis. In this part of the course, you will explore methods and steps that analysts take to check data for integrity. This includes knowing what to do when you have an insufficient amount of data. You will also learn about sample size, avoiding sample bias, and using random samples. All of these measures also help to ensure a successful data analysis.

2. Understanding clean data. 
   Every data analyst wants clean data to work with when performing an analysis. In this part of the course, you will learn the difference between clean and dirty data. You will practice data cleaning techniques in spreadsheets and other tools.

3. Cleaning data using SQL. 
   Knowing a variety of ways to clean data can make an analyst’s job much easier. In this part of the course, you will use SQL to clean data from databases. You will explore how SQL queries and functions can be used to clean and transform your data before an analysis.

4. Verifying and reporting cleaning results. 
   Cleaning data is an important step in the data analysis process. In this part of the course, you will verify that data is clean and report data cleaning results. With verified clean data, you will be ready for the next step in the data analysis process.


Checkiung the Integrity of data. 

Reasons for the loss of integrity. 
1. Data Replication -IF data is saved in different locations then the data will not be in sync. (This means that the data would be updated differently in different locations)
   - Example - Continuing with the example, imagine you ask your international counterparts to verify dates and stick to one format. One analyst copies a large dataset to check the dates. But because of memory issues, only part of the dataset is actually copied. The analyst would be verifying and standardizing incomplete data. That partial dataset would be certified as compliant but the full dataset would still contain dates that weren't verified. Two versions of a dataset can introduce inconsistent results. A final audit of results would be essential to reveal what happened and correct all dates. 

2. Data Transfer - If there is an issue while transfering the data. 
   - Another analyst checks the dates in a spreadsheet and chooses to import the validated and standardized data back to the database. But suppose the date field from the spreadsheet was incorrectly classified as a text field during the data import (transfer) process. Now some of the dates in the database are stored as text strings. At this point, the data needs to be cleaned to restore its integrity. 


3. Data Manupulations - These are part of some human errors that can lead to an issue.
   - When checking dates, another analyst notices what appears to be a duplicate record in the database and removes it. But it turns out that the analyst removed a unique record for a company’s subsidiary and not a duplicate record for the company. Your dataset is now missing data and the data must be restored for completeness.
  
4. Other factors - Human error, Hacking, Viruses, Malware and System failures. 

Data Constraints  - https://www.coursera.org/learn/process-data/supplement/uWR9E/more-about-data-integrity-and-compliance


___________________________________________________________________________________________________________________________________________________________

Primary Goal 
Align business objective + Clean Data 

VLOOKUP - 
=VLOOKUP(search_key, range, index, [is_sorted])
Search key - Column index 
Range - Range of the colums 
Index - Of the column that will return the value of the range
is_Sorted - False - for exact matches 
True for estimate matches

Alignment to business objective + newly discovered variables + constraints = accurate conclusions

newly discovered variables + constraints - If we ever feel that the data is not complete align with the business needs. We can add a few more contraints for more accurate results. (Just a way to complete the data)