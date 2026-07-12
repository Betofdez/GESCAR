-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-07-2026 a las 21:07:29
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gescar_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `acciones_ibex`
--

CREATE TABLE `acciones_ibex` (
  `id` int(11) NOT NULL,
  `ticker` varchar(15) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `ticker_yahoo` varchar(30) NOT NULL,
  `cotizacion_actual` decimal(12,4) DEFAULT 0.0000,
  `variacion` decimal(12,4) DEFAULT 0.0000,
  `variacion_porcentaje` decimal(12,4) DEFAULT 0.0000
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `acciones_ibex`
--

INSERT INTO `acciones_ibex` (`id`, `ticker`, `nombre`, `ticker_yahoo`, `cotizacion_actual`, `variacion`, `variacion_porcentaje`) VALUES
(1, 'ANA', 'Acciona', 'ANA.MC', 250.2000, -0.4000, -0.1596),
(2, 'ACX', 'Acerinox', 'ACX.MC', 16.0000, 0.4800, 3.0928),
(3, 'ACS', 'ACS', 'ACS.MC', 120.0000, -0.6000, -0.4975),
(4, 'AENA', 'Aena', 'AENA.MC', 26.9400, 0.1200, 0.4474),
(5, 'AMS', 'Amadeus', 'AMS.MC', 50.7400, 0.6600, 1.3179),
(6, 'MTS', 'ArcelorMittal', 'MTS.MC', 57.9800, 3.4200, 6.2683),
(7, 'SAB', 'Banco Sabadell', 'SAB.MC', 3.2190, 0.0410, 1.2901),
(8, 'SAN', 'Banco Santander', 'SAN.MC', 12.1380, 0.0920, 0.7637),
(9, 'BKT', 'Bankinter', 'BKT.MC', 15.3600, 0.2200, 1.4531),
(10, 'BBVA', 'BBVA', 'BBVA.MC', 22.4800, 0.3400, 1.5357),
(11, 'CABK', 'CaixaBank', 'CABK.MC', 12.5250, -0.0250, -0.1992),
(12, 'CLNX', 'Cellnex', 'CLNX.MC', 25.1800, 0.4700, 1.9021),
(13, 'ENG', 'Enagás', 'ENG.MC', 16.8400, -0.0400, -0.2370),
(14, 'ELE', 'Endesa', 'ELE.MC', 38.9900, 0.1600, 0.4121),
(15, 'FER', 'Ferrovial', 'FER.MC', 56.8000, 0.1600, 0.2825),
(16, 'FDR', 'Fluidra', 'FDR.MC', 18.7600, 0.1300, 0.6978),
(17, 'GRF', 'Grifols', 'GRF.MC', 8.9040, -0.0880, -0.9786),
(18, 'IAG', 'IAG', 'IAG.MC', 5.5220, 0.0580, 1.0615),
(19, 'IBE', 'Iberdrola', 'IBE.MC', 20.9000, -0.1600, -0.7597),
(20, 'ITX', 'Inditex', 'ITX.MC', 54.9600, -0.4400, -0.7942),
(21, 'IDR', 'Indra', 'IDR.MC', 47.4500, -2.1500, -4.3347),
(22, 'LOG', 'Logista', 'LOG.MC', 33.9000, 0.0200, 0.0590),
(23, 'MAP', 'Mapfre', 'MAP.MC', 4.4160, 0.0120, 0.2725),
(24, 'MEL', 'Meliá Hotels', 'MEL.MC', 11.1600, 0.0000, 0.0000),
(25, 'MRL', 'Merlin Properties', 'MRL.MC', 15.0500, 0.1500, 1.0067),
(26, 'NTGY', 'Naturgy', 'NTGY.MC', 28.0400, -0.2000, -0.7082),
(27, 'PUIG', 'Puig', 'PUIG.MC', 16.7700, -0.0900, -0.5338),
(28, 'RED', 'Redeia', 'RED.MC', 15.3900, 0.1700, 1.1170),
(29, 'REP', 'Repsol', 'REP.MC', 23.1200, -0.1100, -0.4735),
(30, 'ROVI', 'Laboratorios Rovi', 'ROVI.MC', 56.0000, -0.1500, -0.2671),
(31, 'SCYR', 'Sacyr', 'SCYR.MC', 4.7340, -0.0640, -1.3339),
(32, 'SLR', 'Solaria', 'SLR.MC', 18.7550, 0.0000, 0.0000),
(33, 'TEF', 'Telefónica', 'TEF.MC', 3.5260, 0.0500, 1.4384),
(34, 'UNI', 'Unicaja Banco', 'UNI.MC', 3.2700, 0.0240, 0.7394),
(35, 'VIS', 'Viscofan', 'VIS.MC', 55.1000, -1.9000, -3.3333);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alarmas`
--

CREATE TABLE `alarmas` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `valor_id` int(11) NOT NULL,
  `tipo` enum('SUPERIOR','INFERIOR') NOT NULL,
  `precio_objetivo` decimal(12,4) NOT NULL,
  `activa` tinyint(1) DEFAULT 1,
  `notificar_email` tinyint(1) DEFAULT 0,
  `notificar_sms` tinyint(1) DEFAULT 0,
  `fecha_creacion` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `alarmas`
--

INSERT INTO `alarmas` (`id`, `usuario_id`, `valor_id`, `tipo`, `precio_objetivo`, `activa`, `notificar_email`, `notificar_sms`, `fecha_creacion`) VALUES
(1, 1, 1, 'SUPERIOR', 4.0000, 1, 1, 0, '2026-07-04 17:32:11'),
(2, 1, 2, 'INFERIOR', 11.0000, 1, 1, 1, '2026-07-04 17:32:11'),
(3, 1, 3, 'INFERIOR', 10.0000, 1, 1, 0, '2026-07-05 14:35:00'),
(4, 1, 1, 'SUPERIOR', 12.0000, 1, 0, 1, '2026-07-05 14:35:20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dividendos`
--

CREATE TABLE `dividendos` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `valor_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `importe_por_accion` decimal(12,4) NOT NULL,
  `numero_acciones` decimal(12,4) NOT NULL,
  `retencion` decimal(12,4) DEFAULT 0.0000,
  `comentarios` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `indices`
--

CREATE TABLE `indices` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `ticker_yahoo` varchar(30) NOT NULL,
  `cotizacion_actual` decimal(12,4) DEFAULT 0.0000,
  `variacion` decimal(12,4) DEFAULT 0.0000,
  `variacion_porcentaje` decimal(12,4) DEFAULT 0.0000
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `indices`
--

INSERT INTO `indices` (`id`, `nombre`, `ticker_yahoo`, `cotizacion_actual`, `variacion`, `variacion_porcentaje`) VALUES
(1, 'IBEX 35', '^IBEX', 19852.4004, 180.5996, 0.9181),
(2, 'S&P 500', '^GSPC', 7483.2402, 0.0103, 0.0001),
(3, 'NASDAQ', '^IXIC', 25832.6699, -207.3594, -0.7963),
(4, 'DAX', '^GDAXI', 25779.3105, 198.4297, 0.7757),
(5, 'FTSE 100', '^FTSE', 10679.0000, 26.0996, 0.2450);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operaciones`
--

CREATE TABLE `operaciones` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `valor_id` int(11) NOT NULL,
  `tipo` enum('COMPRA','VENTA') NOT NULL,
  `fecha` date NOT NULL,
  `numero_acciones` decimal(12,4) NOT NULL,
  `precio` decimal(12,4) NOT NULL,
  `gastos` decimal(12,4) DEFAULT 0.0000,
  `comentarios` text DEFAULT NULL,
  `fecha_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `operaciones`
--

INSERT INTO `operaciones` (`id`, `usuario_id`, `valor_id`, `tipo`, `fecha`, `numero_acciones`, `precio`, `gastos`, `comentarios`, `fecha_registro`) VALUES
(1, 1, 1, 'COMPRA', '2005-12-12', 150.0000, 3.5000, 11.0000, 'Compra inicial Telefónica', '2026-06-28 13:48:07'),
(2, 1, 2, 'COMPRA', '2026-03-19', 200.0000, 10.5000, 11.0000, 'Compra CaixaBank', '2026-06-28 13:48:07'),
(3, 1, 3, 'COMPRA', '2005-01-01', 200.0000, 50.0000, 11.0000, 'Compra Indra', '2026-06-28 13:48:07'),
(4, 1, 1, 'COMPRA', '2026-06-28', 10.0000, 4.0000, 1.0000, 'Esto es un comentario de prueba', '2026-06-28 13:50:05'),
(5, 1, 1, 'COMPRA', '2026-06-28', 15.0000, 1.0000, 1.0000, '', '2026-06-28 14:00:36'),
(6, 1, 2, 'COMPRA', '2026-06-28', 1.0000, 1.0000, 1.0000, 'COmentario', '2026-06-28 14:06:21'),
(7, 1, 2, 'COMPRA', '2026-06-27', 1.0000, 1.0000, 1.0000, '', '2026-06-28 14:16:22'),
(8, 1, 2, 'VENTA', '2026-06-30', 1.0000, 12.5000, 5.0000, 'Comentario de venta', '2026-06-28 14:22:58'),
(9, 1, 2, 'VENTA', '2026-06-22', 2.0000, 12.5000, 2.0000, '', '2026-06-28 14:23:08'),
(10, 1, 3, 'VENTA', '2026-07-08', 1.0000, 51.0000, 10.0000, '', '2026-07-04 14:17:01'),
(11, 1, 1, 'VENTA', '2026-07-10', 1.0000, 3.9000, 0.0000, '', '2026-07-04 17:04:12'),
(12, 1, 1, 'VENTA', '2026-07-15', 4.0000, 3.9000, 0.0000, '', '2026-07-04 17:11:14'),
(13, 1, 3, 'VENTA', '2026-07-04', 49.0000, 51.0000, 10.0000, 'Otro comentario', '2026-07-04 17:19:12'),
(14, 1, 1, 'VENTA', '2026-07-09', 50.0000, 3.5500, 10.0000, '', '2026-07-04 18:09:03'),
(15, 1, 2, 'COMPRA', '2026-07-01', 200.0000, 10.0000, 0.0000, 'Nueva compra de acciones de Caixxa', '2026-07-04 18:28:30'),
(16, 1, 2, 'COMPRA', '2026-07-08', 12.0000, 12.0000, 12.0000, 'Otro COmentario', '2026-07-05 14:36:12'),
(17, 1, 2, 'VENTA', '2026-07-05', 111.0000, 12.6500, 0.0000, '', '2026-07-05 14:40:01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(150) DEFAULT NULL,
  `usuario` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `password_hash` varchar(255) NOT NULL,
  `fecha_alta` datetime DEFAULT current_timestamp(),
  `ultimo_acceso` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `usuario`, `email`, `telefono`, `password_hash`, `fecha_alta`, `ultimo_acceso`) VALUES
(1, 'Alberto', 'Fernández', 'User1', 'user1@user1.com', '666554433', 'scrypt:32768:8:1$fSl0evdN1Fhb9e02$f9ae3ed931306645efddf6b283217da2a09b82db4cf179a2fe40f829d5016bfc5cf3187752185bef65760b738e5f6bca49d278632f9c4498b9f6608ce1903255', '2026-06-28 13:48:07', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `valores`
--

CREATE TABLE `valores` (
  `id` int(11) NOT NULL,
  `ticker` varchar(15) NOT NULL,
  `isin` varchar(20) DEFAULT NULL,
  `nombre` varchar(150) NOT NULL,
  `mercado` varchar(30) NOT NULL,
  `sector` varchar(100) DEFAULT NULL,
  `pais` varchar(80) DEFAULT NULL,
  `divisa` varchar(10) DEFAULT 'EUR',
  `cotizacion_actual` decimal(12,4) DEFAULT 0.0000,
  `activo` tinyint(1) DEFAULT 1,
  `ticker_yahoo` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `valores`
--

INSERT INTO `valores` (`id`, `ticker`, `isin`, `nombre`, `mercado`, `sector`, `pais`, `divisa`, `cotizacion_actual`, `activo`, `ticker_yahoo`) VALUES
(1, 'TEF', 'ES0178430E18', 'Telefónica', 'BME', 'Telecomunicaciones', 'España', 'EUR', 3.5500, 1, 'TEF.MC'),
(2, 'CABK', 'ES0140609019', 'CaixaBank', 'BME', 'Banca', 'España', 'EUR', 12.6500, 1, 'CABK.MC'),
(3, 'IDR', 'ES0118594417', 'Indra', 'BME', 'Tecnología', 'España', 'EUR', 51.4400, 1, 'IDR.MC');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `acciones_ibex`
--
ALTER TABLE `acciones_ibex`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `alarmas`
--
ALTER TABLE `alarmas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_alarmas_usuario` (`usuario_id`),
  ADD KEY `idx_alarmas_valor` (`valor_id`);

--
-- Indices de la tabla `dividendos`
--
ALTER TABLE `dividendos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_dividendos_usuario` (`usuario_id`),
  ADD KEY `idx_dividendos_valor` (`valor_id`);

--
-- Indices de la tabla `indices`
--
ALTER TABLE `indices`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `operaciones`
--
ALTER TABLE `operaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_operaciones_usuario` (`usuario_id`),
  ADD KEY `idx_operaciones_valor` (`valor_id`),
  ADD KEY `idx_operaciones_fecha` (`fecha`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `valores`
--
ALTER TABLE `valores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ticker` (`ticker`,`mercado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `acciones_ibex`
--
ALTER TABLE `acciones_ibex`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `alarmas`
--
ALTER TABLE `alarmas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `dividendos`
--
ALTER TABLE `dividendos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `indices`
--
ALTER TABLE `indices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `operaciones`
--
ALTER TABLE `operaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `valores`
--
ALTER TABLE `valores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alarmas`
--
ALTER TABLE `alarmas`
  ADD CONSTRAINT `alarmas_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `alarmas_ibfk_2` FOREIGN KEY (`valor_id`) REFERENCES `valores` (`id`);

--
-- Filtros para la tabla `dividendos`
--
ALTER TABLE `dividendos`
  ADD CONSTRAINT `dividendos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `dividendos_ibfk_2` FOREIGN KEY (`valor_id`) REFERENCES `valores` (`id`);

--
-- Filtros para la tabla `operaciones`
--
ALTER TABLE `operaciones`
  ADD CONSTRAINT `operaciones_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `operaciones_ibfk_2` FOREIGN KEY (`valor_id`) REFERENCES `valores` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
