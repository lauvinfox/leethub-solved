# Write your MySQL query statement below
# SELECT name, population, area FROM world WHERE population >= 25000000 or area >= 3000000;
SELECT name, population, area
FROM World
WHERE area >= '3000000' OR population >= '25000000'