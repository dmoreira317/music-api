# music
simple-api-code-challenge

## Requirements
- Docker
- docker-compose

To use this API, simply clone the repo and execute:

```docker-compose up music_api```

This will serve the app in dev mode, in port localhost:8000.

Challenge:

Utilizando la siguiente base de datos: https://www.sqlitetutorial.net/sqlite-sample-database/
Se pide que se desarrolle una API de consulta con los siguientes servicios:
- Obtener una lista de todos los músicos / grupos.
    ### SERVED AT:
    ```/artists/```

- Obtener una lista de todos los discos junto con sus canciones.
    ### SERVED AT:
    ```/albums/```

- Dado un músico / grupo, obtener un listado de todos sus discos.
    ### SERVED AT:
    ```/artists/<artist_id>/get_artist_albums/```

- Dado un disco, obtener un listado de todas las canciones.
    ### SERVED AT:
    ```/albums/<album_id>/get_album_tracks/```

- Listado de todos los discos con los siguientes datos agregados:
    - Nombre del músico / grupo.
    - Número total de canciones.
      ### SERVED AT:
    ```/albums_info/```

Deberá utilizarse Python, Docker y ORM para las consultas además de subir el resultado en
un repositorio de GitHub.
