DROP TABLE IF EXISTS alarmas;
DROP TABLE IF EXISTS dividendos;
DROP TABLE IF EXISTS operaciones;
DROP TABLE IF EXISTS valores;
DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150),
    usuario VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    password_hash VARCHAR(255) NOT NULL,
    fecha_alta DATETIME DEFAULT CURRENT_TIMESTAMP,
    ultimo_acceso DATETIME
);

CREATE TABLE valores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(15) NOT NULL,
    isin VARCHAR(20),
    nombre VARCHAR(150) NOT NULL,
    mercado VARCHAR(30) NOT NULL,
    sector VARCHAR(100),
    pais VARCHAR(80),
    divisa VARCHAR(10) DEFAULT 'EUR',
    cotizacion_actual DECIMAL(12,4) DEFAULT 0,
    activo BOOLEAN DEFAULT TRUE,
    UNIQUE (ticker, mercado)
);

CREATE TABLE operaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    valor_id INT NOT NULL,
    tipo ENUM('COMPRA', 'VENTA') NOT NULL,
    fecha DATE NOT NULL,
    numero_acciones DECIMAL(12,4) NOT NULL,
    precio DECIMAL(12,4) NOT NULL,
    gastos DECIMAL(12,4) DEFAULT 0,
    comentarios TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (valor_id) REFERENCES valores(id)
);

CREATE TABLE dividendos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    valor_id INT NOT NULL,
    fecha DATE NOT NULL,
    importe_por_accion DECIMAL(12,4) NOT NULL,
    numero_acciones DECIMAL(12,4) NOT NULL,
    retencion DECIMAL(12,4) DEFAULT 0,
    comentarios TEXT,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (valor_id) REFERENCES valores(id)
);

CREATE TABLE alarmas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    valor_id INT NOT NULL,
    tipo ENUM('SUPERIOR', 'INFERIOR') NOT NULL,
    precio_objetivo DECIMAL(12,4) NOT NULL,
    activa BOOLEAN DEFAULT TRUE,
    notificar_email BOOLEAN DEFAULT FALSE,
    notificar_sms BOOLEAN DEFAULT FALSE,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (valor_id) REFERENCES valores(id)
);

CREATE INDEX idx_operaciones_usuario ON operaciones(usuario_id);
CREATE INDEX idx_operaciones_valor ON operaciones(valor_id);
CREATE INDEX idx_operaciones_fecha ON operaciones(fecha);

CREATE INDEX idx_dividendos_usuario ON dividendos(usuario_id);
CREATE INDEX idx_dividendos_valor ON dividendos(valor_id);

CREATE INDEX idx_alarmas_usuario ON alarmas(usuario_id);
CREATE INDEX idx_alarmas_valor ON alarmas(valor_id);