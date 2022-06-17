# Ollivanders Flask

Para ejecutar la aplicación (Desde linux):
```
python3 api.py
```

Es necesario crear un archivo llamado `uri.py` dentro de la carpeta `repository` con información parecida a la siguiente:
```
uri = mongodb+srv://<username>:<password>@<database>.glkvp.mongodb.net/?retryWrites=true&w=majority
```
> Lo unico que hay que modificar es lo que esta dentro de los signos `<>`: 
> - username: nombre de usuario de que pueda acceder a la database
> - password: del usuario
> - database: Base de datos a conectarse

Solo hay test del endpoint del item, que era el mas complicado