CREATE DATABASE aerolinea;

USE aerolinea;

-- Crear tabla Vuelos
CREATE TABLE Vuelos (
  id INT PRIMARY KEY,
  origen VARCHAR(50),
  destino VARCHAR(50),
  fecha_hora_salida DATETIME,
  fecha_hora_llegada DATETIME,
  duracion_vuelo INT,
  numero_vuelo VARCHAR(50),
  avion VARCHAR(50),
  capacidad_avion INT,
  pasajeros INT,
  carga INT
);

-- Crear tabla Informacion_Financiera
CREATE TABLE Informacion_Financiera (
  id INT PRIMARY KEY,
  vuelo_id INT,
  costo_combustible DECIMAL(10, 2),
  costos_mantenimiento DECIMAL(10, 2),
  ingresos_venta_boletos DECIMAL(10, 2),
  ingresos_servicios_adicionales DECIMAL(10, 2),
  costos_operativos DECIMAL(10, 2),
  FOREIGN KEY (vuelo_id) REFERENCES Vuelos(id)
);

-- Crear tabla Informacion_Operacional
CREATE TABLE Informacion_Operacional (
  id INT PRIMARY KEY,
  vuelo_id INT,
  retraso VARCHAR(50),
  causa_retraso VARCHAR(50),
  cancelacion VARCHAR(50),
  razon_cancelacion VARCHAR(50),
  tasa_ocupacion DECIMAL(10, 2),
  distancia_ruta INT,
  FOREIGN KEY (vuelo_id) REFERENCES Vuelos(id)
);