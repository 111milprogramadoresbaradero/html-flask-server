# Servidor HTML sobre Python Flask

## Pasos para la instalación

1. Instalar [Docker](http://docker.io)
2. Crear imagen:
 
	`docker build --tag curso111-flask-server .`
	
3. Crear contenedor:

	`docker run --name curso111-server -p 9200:9200 -d curso111-flask-server`

4. Acceder al servidor desde el browser en la URL http://localhost:9200

## Usando Docker Compose para levantar el contenedor de la aplicación más el contenedor de la base de datos

1. Instalar [Docker Compose](https://docs.docker.com/compose/install/)

2. Ejecutar el siguiente comando desde la carpeta del proyecto:

	`docker-compose up -d`

* Para parar los contenedores usar el siguiente comando:

	`docker-compose kill`

* Para parar los contenedores y eliminarlos usar el siguiente comando:

	`docker-compose down`

* El contenedor de base de datos está basado en la imágen postgres:9.6, los datos son almacenados en la maquina HOST por medio de un volumén que comparte la carpeta './data' del proyecto en la carpeta '/var/lib/postgresql/data' del contenedor.
