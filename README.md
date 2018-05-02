#  Proyecto Cognitiva
Este proyecto fue desarrollado con Flask.

## Servidor de desarrollo
Para poder correr el servidor de desarrollo se necesitan tener instaladas las siguientes dependencias:

* flask
* flask_cors
* sklearn
* pandas

El objetivo de estas dependendencias es el siguiente:

* flask: Flask nos permite crear un servidor para aplicaciones Python sobre el cual podemos montar nuestra aplicación.

* flask_cors: El único objetivo de esta dependencia es que no se bloqueen las peticiones del frontend ya que este está alojado en su propio servidor y las peticiones de otro origen son bloqueadas por default.

* sklearn: Es la dependencia más importante, esta es la que nos permite crear el modelos de ML, para nuestro caso es un modelo de aprendizaje supervisado de RandomForest.

* pandas: Es una librería que nos proporciona estructuras de datos que nos facilitan el analisis de datos para nuestro dataset.


Una vez que se tienen todas estas dependencias ya se puede correr el servidor de desarrollo de la siguiente manera:

Se tiene que tener los archivos siguientes en el mismo directorio:

* app.py
* inputlabels.sav
* Modelo.py
* outputlabels.sav
* random_forest.sav 

Si ya se tiene eso entoces ya se puede correr el servidor si ejecutamos el comando:

```
python ./app.py
```


## API
Realmente el servidor no tiene base de datos, este servidor es puramente para recibir un input de variables las cuales envía al modelo y este le regresa las predicciones resultantes de las variables.

Solo existe una ruta y esta es la ruta raíz, si se hace un POST se espera un objeto de la siguiente forma:

```
{
  "Music": 1,
  "Music1": "Musical",
  "Music2": "Pop",
  "Music3": "Swing or Jazz",
  "Movies": 1,
  "Movies1": "Sci-fi",
  "Movies2": "Fantasy or Fairy tales",
  "Subject": "History",
  "Pastime": "Art exhibitions",
  "Fear": "Flying",
  "Alcohol": "never",
  "Smoking": "tried smoking",
  "Phrases1": "Healthy eating",
  "Phrases2": "Keeping promises",
  "Phrases3": "Self criticism",
  "Phrases4": "Cheating in school",
  "Punctuality": "i am often early",
  "Lying": "only to avoid hurting someone",
  "Important1": "Waiting",
  "Important2": "Children",
  "Important3": "Energy levels",
  "Internet usage": "few hours a day"
}
```

A esto el modelo responde un objeto JSON de la siguiente forma:

```
{
  "Finances": 5.0, 
  "Shopping centres": 1.0, 
  "Branded clothing": 3.0, 
  "Entertainment spending": 3.0, 
  "Spending on looks": 3.0, 
  "Spending on gadgets": 3.0, 
  "Spending on healthy eating": 4.0, 
  "Age": 20.0, 
  "Education": "secondary school", 
  "Village town": "city", 
  "House": "block of flats"
}
```