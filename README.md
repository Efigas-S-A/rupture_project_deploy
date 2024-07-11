# rupture_project

Este repositorio contiene un proyecto desarrollado específicamente para empresas del sector gasero interesadas en estudiar y analizar roturas en tuberias causadas por terceros. El objetivo principal es proporcionar herramientas y análisis que permitan mejorar la gestión y mantenimiento de las infraestructuras de tuberías utilizadas en la industria del gas, y los volumenes de gas emitidos por las roturas.

## Tabla de Contenidos

1. descarga del proyecto
2. Creación del entorno virtual
3. Instalación de dependencias
4. Creación de variables de entorno
5. Ejecución del proyecto
6. Recomendaciones

## Descarga del proyecto

Para obtener una copia del proyecto y empezar su proceso de despliegue es necesario clonar este repositorio para esto es necesario tener instalado git en el sistema operativo correspondiente.

Instalación de git 

* Windows
  1) Descargar Git desde [git-scm.com](https://git-scm.com/).
  2) Ejecutar el instalador y seguir las instrucciones.

* macOS (desde consola)
  1) Instalar git usando Homebrew:
    ```bash
       brew install git
* Linux (desde consola)
   ```bash
      sudo apt update
      sudo apt install git

Una vez instalado git en el sistema operativo correspondiente, desde una consola de comando y configurar las credenciales de git asociadas a la cuenta de git de la siguiente manera:

   ```bash
      git config --global user.name "Tu Nombre"
      git config --global user.email "tu_correo@ejemplo.com"
   ```
Clonar el repositorio del proyecto (DESDE CONSOLA)
definida las credenciales ya podemos clonar este proyecto en una carpeta dentro de nuestra pc, para esto dentro de una consola de comando y ubicandonos en la ruta de la carpeta donde queremos ubicar el proyecto ejecutar el siguiente comando
   
   ```bash
      git clone https://github.com/Efigas-S-A/rupture_project.git
    ```
Esto clonara una carpeta con el proyecto, con lo cual con el comando "cd rupture_project" , podemos dirigirnos a la carpeta del proyecto donde encontraremos todos los elementos para ejecutar la aplicación, la cual podemos abrir en un IDE de codigo como visual studio code mediante el comando "code ./" en caso tal de que ya lo tengamos instalado.


## Creación del entorno virtual
ubicados en la carpeta clonada rupture_project/, y con python instalado en el pc, realizamos la creación del entorno virtual de trabajo, mediante el siguiente comando en consola
  ```bash
        python -m venv venv
   ```
esto creara una carpeta venv en el proyecto, y como siguiente paso activamos el entorno, lo cual puede variar dependiendo del sistema operativo utilizado

 * Windows
   ```bash
        .\venv\Scripts\activate
    ```
* Linux / mac OS
    ```bash
        source ./venv/bin/activate
     ```
a lo cual debe aparecer en consola al inicio de la ruta actual  las siglas "(venv)" que indicaran que el entorno se encuentra activado.

## Instalación de dependencias
  Con el entorno virtual activado realizamos una actualización del comando pip que es el que nos permitira instalar los paquetes de python necesarios para correr la aplicación
  * Windows
    ```bash
        python.exe -m pip install --upgrade pip
     ```
  * Linux
    ```bash
        pip install --upgrade pip
     ```

  Una vez actualizado instalamos las dependencias con el archivo requirements.txt que esta presente en el proyecto desde la consola de la siguiente manera
    ```bash
        pip install -r requirements.txt
     ```

  Con esto tenemos todos los paquetes de python necesarios para ejecutar nuestra aplicación, solo falta un paso para completar todos los requerimientos necesarios y es crear las variables de entorno que nuestra aplicación necesita para poder ejecutar los procesos que realiza.

## Creación de variables de entorno
Para crear las variables de entorno varia despendiendo del sistema operativo 

