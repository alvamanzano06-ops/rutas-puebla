# Rutas Puebla

Aplicación web para administrar paradas de transporte público de la ciudad de Puebla.
Permite crear, consultar, editar y eliminar paradas, y verlas en un mapa interactivo.

## Tecnologías
- **Python 3.11+** y **FastAPI** (servidor y API)
- **Redis Cloud** (base de datos en la nube, clave-valor con JSON)
- **redis-py** (conexión de Python con Redis)
- **HTML, CSS y JavaScript** (página web)
- **Leaflet + OpenStreetMap** (mapa)

## Funciones
- Registrar una parada (nombre, colonia, coordenadas, rutas y estado)
- Consultar una parada por su ID
- Listar todas las paradas
- Editar una parada
- Eliminar una parada (con confirmación)
- Ver las paradas en un mapa de Puebla
- Documentación automática de la API en `/docs`

## Estructura del proyecto
```
rutas-puebla/
├── app/
│   ├── main.py        # Servidor principal
│   ├── database.py    # Conexión a Redis
│   ├── models.py      # Datos de una parada
│   └── routes.py      # Endpoints del CRUD
├── static/
│   ├── index.html     # Página principal
│   ├── styles.css     # Estilos
│   └── app.js         # Lógica de la página y mapa
├── capturas/          # Imágenes de pruebas
├── .env.example       # Ejemplo de configuración
├── requirements.txt
└── README.md
```

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/alvamanzano06-ops/rutas-puebla.git
   cd rutas-puebla
   ```
2. Crear y activar el entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Crear un archivo `.env` (copia de `.env.example`) con tu cadena de Redis Cloud:
   ```
   REDIS_URL=redis://default:TU_PASSWORD@TU_HOST:PUERTO
   ```
   > Usa `rediss://` (con dos "s") solo si tu base de Redis Cloud tiene SSL activado.

## Ejecución
```bash
uvicorn app.main:app --reload
```
- Página web: http://127.0.0.1:8000/
- Documentación Swagger: http://127.0.0.1:8000/docs
- Estado de Redis: http://127.0.0.1:8000/estado

## Endpoints
| Método | Ruta | Acción |
|--------|------|--------|
| POST | /paradas | Crear parada |
| GET | /paradas | Listar paradas |
| GET | /paradas/{id} | Obtener una parada |
| PUT | /paradas/{id} | Actualizar parada |
| DELETE | /paradas/{id} | Eliminar parada |

## Ejemplo de parada (JSON)
```json
{
  "nombre": "Parada BUAP",
  "colonia": "Los Volcanes",
  "municipio": "Puebla",
  "latitud": 19.0467,
  "longitud": -98.2065,
  "rutas": ["Ruta 4", "Ruta 61"],
  "activa": true
}
```
Cada parada se guarda en Redis con la clave `parada:{id}`, por ejemplo `parada:pue-001`.

## Errores claros
- `404`: la parada no existe
- `409`: la parada ya existe
- `422`: datos incompletos o incorrectos

## Pruebas manuales
Se probaron los cinco endpoints desde Swagger (`/docs`) y desde la página web.
Las capturas están en la carpeta `capturas/`.

## Autor
Alvaro Manzano Sánchez - Grado: 7mo Grupo: A – Materia: Optativa 1 BD en la Nube – UTP