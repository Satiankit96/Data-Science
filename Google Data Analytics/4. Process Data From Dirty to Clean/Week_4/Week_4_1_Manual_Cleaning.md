Verification - To verify if the cleaning process was correct or not.
Recheck
Manual cleaning
Take a big picture view - Think before the final commit  
Consider the data - Is it able to solve the issue or not. Check with others.

CASE statement

SELECT customer_id,
CASE 
    WHEN first_name = 'Tikna' THEN 'ANKIT'
    ELSE first_name
    END AS cleaned_name
FROM table