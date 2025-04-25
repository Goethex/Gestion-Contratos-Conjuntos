# Sistema de Gestión de Contratos / Contract Management System

## Español

### Descripción
Sistema de Gestión de Contratos es un módulo desarrollado en **Django** para la administración eficiente de contratos en conjuntos residenciales. Permite a los administradores crear, editar, consultar y gestionar contratos de manera sencilla, con una interfaz web intuitiva y funcionalidades adaptadas a las necesidades de gestión de propiedades.

### Características
- **Gestión de contratos**: Registro y edición de contratos con detalles como fechas, términos y partes involucradas.
- **Interfaz amigable**: Plantillas responsivas con formularios dinámicos (usando `django-crispy-forms`).
- **Soporte multimedia**: Manejo de imágenes y documentos asociados a contratos (usando `Pillow`).
- **Escalable**: Estructura modular que permite agregar nuevas funcionalidades.
- **Panel de administración**: Acceso seguro para gestionar datos a través de Django Admin.

### Requisitos previos
- Python 3.8+
- Git
- Virtualenv (recomendado)

### Instalación y configuración
Sigue estos pasos para clonar y ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Goethex/Gestion-Contratos-Conjuntos.git
   cd Gestion-Contratos-Conjuntos
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python3 -m venv venv
   ```
   - En Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos**:
   Aplica las migraciones para configurar la base de datos:
   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario** (opcional, para acceder al panel de administración):
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**:
   ```bash
   python manage.py runserver
   ```

El servidor estará disponible en `http://localhost:8000`.

### Uso
- **Panel de administración**: Accede a `http://localhost:8000/admin` con las credenciales del superusuario para gestionar contratos.
- **Interfaz web**: Usa las funcionalidades de la aplicación para registrar, consultar o editar contratos.
- **Personalización**: Configura las variables de entorno en `settings.py` o un archivo `.env` para ajustar la base de datos, almacenamiento de archivos o claves secretas.

### Estructura del proyecto
- `apps/`: Aplicaciones Django que contienen la lógica de negocio (contratos, usuarios, etc.).
- `templates/`: Plantillas HTML para la interfaz web.
- `static/`: Archivos estáticos (CSS, JavaScript, imágenes).
- `Sistema_de_gesti_n_de_contratos/`: Configuración principal del proyecto Django.
- `requirements.txt`: Lista de dependencias del proyecto.

### Contribuciones
¡Las contribuciones son bienvenidas! Para contribuir:
1. Haz un *fork* del repositorio.
2. Crea una rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz *commit*:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía un *pull request* para revisión.

### Licencia
Este proyecto está bajo la [Licencia MIT](LICENSE).

---

## English

### Description
Contract Management System is a **Django**-based module for the efficient management of contracts in residential complexes. It enables administrators to create, edit, query, and manage contracts seamlessly, with an intuitive web interface and features tailored to property management needs.

### Features
- **Contract Management**: Register and edit contracts with details such as dates, terms, and involved parties.
- **User-Friendly Interface**: Responsive templates with dynamic forms (using `django-crispy-forms`).
- **Multimedia Support**: Handle images and documents associated with contracts (using `Pillow`).
- **Scalable**: Modular structure for adding new functionalities.
- **Admin Panel**: Secure access to manage data via Django Admin.

### Prerequisites
- Python 3.8+
- Git
- Virtualenv (recommended)

### Installation and Setup
Follow these steps to clone and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Goethex/Gestion-Contratos-Conjuntos.git
   cd Gestion-Contratos-Conjuntos
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   ```
   - On Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   Apply migrations to configure the database:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

The server will be available at `http://localhost:8000`.

### Usage
- **Admin Panel**: Access `http://localhost:8000/admin` with superuser credentials to manage contracts.
- **Web Interface**: Use the application to register, query, or edit contracts.
- **Customization**: Configure environment variables in `settings.py` or a `.env` file to adjust the database, file storage, or secret keys.

### Project Structure
- `apps/`: Django applications containing business logic (contracts, users, etc.).
- `templates/`: HTML templates for the web interface.
- `static/`: Static files (CSS, JavaScript, images).
- `Sistema_de_gesti_n_de_contratos/`: Main Django project configuration.
- `requirements.txt`: List of project dependencies.

### Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch for your changes:
   ```bash
   git checkout -b feature/new-functionality
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new functionality"
   ```
4. Submit a pull request for review.

### License
This project is licensed under the [MIT License](LICENSE).