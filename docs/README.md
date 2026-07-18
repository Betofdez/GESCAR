# GESCAR

Sistema de gestión de carteras de inversión desarrollado como Trabajo Fin de Grado.

<p align="center">
    <img src="Capturas/pantallaInicial.png" width="900">
</p>

**GESCAR** (Gestor de Carteras de Inversión) es una aplicación web desarrollada en **Python** utilizando el framework **Flask**, cuyo objetivo es permitir la gestión de una cartera de inversión de forma sencilla e intuitiva.

La aplicación permite registrar operaciones de compra y venta de acciones, consultar la composición de la cartera, obtener cotizaciones actualizadas mediante Yahoo Finance y exportar la información a Excel y PDF.

---

# Características principales

- Autenticación de usuarios mediante inicio de sesión.
- Gestión de carteras de inversión.
- Registro de compras de acciones.
- Registro de ventas de acciones.
- Cálculo automático de posiciones abiertas.
- Consulta del histórico de operaciones.
- Consulta de índices bursátiles.
- Consulta de las empresas del IBEX 35.
- Actualización automática de cotizaciones mediante Yahoo Finance.
- Exportación de información a Excel.
- Exportación de información a PDF.
- Interfaz responsive desarrollada con Bootstrap.
- Tablas dinámicas mediante DataTables.

---

# Tecnologías utilizadas

## Backend

- Python 3.x
- Flask
- PyMySQL
- Werkzeug
- yfinance

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- DataTables

## Base de datos

- MySQL
- XAMPP

## Librerías utilizadas

- openpyxl
- reportlab
- python-dotenv
- pandas
- yfinance

---

# Diagramas de la aplicación

## Arquitectura de la aplicación
El proyecto sigue una arquitectura por capas.
<p align="center">
    <img src="Diagramas/Diagrama de Arquitectura.png"
         alt="Diagrama de arquitectura de GESCAR"
         width="900">
</p>

## Modelo entidad-relación

<p align="center">
    <img src="Diagramas/Diagrama Entidad Relación.png"
         alt="Diagrama de arquitectura de GESCAR"
         width="900">
</p>

## Casos de uso

<p align="center">
    <img src="Diagramas/Diagrama de Casos de Uso (UML).png"
         alt="Diagrama de arquitectura de GESCAR"
         width="900">
</p>

# Estructura del proyecto

```
GESCAR/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── LICENSE
│
├── database/
│   └── schema.sql
│
├── filters/
│   └── formatos.py
│
├── domain/
│   ├── cartera.py
│   ├── operacion.py
│   ├── posicion.py
│   └── valor.py
│
├── models/
│   ├── cartera_model.py
│   ├── operacion_model.py
│   ├── ibex_model.py
│   ├── indice_model.py
│   ├── historico_model.py
│   ├── usuario_model.py
│   └── valor_model.py
├── routes/
│   ├── altas_routes.py
│   ├── cartera_routes.py
│   ├── cotizacion_routes.py
│   ├── error_routes.py
│   ├── exportacion_routes.py
│   ├── historico_routes.py
│   ├── indices_routes.py
│   ├── inicio_routes.py
│   ├── login_routes.py
│   ├── venta_routes.py
│   └── ibex_routes.py
├── services/
│   ├── cartera_service.py
│   ├── cotizacion_service.py
│   ├── exportacion_service.py
│   ├── ibex_service.py
│   └── indice_service.py
├── static/
│   └── estilos.css
│
├── templates/
│   ├── altas.html
│   ├── base.html
│   ├── cartera.html
│   ├── historico.html
│   ├── ibex35.html
│   ├── indices.html
│   ├── inicio.html
│   ├── login.html
│   └── venta.html
│
└── utils/
│   └── auth.py
│
├── docs/
│   ├── MANUAL DE USUARIO.docx
│   ├── README.md
│   ├── altas.html
│   └── Diagramas/
│       ├── Diagrama de Arquitectura.png
│       ├── Diagrama de Casos de Uso (UML).png
│       └── Diagrama Entidad Relación.png
│   └── Capturas/
│       ├── pantallaInicial.png
```

---

# Requisitos

Antes de ejecutar la aplicación es necesario disponer de:

- Python 3.11 o superior
- MySQL
- XAMPP
- Git (opcional)

---

# Instalación

## 1. Clonar el proyecto

```bash
git clone https://github.com/usuario/gescar.git
```

o descargar el proyecto en formato ZIP.

---

## 2. Crear un entorno virtual

Windows

```bash
python -m venv venv
```

Activarlo

```bash
venv\Scripts\activate
```

---

## 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Crear la base de datos

Desde phpMyAdmin crear la base de datos:

```
gescar_db
```

Importar posteriormente el archivo:

```
schema.sql
```

---

## 5. Configurar el archivo .env

Crear un archivo llamado:

```
.env
```

con el siguiente contenido:

```env
SECRET_KEY=gescar_clave_desarrollo

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=gescar_db

FLASK_DEBUG=True
```

---

# Ejecución

Con el entorno virtual activado:

```bash
python app.py
```

Abrir posteriormente el navegador:

```
http://localhost:5000
```

---

# Funcionalidades

## Inicio de sesión

Permite acceder a la aplicación mediante usuario y contraseña.

---

## Mi cartera

Muestra:

- Valor de la cartera
- Inversión realizada
- Rentabilidad
- Posiciones abiertas

---

## Altas

Permite registrar nuevas compras de acciones.

Las acciones disponibles corresponden a todas las empresas del IBEX 35.

---

## Venta de acciones

Permite vender parcial o totalmente una posición existente.

La aplicación actualiza automáticamente la cartera.

---

## Histórico

Consulta de todas las compras y ventas realizadas.

Incluye filtros y ordenación mediante DataTables.

---

## Índices

Consulta de los principales índices bursátiles.

Actualización automática de cotizaciones.

---

## IBEX 35

Consulta de todas las empresas del IBEX 35.

Actualización automática desde Yahoo Finance.

---

## Exportaciones

La información puede exportarse a:

- Excel (.xlsx)
- PDF

---

# Seguridad

La aplicación incorpora:

- Contraseñas cifradas mediante Werkzeug.
- Gestión de sesiones.
- Protección de rutas mediante login_required.
- Configuración centralizada mediante variables de entorno.

---

# Autor

Trabajo Fin de Grado

Desarrollado por:

**Alberto Fernández**

Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)

Curso 2025-2026

---

# Licencia

Este proyecto ha sido desarrollado con fines exclusivamente académicos como Trabajo Fin de Grado.