-- Script that lists all cities contained in the database hbtn_0d_usa
-- You can use only one SELECT statement
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states_id;
