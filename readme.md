#Lista de ventas globales

## Instalación
Ejecutar
```
pip install -r requirements.txt
```

2. Crear _config.py

Renombrar '_config_template.py' a '_config.py' e informar correctamente sus claves

3. Informar correctamente .env (opcional)

Renombrar '.env_template' a '.env' e informar las claves

- FLASK_APP = run.py
- FLASK_ENV = el que quieras de 'development' o 'production'


4. Crear BD

ejecutar 'migrations.sql' con sqlite3' en el fichero elegido como base de datos

