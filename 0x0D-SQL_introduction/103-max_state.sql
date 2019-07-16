-- jba,dba
-- nalknda
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state;
