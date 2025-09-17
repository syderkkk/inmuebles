# 🏥 Gestión de Inmuebles

## 📖 Descripción del Proyecto
Aplicación web desarrollada en Django para la gestión de inmuebles. Permite administrar la información de inmubles, asignarles propietarios y realizar operaciones CRUD completas.

## 🛠️ Tecnologías Utilizadas
- **Backend**: Django 5.2.6
- **Base de Datos**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.8
- **Lenguaje**: Python 3.x

## ⚙️ Pasos para Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación
1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/syderkkk/inmuebles.git
   cd inmuebles
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   cd src
   pip install -r requirements.txt
   ```

4. **Realizar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   Abrir el navegador en: `http://127.0.0.1:8000/`

## 🚀 Funcionalidades Implementadas

### Gestión de Inmuebles
- ✅ **Listado de Inmubles** (2 pts)
- ✅ **Creación de Inmubles** (2 pts)
- ✅ **Edición de Inmubles** (2 pts)
- ✅ **Eliminación de Inmubles** (2 pts)
- ✅ **Buscador de Inmubles** (3 pts)
- ✅ **Relación Inmubles-Propietarios** (3 pts)


## 📁 Estructura del Proyecto
```
inmuebles/
├── src/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── gestor/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── templates/
│   │       └── inmuebles/
│   │           ├── base.html
│   │           ├── listar_inmuebles.html
│   │           ├── crear_inmuebles.html
│   │           └── ...
│   ├── manage.py
│   └── requirements.txt
├── README.md
└── .gitignore
```

## 🔧 Características Técnicas
- **Modelos**: Relación ForeignKey entre Inmuesbles y Propietarios
- **Formularios**: Formularios Django con validación
- **Vistas**: Vistas basadas en funciones
- **Templates**: Sistema de herencia de templates
- **Búsqueda**: Búsqueda por nombre de paciente y doctor
- **Estilos**: Bootstrap para UI responsiva

## 🙌 Autor
** Italo Mendoza**
- Estudiante de Desarrollo de Aplicaciones Empresariales
- TECSUP - Ciclo 4

---
*Proyecto desarrollado como parte de la evaluación de la Semana 4 - Desarrollo de Aplicaciones Empresariales*