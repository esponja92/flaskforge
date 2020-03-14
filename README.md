###FLASK FORGE

Este projeto contêm

1) uma ferramenta para geração de tabelas em um banco SQLite3
2) uma biblioteca simples para ORM

Para rodar a aplicação de exemplo:

1) Execute dbgen.py na pasta tools e crie uma tabela chamada "pessoa" com os seguintes campos:
	- "fname" tipo TEXT
	- "lname" tipo TEXT
2) Na raiz do projeto execute

$ python3 app.py

e acesse o endereço localhost:8000/

O Model Pessoa deve conter atributos começando com "campo_" e seguidos dos nomes das colunas
da tabela pessoa:
	- campo_fname = 'Nome inicial'
	- campo_lname = 'Nome final'

CRÉDITOS:
	- estrutura do projecto MVC baseada no projeto em https://github.com/indhifarhandika/flask-mvc