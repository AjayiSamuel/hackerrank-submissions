--Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
--
--Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
--
--Input Format
--
--The CITY and COUNTRY tables are described as follows:

/* Given two tables, City and Country whose descriptions are given below. Find the sum of population of all the Cities that lies in "Asia" continent.
City
*/
+-------------+----------+
| Field       | Type     |
+-------------+----------+
| ID          | int(11)  |
| Name        | char(35) |
| CountryCode | char(3)  |
| District    | char(20) |
| Population  | int(11)  |
+-------------+----------+
Country
+----------------+-------------+
| Field          | Type        |
+----------------+-------------+
| Code           | char(3)     |
| Name           | char(52)    |
| Continent      | char(50)    |
| Region         | char(26)    |
| SurfaceArea    | float(10,2) |
| IndepYear      | smallint(6) |
| Population     | int(11)     |
| LifeExpectancy | float(3,1)  |
| GNP            | float(10,2) |
| GNPOld         | float(10,2) |
| LocalName      | char(45)    |
| GovernmentForm | char(45)    |
| HeadOfState    | char(60)    |
| Capital        | int(11)     |
| Code2          | char(2)     |
+----------------+-------------+
PS: City.CountryCode and Country.Code is same key.
*/

SELECT SUM(I.population) FROM city I LEFT JOIN country O ON I.countrycode = O.code WHERE O.continent = 'Asia';
--OR
--SELECT SUM(I.population) FROM city AS I INNER JOIN country AS O ON I.countrycode = O.code WHERE O.continent = 'asia';