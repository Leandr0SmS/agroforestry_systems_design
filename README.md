# agroforestry_systems_design
Project to design agroforestry systems based on their plants, each with its own light requirements and spacing.

## Executar

- [Localmente com Python, venv e pip](#localmente-com-python)
- [Replit](#replit)
- [Docker](#executar-com-docker)

### Localmente com Python

Certifique-se de ter o [python](https://www.python.org/) instalado.

Inicializar [virtual environments](https://docs.python.org/3/library/venv.html).

Instalar dependências:

```
(env)$ pip install -r requirements.txt
```

Executar o app com o comando:

```
(env)$ flask run --host 0.0.0.0 --port 5001
```

### Replit:

[[Run on Replit: https://replit.com/@Leandr0SmS/pucrio-mvp1-backend?v=1]](https://replit.com/@Leandr0SmS/pucrio-mvp1-backend?v=1)

### Executar com Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t agroforestry_systems_design .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5001:5001 agroforestry_systems_design
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5001/#/](http://localhost:5001/#/) no navegador.

### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
> Caso queira **remover todas as images**, basta executar o comando:
>```
>$ docker rmi -f $(docker images -aq)
>```
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
> Caso queira **parar todos os conatiner**, basta executar o comando:
>```
>$ docker stop $(docker ps -a -q)
>```
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
> Caso queira **destruir todos os conatiners**, basta executar o comando:
>```
>$ docker rm $(docker ps -a -q)
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).

> **Banco de Dados** - Será iniciado e carregado com informações pré definidas.

## Autor

[Leandro Simões](https://github.com/Leandr0SmS)

## Licença

The MIT License (MIT)
Copyright © 2023 Leandro Simões

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Inspirações

- [PUC-Rio](https://www.puc-rio.br/index.html)
- [CodeCademy](https://www.codecademy.com/)
- [FreeCodeCamp](https://www.freecodecamp.org/learn/)
- [Cepeas](https://www.cepeas.org/)
- [Agenda Gotsch](https://agendagotsch.com/)

