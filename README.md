# Blueprint de micro servicio



## Como empezar a trabajar con el blueprint

Los siguientes pasos son necesarios para trabajar con el blueprint.

* Clonar el repositorio.
* Crear un nuevo directorio limpio.
* Copiar los archivos del repositorio al nuevo directorio, incluya todo menos el directorio .git.
* En el nuevo directorio hacer git init.
* Definir el repositorio remoto.
* Hacer commit del código en el nuevo repositorio.
* Instalar el pyenv según como se describe en https://github.com/pyenv/pyenv#installation.
* Instalar la version de python 3.9.6 con `pyenv install 3.9.6`. La version puede variar de acuerdo a los requerimientos,
  revisar la version en el archivo Pipfile.
* Definir la version de python en el directorio de trabajo con `pyenv local version`.
* Dentro del directorio de trabajo instalar `pipenv` con el comando `pip install pipenv`.
* Para crear el ambiente virtual e instalar los paquetes requeridos, se hace con el comando `pipenv install` dentro del
  directorio de trabajo, para `pipenv` los ambientes virtuales están definidos por el directorio. Luego instalar los
  paquetes de desarrollo con `pipenv install --dev`, es obligatorio instalar los paquetes de --dev.
* Para ejecutar un único comando dentro del ambiente virtual se usa `pipenv run comando`.
* Para activar el ambiente virtual ejecutar `pipenv shell`.
* Luego de activado el ambiente virtual los paquetes instalados estarán disponibles.

### MUY IMPORTANTE

El blueprint hace uso del nombre _microservice_ a modo de ejemplo, es **_necesario_** modificar el código para que refleje
un nombre significativo para el paquete del micro servicio. Esto significa reemplazar todas las ocurrencias de _microservice_
en el código por un nombre de paquete más adecuado. Cambiar también los datos dentro del archivo `setup.py` con valores
que representen al micro servicio.

## Sincronizar `setup.py`

Es necesario mantener al dia el archivo setup.py con las dependencias que se instalen, para hacer la sincronización
ejecute `pipenv-setup sync` dentro del ambiente virtual del micro servicio.

## Linters y hooks de pre commit

Se agregaron varios linters en la sección de paquetes de dev:

* black https://black.readthedocs.io/en/stable/
* pylint http://pylint.pycqa.org/en/latest/
* mypy https://mypy.readthedocs.io/en/stable/
* pydocstyle http://www.pydocstyle.org/en/stable/
* pycodestyle https://pycodestyle.pycqa.org/en/latest/

Para manejar los hooks de pre commit se está usando https://pre-commit.com/ que se va a instalar con los paquetes de dev
de Pipfile, los linters que se están aplicando en el hook son: pylint, pydocstyle, pycodestyle.

Active los hooks de pre commit, haciendo `pre-commit install`, esto evaluará el código antes de llevar a cabo el commit
para asegurar la limpieza y el apego a los estándares del código.

Los linters se pueden aplicar por separado, ejecutándolos desde la línea de comando dentro del ambiente virtual. Para
más information sobre su uso consulte la página que corresponda al linter que desee usar.
