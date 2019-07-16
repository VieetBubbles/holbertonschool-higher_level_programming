-- jba,dba
-- nalknda
SELECT state, MAX(value) FROM temperatures GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
