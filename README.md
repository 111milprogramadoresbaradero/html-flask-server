# Servidor HTML sobre Python Flask

## Pasos para la instalación

1. Instalar [Docker](http://docker.io)
2. Crear imagen:
 
	`docker build --tag curso111-flask-server .`
	
3. Crear contenedor:

	`docker run --name curso111-server -p 9200:9200 -d curso111-flask-server`

4. Acceder al servidor desde el browser en la URL http://localhost:9200