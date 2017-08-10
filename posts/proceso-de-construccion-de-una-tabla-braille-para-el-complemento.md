<!-- 
.. title: Proceso de construcción de una tabla braille para el complemento
.. slug: proceso-de-construccion-de-una-tabla-braille-para-el-complemento
.. date: 2017-05-25 09:12:09 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Iván Novegil
-->

Nota: Este post ha sido construido a partir de la información proporcionada por Alberto Zanella y nuestra experiencia propia construyendo esta tabla.

Tenía en mente hacer algo como este post dese hace unos días, en inglés o español. Dado que la intención de este complemento es que se expanda a los más idiomas posibles, hago este manual para que cada uno pueda hacer la tabla en el suyo a partir del .jbt de los scripts de Jaws. Como el sitio es en español, no quedará más remedio que hacerla en ese idioma, google Translate is your friend.

1. Localizamos la tabla LambdaX.jbt en Inicio>Jaws X.Y>Explorar archivos de Jaws>Explorar archivos de programa o en C:\Archivos de programa\Freedom Scientific\Jaws\X.Y, donde X es la versión mayor (16, 17, 18, etc.) e Y la menor (normalmente 0, pero puede variar, sobre todo para versiones anteriores a Jaws8). En esa tabla encontraremos una lista de signos como la que sigue:

	\1 = 123

	\2 = 456

	\3 = 567

2. Tenemos que convertir los números a la izquierda de la tabla a hexadecimal, que es lo que usa Liblouis, que es el motor braille de NVDA. Para ello podemos usar el `[script dec2hex por José Manuel Delicado](/linked_files/dec_to_hex.py). Podemos ejecutar en Python:

		import dec_to_hex
		dec_to_hex.procesar("LambdaX.jbt")

	Esto devolverá un txt en el mismo sitio donde se ejecutó el código llamado LambdaX.txt con el mismo formato pero con números hexadecimales en lugar de decimales a la izqueirda. En ambas, lo que figura a la derecha son los patrones de puntos. En las tablas de Liblouis encontraremos un formato algo diferente: categoría símbolo/representación-hexadecimal(\X0000, por ejemplo \X001a, después de la X van cuatro caracteres, si no se llega a ese número rellenar con ceros a la izquierda, por ejemplo para el carácter anterior 1a se ponen dos ceros de forma que \X001a) patrón-puntos.

3. Una vez se han convertido, queda el trabajo más arduo. Comparar los valores de puntos de la tabla de NVDA con los de Jaws. Para eso necesitamos descargar las tablas de Liblouis. Con Git (si no tienes Git, recomendable descargarlo), ejecutar desde la consola:

		git clone https://github.com/liblouis/liblouis

	Obtendremos una carpeta llamada Liblouis. Dentro de ella iremos a tables y buscaremos la nuestra, normalmente algo así como X_G0.utb (las G1 son de 6 puntos y no nos interesan) o X-8.utb/X-8dots.utb. Para incluirla en el addon y testearla, necesitamos bajarlo, también usando Git, ejecutando:

		git clone https://github.com/nvdaaddons/lambda

	Tendremos una carpeta "lambda". Tendremos que entrar y navegad a ddon>appModules>LAMBDA>brailleTables. Pegamos la tabla que copiamos desde la carpeta tables de Liblouis y la renombramos al estilo de los archivos que ya están en esa carpeta (lambda-X.utb).

4. Primero deberíamos comprobar los include de la tabla, haciendo una búsqueda con la función buscar del editor con que la abramos (se recomienda Notepad++). Si el include hace referencia a un archivo que no está en la carpeta brailleTables que tendremos abierta en otra ventana debemos buscar ese archivo en Liblouis (por lo general en la carpeta tables) y pegarlo, sin cambiar el nombre, para que la tabla pueda utilizar las dependencias que necesite. En el caso de nuestra tabla, la española, no fue necesario ya que todas las dependencias de la española las requería también la italiana que ya estaba hecha.

5. Después, se empiezan a verificar todos los símbolos (obviando ciertas categorías, como letras o números, aunque si las cotejamos no debería llevarnos más de 3 horas toda la tabla). Recomiendo ir marcando en el txt que generó el script en el paso 2 (con * o lo que nos sea más cómodo) los símbolos que ya hayamos verificado, luego nos será útil a la hora de añadir aquellos símbolos que falten. Debemos modificar los puntos de aquellos símbolos que estén mal primero, y posteriormente añadir todos los que no figuran en la tabla. En este punto yo personalmente al hacer la tabla no fui demasiado meticuloso, asigné a todos la categoría math y no puse descripción porque los que hicieron la tabla de Jaws se ve que tampoco tenían demasiado tiempo como para ponerse a mirar qué era cada símbolo y ponerlo como comentario. Para añadir símbolos, por ejemplo, si en el txt tenemos b1 345678 podemos poner: math \X00b1 345678.

6. Si has hecho todo esto con éxito, felicidades, lo esencial está completado. Necesitas probar la tabla con NVDA o con lou_debug, lo que esté a tu alcance. Desconozco si hay versión de Liblouis para instalar en windows, pero para Linux la hay y me fue muy útil a la hora de depurar errores en la tabla. Si tenéis por ahí un servidor o máquina virtual solo es cosa de bajarse Liblouis o el código (si es el código compilarlo con make && make install) y pasaros a la MV o servidor el utb. Después de eso:

		lou_debug LambdaX.utb

	Entonces debería decir qué errores ha encontrado y la línea. Para ir a una línea X en el Notepad++ podemos usar Ir a la línea... en el menú buscar (ctrl+G). Si no tienes lou_debug o alguna herramienta de depuración de Liblouis a tu alcance, te tocará hacerlo de la forma chapuza, a mano. A mí me dio demasiada pereza ponerme a verificar qué había hecho mal (además de que seguramente algunos errores no sería capaz de encontrarlos) y busqué, en su lugar, lo de la depuración en Liblouis que cuento al principio de este paso. <!-- ToDo: Mirar si hay debugging para windows y especificarlo.-->

7. Si has depurado todos los errores, enhorabuena, tu tabla debería funcionar con el complemento. compila el complemento si tienes las herramientas necesarias (solo tecla scons en una ventana del símb del sistema u otra consola debidamente configurada), o añade el utb en %appdata%\nvda\addons\lambda\appModules\LAMBDA\brailleTables. Reinicia NVDA.

8. Una vez que no haya ningún error ponte en contacto con el autor o envía una pull request al repo nvdaaddons/lambda de GitHub con la tabla  para que la incluya (cómo enviar pull requests en GitHub está fuera del propósito de este documento). Si la acepta, no olvides ponerte en contacto con el traductor del idioma (o de los idiomas) a los que corresponde tu tabla para avisarle de que la haga predeterminada para todos los que instalen el complemento en ese/esos idioma/s. Si no sabes el traductor de tu idioma busca y subscríbete a la lista de traducciones de NVDA; allí podrás preguntar. Tambien puedes hacer de detective y mirar quién hace commits en tu/s idioma/s en el repo screenReaderTranslations de assembla.com.


Y esto es todo, no tiene mucho más. Gracias por tragaros el tocho. Ah, y suerte.
***La tabla españoala fue construída ena colaboración entre José Manuel Delicado, Salva Doménech y yo, con el autor. Agradecimiento especial a José Enrique Fernández del Campo por sus detallados reportes de errores que intentamos corregir antes de la publicación de la tabla.***