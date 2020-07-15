-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- with conditions
SELECT id, name FROM cities
WHERE state_id = 
    (SELECT ID
    FROM states
    WHERE name = California);
