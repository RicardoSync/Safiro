CREATE DATABASE IF NOT EXISTS gestion_escolar;
USE gestion_escolar;

-- Tabla de Alumnos
CREATE TABLE Alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100),
    anio_escolar VARCHAR(10) NOT NULL
);

-- Tabla de Docentes
CREATE TABLE Docentes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    especialidad VARCHAR(100)
);

-- Tabla de Materias
CREATE TABLE Materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    docente_id INT,
    FOREIGN KEY (docente_id) REFERENCES Docentes(id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- Tabla de Asistencia
CREATE TABLE Asistencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alumno_id INT NOT NULL,
    materia_id INT NOT NULL,
    fecha DATE NOT NULL,
    presente BOOLEAN NOT NULL,
    FOREIGN KEY (alumno_id) REFERENCES Alumnos(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (materia_id) REFERENCES Materias(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla de Calificaciones
CREATE TABLE Calificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alumno_id INT NOT NULL,
    materia_id INT NOT NULL,
    calificacion DECIMAL(5, 2) NOT NULL,
    fecha DATE NOT NULL,
    periodo VARCHAR(20) NOT NULL,
    FOREIGN KEY (alumno_id) REFERENCES Alumnos(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (materia_id) REFERENCES Materias(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla intermedia de Alumnos_Materias
CREATE TABLE Alumnos_Materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alumno_id INT NOT NULL,
    materia_id INT NOT NULL,
    fecha_inscripcion DATE NOT NULL,
    FOREIGN KEY (alumno_id) REFERENCES Alumnos(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (materia_id) REFERENCES Materias(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Crear tabla de Roles
CREATE TABLE Roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Insertar roles predefinidos
INSERT INTO Roles (nombre) VALUES ('Directivo'), ('Docente'), ('Alumno'), ('Secretaria');

-- Crear tabla de Usuarios
CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES Roles(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Crear índices para mejorar la performance en las búsquedas frecuentes
CREATE INDEX idx_alumno_id ON Asistencia(alumno_id);
CREATE INDEX idx_materia_id ON Asistencia(materia_id);
CREATE INDEX idx_alumno_id_calificaciones ON Calificaciones(alumno_id);
CREATE INDEX idx_materia_id_calificaciones ON Calificaciones(materia_id);
