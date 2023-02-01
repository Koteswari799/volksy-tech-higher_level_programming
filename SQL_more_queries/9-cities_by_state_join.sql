-- hii
SELECT cities.id,cities.name,states.name FROM ststes INNER JOIN cities ON states.id = cities.state_id WHERE ORDER BY cities.id ASC;
