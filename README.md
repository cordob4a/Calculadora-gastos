# Calculadora de Gastos – Proyecto Web

## Descripción general

Este proyecto es una **aplicación web simple para el registro de gastos personales**, desarrollada con **FastAPI**, **SQLAlchemy** y **PostgreSQL**, y ejecutada dentro de contenedores **Docker**. El objetivo principal es permitir la carga de gastos mediante un formulario HTML y su persistencia en una base de datos relacional.

La aplicación está pensada como un proyecto de aprendizaje práctico, combinando:

* Backend web con FastAPI
* Renderizado de formularios con Jinja2
* Persistencia de datos con SQLAlchemy
* Orquestación de servicios con Docker Compose

---

## Funcionalidad principal

La aplicación permite:

1. Acceder a un formulario web para cargar gastos.
2. Ingresar los siguientes datos:

   * Concepto del gasto
   * Monto
   * Fecha
   * Descripción
3. Enviar el formulario mediante HTTP POST.
4. Guardar el gasto en una base de datos PostgreSQL.
5. Mostrar una pantalla de confirmación con los datos cargados.

Actualmente, el formulario se encuentra disponible en la ruta:

```
/carga_gastos
```

---

## Arquitectura del proyecto

El proyecto sigue una estructura modular:

```
calculadora_gastos/
├── app/
│   ├── main.py                # Punto de entrada de FastAPI
│   ├── db/
│   │   └── database.py        # Conexión a la base de datos
│   ├── models/
│   │   └── models.py          # Modelos SQLAlchemy
│   ├── functions/
│   │   └── carga_gastos.py    # Rutas y lógica del formulario
│   └── templates/
│       ├── carga_gastos.html  # Formulario HTML
│       └── resultado_gasto.html
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## Tecnologías utilizadas actualmente

* **Python 3.13**
* **FastAPI** – Framework web
* **Uvicorn** – Servidor ASGI
* **SQLAlchemy** – ORM
* **PostgreSQL** – Base de datos
* **Jinja2** – Templates HTML
* **Docker & Docker Compose** – Contenedorización

---

## Base de datos

La base de datos utiliza PostgreSQL y contiene una tabla principal:

### Tabla: `gastos`

Campos esperados:

* `id` (integer, primary key)
* `gasto` (string)
* `monto` (float)
* `fecha` (date)
* `descripcion` (string)

El modelo SQLAlchemy debe coincidir exactamente con la estructura real de la tabla para evitar errores de inserción.

---

## Estado actual del proyecto

* La aplicación levanta correctamente en Docker.
* El formulario HTML responde correctamente en `/carga_gastos`.
* La base de datos recibe intentos de inserción.
* Existe un error actual relacionado con la **no existencia de la tabla `gastos`**, lo que indica que:

  * La tabla no fue creada aún, o
  * El esquema/modelo no coincide con la base real, o
  * Falta ejecutar la creación de tablas (`Base.metadata.create_all`).

---

## Próximos pasos previstos

1. Verificar y unificar:

   * Nombre de la tabla en el modelo
   * Nombre de la tabla en PostgreSQL
2. Asegurar la creación automática de tablas al iniciar la app.
3. Agregar una ruta raíz (`/`) como página de inicio.
4. Mejorar manejo de errores y validaciones.
5. Agregar listado de gastos cargados.

---

## Objetivo del proyecto

Este proyecto busca consolidar conocimientos en:

* Desarrollo backend con FastAPI
* Uso real de ORM y bases de datos
* Arquitectura básica de aplicaciones web
* Dockerización de servicios
* A futuro implementar IA para analisis de gastos
* Se intentara que sea un gestor de economico para los usuarios



No está enfocado en frontend avanzado, sino en la **lógica, estructura y persistencia** de la aplicación.(Cabe destacar que cuando se finalice la logica se buscara dar un estilo estetico y facil de utilizar para cualquier usuario).
