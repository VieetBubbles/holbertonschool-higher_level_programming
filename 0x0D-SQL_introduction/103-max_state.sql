-- jba,dba
-- nalknda
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY MAX(value) DESC LIMIT 3;
