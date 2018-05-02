#  Proyecto Cognitiva
Este proyecto fue desarrollado con Flask.

## Servidor de desarrollo
Para poder correr el servidor de desarrollo se necesitan tener instaladas las siguientes dependencias:

- flask
- flask_cors
- sklearn
- pandas

El objetivo de estas dependendencias es el siguiente:

- flask: Flask nos permite crear un servidor para aplicaciones Python sobre el cual podemos montar nuestra aplicación.

- flask_cors: El único objetivo de esta dependencia es que no se bloqueen las peticiones del frontend ya que este está alojado en su propio servidor y las peticiones de otro origen son bloqueadas por default.

- sklearn: Es la dependencia más importante, esta es la que nos permite crear el modelos de ML, para nuestro caso es un modelo de aprendizaje supervisado de RandomForest.

- pandas: Es una librería que nos proporciona estructuras de datos que nos facilitan el analisis de datos para nuestro dataset.

- graphviz: Esta librería se usó para generar el diagrama del modelo que se había demostrado anteriormente.  