* Windows

 1) Abre una powershell de windows y ejecuta el siguiente comando para crear las variables de entorno
    ```bash
          setx NOMBRE_VARIABLE "Valor_variable"
     ```
 * Linux

    1)  Abre una terminal.
    
    2) Edita tu archivo de perfil del shell (por ejemplo, `~/.bashrc` o `~/.profile`):
    
       ```bash
       nano ~/.bashrc
        ```
    3) Dentro del archivo bashrc ubica la variable de la siguiente manera:

       export MI_VARIABLE="valor_de_mi_variable"

Las variables a crear son:

- MAIL_SERVER => Corresponde a el servidor SMTP de preferencia asociado al servidor del correo es decir si es gmail o outlook etc por ejemplo si es gmail el valor seria smtp.gmail.com
- MAIL_PORT => el puerto del servidor SMTP que se requiere y por el cual se envian los correos.  por ejemplo para gmail seria el puerto 587
- MAIL_USERNAME => seria el correo desde el cual se van a enviar los mails de creación de usuario, recuperación de cuentas y demas y que esta asociado al MAIL_SERVER seleccionado-
- MAIL_PASSWORD => hace referencia a la contraseña de aplicación creada para el correo seleccionado, este se debe crear desde gmail o microsoft dependiendo del tipo de correo seleccionado no corresponde a la contraseña del correo como tal, se debe crear una contraseña de aplicación.
- MAIL_DEFAULT_SENDER => corresponde al mismo MAIL_USERNAME
- KEY_APP => corresponde a la llave unica que identifica el inicio de sesión de la aplicación debe ser de tipo LLAVE PARA ENVOLVER LA APLICACIÓN TIENE QUE SER EN EL FORMATO HEXADECIMAL Y LUEGO SE PASA A CADENA DE BYTES QUE TERMINA SIENDO DEL FORMATO b''
- ENCRIPT_KEY => LLAVE QUE REPRESENTA EL TIPO DE ENCRIPTACIÓN QUE SE LE REALIZARA A LAS CONTRASEÑAS E INFORMACIÓN DEL USUARIO TIENE QUE SER EN EL FORMATO HEXADECIMAL PARA LUEGO SER PASADA A CADENA DE BYTES QUE TERMINA SIENDO DEL FORMATO b'' ESTA LLAVE SE USA CON LA LIBRERIA pyDes de python que permite realizar encriptaciones, para codificar mi llabe de cadena de bytes a hexadecimal usar el codigo de python:

```bash
      hex_key = secret_key.hex() ## DONDE secret_key es una cadena de bytes en b''

 ```
Para verificar donde se usan dichas variables, mirar el archivo rl.py lineas 18 a la 27

FINALMENTE EN CASO DE QUE LA APLICACIÓN ESTE SIENDO DESPLEGADA CON UN DOMINIO DETERMINADO SERA NECESARIO EDITAR TODAS LAS PORCIONES DE CODIGO DONDE SE TIENE
http://localhost:5000 => dominio respectivo. ejemplo https://ruptures.projecthub.site


## RECOMENDACIONES

El proyecto suministrado es un proyecto que sirve como demo para demostrar el funcionamiento base de la aplicación, pero no esta desarrollado en su totalidad para un despliegue un puesta en producción, en caso tal de que se desee realizar algo parecido, es necesario tener presente lo siguiente:

 - El sistema no cuenta con una base de datos para su despliegue, en esta se esta simulando dicha conexión mediante el uso de 3 archivos excel, que son usuarios.xlsx,solicitudes.xlsx y la carpeta eventos donde se registran los sucesos registrados en la plataforma, por ende a la hora de pensar en un despliegue producto sera necesario cambiar la funcionalidad de la aplicación a una conexión a una base de datos que se estipule ya sea de tipo SQL o No SQL como mongo.
-  Las variables de acceso a la base de datos nueva, para un despliegue deben quedar tambien referidas mediante variables de entorno para evitar fallas de seguridad a la hora del despliegue.
-  El correo asociado a los mensajes debe ser un correo que haga parte del directorio activo de la institución que lo vaya a utilizar, para evitar fallas por bloqueos de spam y demas situaciones que se pueden presentar debido a la diferencia entre el dominio del correo y los correos de la empresa.

- En caso de querer generar un repo nuevo en base al proyecto realizado generar un fork desde github.




