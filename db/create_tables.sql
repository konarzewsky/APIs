CREATE TABLE IF NOT EXISTS drivers (
  id INT NOT NULL,
  name varchar(20) NOT NULL,
  surname varchar(40) NOT NULL,
  age INT NOT NULL,
  created_at DATE NOT NULL DEFAULT CURRENT_DATE,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS cars (
  id INT NOT NULL,
  brand varchar(20) NOT NULL,
  model varchar(20) NOT NULL,
  year_of_production INT NOT NULL,
  mileage INT NOT NULL,
  color varchar(20) NOT NULL,
  driver_id INT NOT NULL REFERENCES drivers(id),
  created_at DATE NOT NULL DEFAULT CURRENT_DATE,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS tickets (
  id INT NOT NULL,
  driver_id INT NOT NULL REFERENCES drivers(id),
  fine INT,
  penalty_points INT,
  created_at DATE NOT NULL DEFAULT CURRENT_DATE,
  PRIMARY KEY (id)
);
