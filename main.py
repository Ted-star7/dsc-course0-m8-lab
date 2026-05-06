# Introduction

#In this lab assessment you will explore writing more advanced SQL queries aimed at analyzing data on a more granular level. You will be working with 3 different databases throughout the assessment.
#planets.db: Contains data pertaining to planets in our solar system
#dogs.db: Contains data pertaining to famous fictional dog characters
#babe_ruth.db: Contains data pertaining to Babe Ruth's baseball career statistics

#SQL (Structured Query Language) provides powerful tools for manipulating and analyzing data in relational databases. Four key operations for working with data are filtering, ordering, limiting, and grouping. These operations can be combined in a single query to perform complex data analysis and extraction tasks, allowing for powerful and flexible data manipulation.
# Learning Objectives

#Retrieve a subset of records from a table using a WHERE clause
#Filter results using conditional operators
#Apply an aggregate function to the result of a query
#Order the results of your queries by using ORDER BY (ASC & DESC).
#Limit the number of records returned by a query using LIMIT.
#Use Group BY statements in SQL to apply aggregate functions.
#Part I: Basic Filtering

#You will begin by looking at the planets data to perform some basic filtering queries

#Table Name: planets
# CodeGrade step0

# Run this cell without changes

import pandas as pd
import sqlite3

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)
### Step 1
#Return all the columns for planets that have 0 moons.
# CodeGrade step1
# Replace None with your code
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons = 0
""", conn1)
df_no_moons
#Step 2
#Return the name and mass of each planet that has a name with exactly 7 letters. Avoid hard coding this filter subset as much as possible.
#CodeGrade step2
#Replace None with your code
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7
""", conn1)
df_name_seven
#Part 2: Advanced Filtering
#Step 3

#Return the name and mass for each planet that has a mass that is less than or equal to 1.00.
#CodeGrade step3
#Replace None with your code
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00;
""", conn1)
df_mass

#Step 4

#Return all the columns for planets that have at least one moon and a mass less than 1.00.
# CodeGrade step4
# Replace None with your code
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1 AND mass < 1.00;
""", conn1)
df_mass_moon
### Step 5

#Return the name and color of planets that have a color containing the string "blue".
#CodeGrade step5
#Replace None with your code
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%'
""", conn1)
df_blue
##Part 3: Ordering and Limiting
#This database has some fictional, yet generally famous, dogs.

## Table Name: dogs
# CodeGrade step0

# Run this cell without changes

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)
### Step 6
## Return the name, age, and breed of all dogs that are hungry (binary flag of 1) and sort them from youngest to oldest.
# CodeGrade step6
# Replace None with your code
df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC
""", conn2)
df_hungry
### Step 7
## Return the name, age, and hungry columns for hungry dogs between the ages of two and seven. This query should also sort these dogs in alphabetical order.
# CodeGrade step7
# Replace None with your code
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC
""", conn2)
df_hungry_ages
### Step 8

## Return the name, age, and breed for the 4 oldest dogs. Sort the result alphabetically based on the breed.
# CodeGrade step8
# Replace None with your code
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4
""", conn2)
df_4_oldest = df_4_oldest.sort_values('breed').reset_index(drop=True)
df_4_oldest
## Part 4: Aggregation
##In the next few parts, you'll query data from a table populated with Babe Ruth's career hitting statistics. You'll use aggregate functions to pull interesting information from the table that basic queries cannot track.

##Table Name: babe_ruth_stats
# CodeGrade step0

# Run this cell without changes

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)
### Step 9

##Return the total number of years that Babe Ruth played professional baseball
# CodeGrade step9
# Replace None with your code
df_ruth_years = pd.read_sql("""
    SELECT COUNT(year) AS total_years
    FROM babe_ruth_stats
""", conn3)
df_ruth_years

### Step 10

#Return the total number of homeruns hit by Babe Ruth during his career.
# CodeGrade step10
# Replace None with your code
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) AS total_homeruns
    FROM babe_ruth_stats
""", conn3)
df_hr_total
## Part 5: Grouping and Aggregation
### Step 11

#For each team that Babe Ruth has played on, return the team name and the number of years he played on that team, aliased as 'number_years'.
# CodeGrade step11
# Replace None with your code
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(year) AS number_years
    FROM babe_ruth_stats
    GROUP BY team
""", conn3)
df_teams_years
### Step 12

#For each team that Babe Ruth played on and averged over 200 at bats with, return the team name and average number of at bats, aliased as 'average_at_bats'.
# CodeGrade step12
# Replace None with your code
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING AVG(at_bats) > 200
""", conn3)
df_at_bats
#### Close the connections
# Run this cell without changes

conn1.close()
conn2.close()
conn3.close()