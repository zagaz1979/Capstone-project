# Capstone-project
Proyecto para un restaurante LitleLemon

## Que tecnologías se utilizaron
- Python3
- Django
- Django Rest Framework
- Djoser
- Mysql
- Insomnia

## Pasos para ejecutar el proyecto

1. Clona el repositorio
```
git clone https://github.com/zagaz1979/Capstone-project
cd Capstone-project
```
2. Crear el entorno virtual
```
# Crear entorno
python3 -m venv venv

# Activar el entorno
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate.bat    # Windows
```

3. Instalar las dependencias
```
pip install -r requirements.txt
```

4. Debe de tener el servicio de mysql activo

5. Ejecutar las migraciones
```
python manage.py makemigrations
python manage.py migrate
```

6. Ejecutar el servidor
```
python manage.py runserver
```

7. Rutas principales
```
/restaurant/menu-items/
/restaurant/booking/tables/
```

8. Otras rutas
```
/auth/users/
/auth/token/login/
/restaurant/api-token-auth/
```

## Nota:
- Para ejecutar los endpoint utilice insomnia o Postman 