INSERT INTO usuarios
(nombre, apellidos, usuario, email, telefono, password_hash)
VALUES
('User', 'Fernández', 'User1', 'user1@user1.com', '666554433', '1234');

INSERT INTO valores
(ticker, isin, nombre, mercado, sector, pais, divisa, cotizacion_actual)
VALUES
('TEF', 'ES0178430E18', 'Telefónica', 'BME', 'Telecomunicaciones', 'España', 'EUR', 3.90),
('CABK', 'ES0140609019', 'CaixaBank', 'BME', 'Banca', 'España', 'EUR', 12.50),
('IDR', 'ES0118594417', 'Indra', 'BME', 'Tecnología', 'España', 'EUR', 51.00);

INSERT INTO operaciones
(usuario_id, valor_id, tipo, fecha, numero_acciones, precio, gastos, comentarios)
VALUES
(1, 1, 'COMPRA', '2005-12-12', 150, 3.50, 11.00, 'Compra inicial Telefónica'),
(1, 2, 'COMPRA', '2026-03-19', 200, 10.50, 11.00, 'Compra CaixaBank'),
(1, 3, 'COMPRA', '2005-01-01', 200, 50.00, 11.00, 'Compra Indra');