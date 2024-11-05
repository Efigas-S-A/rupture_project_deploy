# Proyecto Flask con MongoDB

Este proyecto es una aplicación Flask . A continuación se describen los pasos necesarios para configurar el entorno y ejecutar la aplicación.

## Requisitos previos
- Tener **Python 3** instalado.

## Pasos de configuración

1. Clona este repositorio en tu máquina local la rama de interes es LocalHost:
   ```bash
   git clone https://github.com/Efigas-S-A/rupture_project_deploy.git
   cd rupture_project_deploy
   git checkout LocalHost
   ```

2. Crea un entorno virtual para instalar las dependencias de Python:
  ```bash
     python3 -m venv venv
  ```

activa el entorno virtual 

3. En Linux/MacOS:

   ```bash
   source venv/bin/activate
   ```

4. En Windows

   ```bash
    .\venv\Scripts\activate
   ```

5. Con el entorno virtual activado, instala las dependencias desde el archivo requirements.txt:

   ```bash
      pip install -r requirements.txt
   ```


6. Finalmente, ejecuta la aplicación Flask:
   ```bash
      python rl.py
   ```




Autor
<Juan Sebastian Mendez> ```