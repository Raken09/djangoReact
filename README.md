# Aplicacion que utiliza django para el backend y react vite para el frontend.

## Back end
Para el backend con django, se realizó un deploy en render.com, con el fin de realizar las consultas desde dicha dirección, para acceder a la appi se definió el siguiente enlace: https://proyectodjango-bgg5.onrender.com/appUsers/api/.

Para acceder a el usuario (o los) admin, se utiliza la siguiente ruta mediante peticion GET: https://proyectodjango-bgg5.onrender.com/appUsers/api/usuarioadmin/
Para acceder a los usuarios regulares se utiliza la siguiente ruta mediante petición GET: https://proyectodjango-bgg5.onrender.com/appUsers/api/usuarioregular/

Los usuarios admin y los usuarios regulares se crearon de manera automatica con un script personalizado llamado [crearUsuarios.py](https://github.com/Raken09/djangoReact/blob/ceb5b674dc5299a45a0ebf611c4113bdf0cff051/appUsers/management/commands/crearUsuarios.py), el cual crea los usuarios en la base de datos de acuerdo a los modelos definidos.

Render.com permite crear bases de datos con PostgreSQL basandose en los modelos de django, por lo tanto una vez hecho el deploy de la aplicacion los datos quedan guardados en la base de datos definida en render.com.

## Conexion backend-frontent

Para conectar django con react, se definió una api [apiUsuarios](https://github.com/Raken09/djangoReact/blob/ceb5b674dc5299a45a0ebf611c4113bdf0cff051/FrontEnd/src/api/apiUsuarios.js) utilizando axios con el fin de realizar las diferentes peticiones a la base de datos.

## Frontend

Para el desarrollo del frontend se utilizó react.js junto co vite el cual dependiendo de la aplicacion tiene ventajas sobre otras herramientas como webpack, todo el codifo del frontend se encuentra en la carpeta [FrontEnd](https://github.com/Raken09/djangoReact/tree/ceb5b674dc5299a45a0ebf611c4113bdf0cff051/FrontEnd) 

Por ultimo mi idea era hacer deploys para el backend y frontend de manera independiente pero que existiera la conexion entre ambas partes, con el fin de que se pudieran optimizar de mejor manera ambas partes del proyecto, se que no pude completar la tarea en su totalidad y si llegaste hasta aquí te agradezco mucho, no queria terminar el reto sin entregar nada, me pareció un muy buen desadfio y pienso terminarlo por mi cuenta con el fin de practicar y adquirir mas conocimientos, ya que django no es una tecnologia que utilizo mucho, le dediqué mas tiempo a dicha prarte, dandome cuenta de todas las ventajas que tiene desarrollar el back en dicha tecnologia la cual pienso utilizar mas.
