import pandas as pd
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql_query("""SELECT * FROM sqlite_master
 WHERE type='table';""", conn)

print(tables)

matches = pd.read_sql("SELECT * FROM Match;", conn)
pd.set_option('display.max_columns', None)
print(matches.head())

result1 = pd.read_sql("""
SELECT AVG(Win_Margin) AS Avg_margin, Match_Winner
FROM Match
WHERE Season_Id = 9 
GROUP BY Match_Winner
ORDER BY AVG(Win_Margin)""", conn)
print(result1)

result2 = pd.read_sql("""
  SELECT COUNT(DISTINCT Venue_Id) AS venue_count
  FROM Match
  WHERE Season_Id = 9
  """, conn)   
print(result2)

result3 = pd.read_sql("""
    SELECT MIN(Win_Margin) AS min_margin,
    MAX(Win_Margin) AS max_margin,
    AVG(Win_Margin) AS avg_margin,
    COUNT(DISTINCT Man_of_the_Match) AS unique_mom_players
    FROM Match
    """, conn)
print(result3)

result4 = pd.read_sql("""
    SELECT SUM(Win_Margin) AS total_win_margin
    FROM Match
    WHERE Season_Id = 9
    """, conn)
print(result4)

# List all matches in Season 9 where the win margin was greater than 50
result5 = pd.read_sql("""
    SELECT *
    FROM Match
    WHERE Win_Margin > 50 AND Season_Id = 9
    """, conn)
pd.set_option('display.max_rows', None)
print(result5)