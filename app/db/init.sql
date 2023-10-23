/*  USE db; */

CREATE TABLE stations (
  id SERIAL PRIMARY KEY,
  p_id INT,
  time TIMESTAMP,
  station VARCHAR(50),
  ta FLOAT,
  lon FLOAT,
  lat FLOAT,
  z INT,
  humidity FLOAT
);

COPY stations(p_id, time, station, ta, lon, lat, z, humidity) FROM '/data/Bamberg_Stations 01.03.2023to31.03.2023.csv' DELIMITER ';' CSV HEADER;
COPY stations(p_id, time, station, ta, lon, lat, z, humidity) FROM '/data/Bamberg_Stations 01.04.2023to30.04.2023.csv' DELIMITER ';' CSV HEADER;
COPY stations(p_id, time, station, ta, lon, lat, z, humidity) FROM '/data/Bamberg_Stations 01.06.2023to30.06.2023.csv' DELIMITER ';' CSV HEADER;
COPY stations(p_id, time, station, ta, lon, lat, z, humidity) FROM '/data/Bamberg_Stations 01.07.2023to31.07.2023.csv' DELIMITER ';' CSV HEADER;
COPY stations(p_id, time, station, ta, lon, lat, z, humidity) FROM '/data/Bamberg_Stations 01.08.2023to10.08.2023.csv' DELIMITER ';' CSV HEADER;
