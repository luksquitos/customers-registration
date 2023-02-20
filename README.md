# Registro de Clientes

## Introdução
Api de cadastro de clientes com validador de CPF. Foi construída utilizando o framework Django, Django Rest Framework, o banco de dados Postgres e conteirizada com Docker.

## Premissas

- Ter o Docker e Docker Compose instalados na máquina.
- Na raiz do projeto utilizar o comando: `docker-compose up --build`
  
## Configurações iniciais

**Todos os comandos a seguir precisam ser executados no terminal do container.**

**Comando para acessar terminal do container:** 
```
docker exec -it api bash
```

- Rodar as migrates iniciais: Execute `python manage.py migrate` para que as bibliotecas padrões, arquivos estáticos sejam migrados para a base de dados. 

- Rodar as migrations das aplicações 'customers'.
  Utilize o comando `python manage.py makemigrations`, seguido do `python manage.py migrate`. Assim, os serviços presentes na API serão adicionados a base de dados.

**Para sair do terminal do container basta escrever `exit`**

## Endpoints

- `http://localhost:8000/` : Possui as rotas que serão usadas pela aplicação web.

- `localhost:8000/customers/` : 
  - `GET`: Listagem de todos os clientes cadastrados na base de dados. 
  - `POST`: Criação de um novo cliente na base de dados
    ```json
    {
        "name": "Walter Branco",
        "birth": "1980-03-10",
        "cpf": "785.023.120-14"
    }
    ```
    > Obs: Caso CPF seja inválido, cliente não será cadastrado.

- `localhost:8000/customers/{pk}/` :
  - `GET`: Detalhes do cliente {pk}
  - `PATCH`: Updates parciais no cliente.
    ```json
    {
        "cpf": "847.610.520-74"
    }
    ```
  - `PUT`: Updates totais do cliente
    ```json
    {
        "name": "Kratos Bom de Guerra",
        "birth": "1904-03-10",
        "cpf": "256.702.260-03"
    }
    ```
- `localhost:8000/customers/?search={cpf}`: Pesquisa de algum CPF em específico
**OBS: Pesquisa deve ser feita sem aspas**

- `localhost:8000/customers/?page={integer}`: Sistema de páginas no endpoint

## Bibliotecas utilizadas
- [Django](https://www.djangoproject.com/start/overview/)

- [Django Rest Framework](https://www.django-rest-framework.org/)

## Contatos
- [LinkedIn](https://www.linkedin.com/in/lucas-martins-caetano/)
- [Email](mailto:lucas.caetano@aluno.unievangelica.edu.br)