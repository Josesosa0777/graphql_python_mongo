from os import path
from io import open
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="microservice",  # Required
    version="0.0.1",  # Required
    description="Prueba de concepto de la integracion de graphql con el blueprint",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    author="The Python Packaging Authority",  # Optional
    author_email="pypa-dev@googlegroups.com",  # Optional
    keywords="sample setuptools development",  # Optional
    packages=["microservice"],  # Required
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
    install_requires=[
        "anyio==3.4.0; python_full_version >= '3.6.2'",
        "ariadne==0.14.0",
        "click==8.0.3",
        "dependency-injector[yaml]==4.37.0",
        "flask==2.0.2",
        "graphql-core==3.1.6; python_version >= '3.6' and python_version < '4'",
        "greenlet==1.1.2; python_version >= '3' and platform_machine == 'aarch64' or (platform_machine == 'ppc64le' or (platform_machine == 'x86_64' or (platform_machine == 'amd64' or (platform_machine == 'AMD64' or (platform_machine == 'win32' or platform_machine == 'WIN32')))))",
        "idna==3.3; python_version >= '3.5'",
        "itsdangerous==2.0.1; python_version >= '3.6'",
        "jinja2==3.0.3; python_version >= '3.6'",
        "markupsafe==2.0.1; python_version >= '3.6'",
        "pyyaml==6.0",
        "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "sniffio==1.2.0; python_version >= '3.5'",
        "sqlalchemy==1.4.27",
        "starlette==0.17.1; python_version >= '3.6'",
        "typing-extensions==4.0.1; python_version >= '3.6'",
        "werkzeug==2.0.2; python_version >= '3.6'",
    ],
    extras_require={
        "dev": [
            "appdirs==1.4.4",
            "astroid==2.9.0; python_version ~= '3.6'",
            "asttokens==2.0.5",
            "attrs==21.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "backports.entry-points-selectable==1.1.1; python_version >= '2.7'",
            "black==19.10b0",
            "cached-property==1.5.2",
            "cerberus==1.3.4",
            "certifi==2021.10.8",
            "cfgv==3.3.1; python_full_version >= '3.6.1'",
            "chardet==4.0.0",
            "charset-normalizer==2.0.9; python_version >= '3'",
            "click==8.0.3",
            "colorama==0.4.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "distlib==0.3.4",
            "executing==0.8.2",
            "filelock==3.4.0; python_version >= '3.6'",
            "icecream==2.1.1",
            "identify==2.4.0; python_full_version >= '3.6.1'",
            "idna==3.3; python_version >= '3.5'",
            "isort==5.10.1; python_version < '4' and python_full_version >= '3.6.1'",
            "lazy-object-proxy==1.6.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
            "mccabe==0.6.1",
            "mypy==0.910",
            "mypy-extensions==0.4.3",
            "nodeenv==1.6.0",
            "orderedmultidict==1.0.1",
            "packaging==20.9; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pathspec==0.9.0",
            "pep517==0.12.0",
            "pip-shims==0.6.0; python_version >= '3.6'",
            "pipenv-setup==3.1.4",
            "pipfile==0.0.2",
            "platformdirs==2.4.0; python_version >= '3.6'",
            "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pre-commit==2.16.0",
            "pycodestyle==2.8.0",
            "pydocstyle==6.1.1",
            "pygments==2.10.0; python_version >= '3.5'",
            "pylint==2.12.2",
            "pyparsing==3.0.6; python_version >= '3.6'",
            "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "pyyaml==6.0",
            "regex==2021.11.10",
            "requests==2.26.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
            "requirementslib==1.6.1; python_version >= '3.6'",
            "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "snowballstemmer==2.2.0",
            "toml==0.10.2; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "tomli==1.2.2; python_version >= '3.6'",
            "tomlkit==0.7.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "typed-ast==1.5.1; python_version >= '3.6'",
            "typing-extensions==4.0.1; python_version >= '3.6'",
            "urllib3==1.26.7; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
            "virtualenv==20.10.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "wheel==0.37.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "wrapt==1.13.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        ]
    },  # Optional
    entry_points={"console_scripts": ["microservice=microservice:cli"]},
)
