import sqlite3
database = 'database (1).sqlite'
conn = sqlite3.connect(database)
print("Database connected successfully")

import pandas as pd
tables = pd.read_sql(""" 
SELECT  * FROM sqlite_master WHERE type ='table';
""",conn )
print (tables)

match_details = pd.read_sql("""  
SELECT Match_Id , Team_Name as Match_Winner
FROM Match
INNER JOIN Team
ON Match.Match_winner==Team.Team_Id                          
""",conn)
print (match_details)

result =pd.read_sql("""
SELECT Season_Id,Man_of_the_Series
FROM Season
WHERE Man_of_the_Series
IN (SELECT Player_Id
FROM Player WHERE Country_Name=1);
 """,conn)
print (result)
