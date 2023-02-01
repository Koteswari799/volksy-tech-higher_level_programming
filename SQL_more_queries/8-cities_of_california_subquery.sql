-- hii
SELECT id,name FROM cities WHERE state_id = (SELECT id FROM STATES WHERE name = 'California') ORDER BY ID ASC;
