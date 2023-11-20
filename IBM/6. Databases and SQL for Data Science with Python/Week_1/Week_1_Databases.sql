SQL Basics - Just a refresher 
- Count (The country count)
SELECT COUNT(Country)
FROM Medals
Where Country = 'CANADA'

SELECT DISTINCT Country 
FROM Medals
WHERE MedalType = 'Gold' 

Question 1 
SELECT COUNT(*)
FROM FilmLocations
WHERE Locations = 'Russian Hill';

SELECT COUNT(*)
FROM FilmLocations
WHERE ReleaseYear < 1950;


Question 2 -  Distinct 
SELECT DISTINCT Title, Director
FROM FilmLocations
WHERE Locations = 'City Hall' ;

SELECT COUNT(DISTINCT Distributor)
FROM FilmLocations
WHERE Actor1 = 'Clint Eastwood' ;

SELECT COUNT(DISTINCT Distributor)
FROM FilmLocations
-- CHEAT SHEET
-- https://www.coursera.org/learn/sql-data-science/ungradedWidget/JGZSf/sql-cheat-sheet-basics-select-insert-update-delete-count-distinct-limit

-- Quiz 1 -100
-- Quiz 2 -100


