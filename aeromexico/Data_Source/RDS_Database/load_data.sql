-- Cargar datos en la tabla Vuelos
LOAD DATA INFILE 'vuelos.csv'
INTO TABLE Vuelos
FIELDS TERMINATED BY ','
ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos en la tabla Informacion_Financiera
LOAD DATA INFILE 'informacion_financiera.csv'
INTO TABLE Informacion_Financiera
FIELDS TERMINATED BY ','
ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Cargar datos en la tabla Informacion_Operacional
LOAD DATA INFILE 'informacion_operacional.csv'
INTO TABLE Informacion_Operacional
FIELDS TERMINATED BY ','
ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;