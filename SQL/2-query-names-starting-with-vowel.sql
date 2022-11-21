--Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

/*
Enter your query here.
*/

SELECT DISTINCT city FROM station WHERE LEFT(city, 1) IN ('A', 'E', 'I', 'O', 'U');