###FLASK FORGE

Este projeto contêm

1) uma ferramenta para geração de tabelas em um banco SQLite3
2) uma API simples de acesso a este banco criado

Para rodar a aplicação de exemplo:

1) Execute dbgen.py na pasta tools e crie uma tabela chamada "pessoa" com os seguintes campos:
	- "fname" tipo TEXT
	- "lname" tipo TEXT
2) Na raiz do projeto execute

$ python3 app.py

e acesse o endereço 127.0.0.1:5000/