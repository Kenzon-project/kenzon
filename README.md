<h1 align="center">Kenzon Ecommerce</h1>
 <p align="center"> Esta é uma aplicação backend sobre um ecommerce, contém cadastro de usuários, cadastro de produtos, e vendas</p>

 <p align="center">
  <a href="#endpoints">Endpoints</a>
</p>

## **Endpoints**

A API tem um total de 5 endpoints, podendo cadastrar usuários, realizar login, cadastrar produtos, inserir item no carrinho, e realizar pedidos. <br/>

<a href="https://insomnia.rest/run/?label=Kenzon-API&uri=https%3A%2F%2Fgithub.com%2FKenzon-project%2Fkenzon%2Fblob%2Fdevelop%2FKenzon_Insomnia" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>

<blockquote> Para importar o JSON no Insomnia é só clicar no botão "Run in Insomnia". Depois é só seguir os passos que ele irá importar todos os endpoints em seu insomnia.
</blockquote>
<br>

A url base da API é https://kenzon-ecomerce.onrender.com

<h2 align ='center'>Usuários</h2>

<h3> Criação de usuário </h3>

`POST /api/users/ - FORMATO DA REQUISIÇÃO`

```json
{
  "first_name": "Julia",
  "last_name": "Pereira",
  "email": "julia@email.com",
  "cpf": 58326892831,
  "birthdate": "1995-07-20",
  "password": "1234",
  "address": {
    "bairro": "Centro",
    "rua": "Avenida Getúlio Vargas",
    "numero": 19,
    "cidade": "Arraial do Cabo",
    "estado": "RJ",
    "cep": 28930970,
    "complemento": "Loja A"
  }
}
```

Caso dê tudo certo, a resposta será assim:

`POST /api/users/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "username": "Julia3FSDH",
  "first_name": "Julia",
  "last_name": "Pereira",
  "email": "julia@email.com",
  "cpf": 58326892831,
  "birthdate": "1995-07-20",
  "is_seller": false,
  "is_admin": false,
  "address": {
    "id": 4,
    "bairro": "Centro",
    "rua": "Avenida Getúlio Vargas",
    "numero": "19",
    "cidade": "Arraial do Cabo",
    "estado": "RJ",
    "cep": 28930970,
    "complemento": "Loja A"
  },
  "carrinho": 1,
  "produtos": []
}
```

Para criar um vendendor, é só acrescentar a chave "is_seller: true" na requisição!
Para criar um administrador, é só acrescentar a chave "is_admin: true" na requisição!

<h4 align ='center'> Possíveis erros </h4>

Caso você acabe errando e mandando algum campo errado, a resposta de erro será assim:

Email ou CPF repetidos:

`POST /api/users/`

`FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "email": ["This field must be unique."],
  "cpf": ["user with this cpf already exists."]
}
```

<h3> Busca de usuários </h3><br/>

Somente administrador tem acesso a essa rota.
Não é necessário um corpo da requisição.
`GET /api/users/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "count": 4,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "userSeller10FSDH",
      "first_name": "userSeller1",
      "last_name": "LastName",
      "email": "userSeller1@email.com",
      "cpf": 4541239786,
      "birthdate": "1995-07-20",
      "is_seller": true,
      "is_admin": false,
      "address": {
        "id": 1,
        "bairro": "Barra",
        "rua": "Avenida 81",
        "numero": "55",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "cep": 2536985,
        "complemento": "Nenhum"
      },
      "carrinho": 1,
			"produtos": [
				{
					"id": 1,
					"nome": "Mesa de Escritório",
					"descricao": "Mesa de Escritório em L Estilo Industrial 1,50mX1,50m Kuadra, Trevalla, Preto Ônix/Est.Preta",
					"img": "https://m.media-amazon.com/images/I/71vJtkqhn+L._AC_SY300_SX300_.jpg",
					"valor": "399.94",
					"vendidos": 19,
					"quantidade_estoque": 31,
					"disponibilidade": true,
					"user": "userSeller10FSDH",
					"categorias": [
						{
							"id": 1,
							"nome": "Casa"
						}
					]
        },
      ]
    },
    .
    .
    .
  ]
}
```

Não é necessário um corpo da requisição mas será necessária a autorização de admin.

`GET /api/users/:id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 2,
  "username": "userSeller21FSDH",
  "first_name": "userSeller2",
  "last_name": "LastName",
  "email": "userSeller2@email.com",
  "cpf": 4541235636,
  "birthdate": "1995-07-20",
  "is_seller": true,
  "is_admin": false,
  "address": {
    "id": 2,
    "bairro": "Barra",
    "rua": "Avenida 81",
    "numero": "89",
    "cidade": "Rio de Janeiro",
    "estado": "RJ",
    "cep": 2536985,
    "complemento": "Nenhum"
  },
  "carrinho": 2,
  "produtos": [
    {
      "id": 3,
      "nome": "Geladeira Brastemp French",
      "descricao": "O Refrigerador Brastemp Frost Free French Door 554 Litros Inox BRO85AK – 127 Volts, traz mais tecnologia e sofisticação para a sua cozinha. Tecnologia Inverter A+++: Com a tecnologia inverter A+++, o refrigerador Brastemp economiza até 30% de energia e mantém a temperatura estável, ajudando na preservação dos alimentos.",
      "img": "https://m.media-amazon.com/images/I/41lgp8caWoL._AC_SX425_.jpg",
      "valor": "6399.00",
      "vendidos": 21,
      "quantidade_estoque": 89,
      "disponibilidade": true,
      "user": "userSeller21FSDH",
      "categorias": [
        {
          "id": 3,
          "nome": "Eletrodomésticos"
        }
      ]
    },
    {
      "id": 4,
      "nome": "LEGO® Classic Blocos",
      "descricao": "LEGO® Classic Blocos Transparentes Criativos; Kit de Construção para Crianças (500 peças)",
      "img": "https://m.media-amazon.com/images/I/81+xlh0eUIL._AC_SX425_.jpg",
      "valor": "204.15",
      "vendidos": 22,
      "quantidade_estoque": 78,
      "disponibilidade": true,
      "user": "userSeller21FSDH",
      "categorias": [
        {
          "id": 4,
          "nome": "Brinquedos"
        }
      ]
    }
  ]
}
```

Todos os usuários tem acesso a essa rota, porém é necessário estar autenticado

`GET /api/users/perfil/:username - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "username": "userSeller21FSDH",
  "email": "userSeller2@email.com",
  "is_seller": true,
  "address": [
    {
      "cidade": "Rio de Janeiro",
      "estado": "RJ"
    }
  ],
  "produtos": [
    {
      "id": 3,
      "nome": "Geladeira Brastemp French",
      "descricao": "O Refrigerador Brastemp Frost Free French Door 554 Litros Inox BRO85AK – 127 Volts, traz mais tecnologia e sofisticação para a sua cozinha. Tecnologia Inverter A+++: Com a tecnologia inverter A+++, o refrigerador Brastemp economiza até 30% de energia e mantém a temperatura estável, ajudando na preservação dos alimentos.",
      "img": "https://m.media-amazon.com/images/I/41lgp8caWoL._AC_SX425_.jpg",
      "valor": "6399.00",
      "vendidos": 21,
      "quantidade_estoque": 89,
      "disponibilidade": true,
      "user": "userSeller21FSDH",
      "categorias": [
        {
          "id": 3,
          "nome": "Eletrodomésticos"
        }
      ]
    },
    {
      "id": 4,
      "nome": "LEGO® Classic Blocos",
      "descricao": "LEGO® Classic Blocos Transparentes Criativos; Kit de Construção para Crianças (500 peças)",
      "img": "https://m.media-amazon.com/images/I/81+xlh0eUIL._AC_SX425_.jpg",
      "valor": "204.15",
      "vendidos": 22,
      "quantidade_estoque": 78,
      "disponibilidade": true,
      "user": "userSeller21FSDH",
      "categorias": [
        {
          "id": 4,
          "nome": "Brinquedos"
        }
      ]
    }
  ]
}
```

Caso o usuário não seja encontrado:

`FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

<h3> Exclusão de usuários </h3><br/>
Somente administrador tem acesso a essa rota.

`DELETE /api/users/:id - FORMATO DA RESPOSTA - STATUS 204`

<h3> Alteração de usuários </h3><br/>

Somente o próprio usuário pode acessar:

`PATCH /api/users/:id `

`- FORMATO DA REQUISIÇÃO`

Campos que pode ser atualizados:<br/>

<ul>
	<li>- first_name,</li>
	<li>- last_name,</li>
	<li>- email,</li>
	<li>- birthdate,</li>
	<li>- is_seller,</li>
	<li>- address":<ul>
		<li>- bairro,</li>
		<li>- rua",</li>
		<li>- numero,</li>
		<li>- cidade,</li>
		<li>- estado,</li>
		<li>- cep,</li>
		<li>- complemento</li></ul>
	</li>
  </ul>

```json
{
  "email": "julia123@email.com"
}
```

`FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 1,
  "username": "Julia3FSDH",
  "first_name": "Julia",
  "last_name": "Pereira",
  "email": "julia123@email.com",
  "cpf": 58326892831,
  "birthdate": "1995-07-20",
  "is_seller": false,
  "is_admin": false,
  "address": {
    "id": 4,
    "bairro": "Centro",
    "rua": "Avenida Getúlio Vargas",
    "numero": "19",
    "cidade": "Arraial do Cabo",
    "estado": "RJ",
    "cep": 28930970,
    "complemento": "Loja A"
  },
  "carrinho": 1,
  "produtos": []
}
```

<hr/>
<h2 align = "center"> Login </h2>

`POST /api/users/login/ - FORMATO DA REQUISIÇÃO`

```json
{
  "email": "julia@email.com",
  "password": "1234"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /api/users/login/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NDE5NDMzOCwiaWF0IjoxNjgzNTg5NTM4LCJqdGkiOiI5YjgzNDM1MGZmZDI0NDIzOGQ5OTBlNzdlYzEzOTZkNiIsInVzZXJfaWQiOjF9.P_P0TO78e02yBpYxNUtduuEltQ717jTLbvga49YhKLI",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNjQzNTM4LCJpYXQiOjE2ODM1ODk1MzgsImp0aSI6IjRkMzc4MWFmNGI1NDRkOGZhZGNhZDdhNmYyMmI0YjRlIiwidXNlcl9pZCI6MX0.ufnPHJKDSaALYvab6Xlzm3kv77hc-IO3M6-UJMmbDoo"
}
```

<h3 align ='center'> Possíveis erros </h3>

Caso seja enviado algum dado não registrado:

`POST /api/users/login/`
`FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "detail": "No active account found with the given credentials"
}
```

<hr/>

<h2 align ='center'>Produtos</h2>

<h3> Cadastro de produtos </h3><br/>
Somente vendedor tem acesso a essa rota.<br/>
Categorias disponíves para o cadastro:

<ul>
    <li>"Informática"</li>
    <li>"Eletrodomésticos"</li>
    <li>"Casa"</li>
    <li>"Livros"</li>
    <li>"Eletrônicos"</li>
    <li>"Games"</li>
    <li>"Brinquedos"</li>
    <li>"Crianças"</li>
    <li>"Not Informed"</li>
</ul>

`POST /api/produtos/ - FORMATO DA REQUISIÇÃO`<br/>

```json
{
  "nome": "Mesa de Escritório",
  "descricao": "Mesa de Escritório em L Estilo Industrial 1,50mX1,50m Kuadra, Trevalla, Preto Ônix/Est.Preta",
  "valor": 399.94,
  "quantidade_estoque": 50,
  "img": "https://m.media-amazon.com/images/I/71vJtkqhn+L._AC_SY300_SX300_.jpg",
  "categorias": [
    {
      "nome": "Casa"
    }
  ]
}
```

`POST /api/produtos/ - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "nome": "Mesa de Escritório",
  "descricao": "Mesa de Escritório em L Estilo Industrial 1,50mX1,50m Kuadra, Trevalla, Preto Ônix/Est.Preta",
  "img": "https://m.media-amazon.com/images/I/71vJtkqhn+L._AC_SY300_SX300_.jpg",
  "valor": "399.94",
  "vendidos": 0,
  "quantidade_estoque": 50,
  "disponibilidade": true,
  "user": "userSeller10FSDH",
  "categorias": [
    {
      "id": 1,
      "nome": "Casa"
    }
  ]
}
```

<h3> Busca de produtos </h3><br/>

`GET /api/produtos/ - FORMATO DA RESPOSTA - STATUS 200`<br/>
Todos os usuários tem acesso a essa rota, não é necessário estar autenticado.<br/>
Não é necessário um corpo da requisição.

```json
{
	"count": 4,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"nome": "Mesa de Escritório",
			"descricao": "Mesa de Escritório em L Estilo Industrial 1,50mX1,50m Kuadra, Trevalla, Preto Ônix/Est.Preta",
			"img": "https://m.media-amazon.com/images/I/71vJtkqhn+L._AC_SY300_SX300_.jpg",
			"valor": "399.94",
			"vendidos": 19,
			"quantidade_estoque": 31,
			"disponibilidade": true,
			"user": "userSeller10FSDH",
			"categorias": [
				{
					"id": 1,
					"nome": "Casa"
				}
			]
		},
    .
    .
    .
  ]
}
```

Podemos utilizar os query params para fazer filtros e mudar a página

`GET /api/produtos/?nome=Compu`<br/>
<span>Mostra todos os produtos que contém "compu" no nome</span>

`GET /api/produtos/?categoria=Brinquedos`<br/>
<span>Mostra todos os produtos da categoria "Brinquedos"</span>

`GET /api/produtos/?page=4`<br/>
<span>Mostra todos os produtos da página 4</span>

`GET /api/produtos/:id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 4,
  "nome": "Computador",
  "descricao": "Um computador super potente!",
  "img": "https://m.media-amazon.com/images/I/41tQcIInuAL._AC_.jpg",
  "valor": "999.96",
  "quantidade_estoque": 100,
  "vendidos": 0,
  "user": "Julia0FSDH",
  "categorias": [
    {
      "id": 3,
      "nome": "Informática"
    }
  ]
}
```

<h3> Alteração de produtos </h3><br/>

`PATCH /api/produtos/:id - FORMATO DA REQUISIÇÃO`<br/>

```json
{
  "quantidade_estoque": 150
}
```

Somente vendedores tem acesso a essa rota.<br/>
Campos que podem ser atualizados:<br/>

<ul>
	<li>nome,</li>
	<li>descricao,</li>
	<li>img,</li>
	<li>valor,</li>
	<li>quantidade_estoque,</li>
  <li>categorias:[ <ul>
		<li>{
			"nome"
		}</li></ul>
	]</li>
</ul>

`PATCH /api/produtos/:id - FORMATO DA RESPOSTA - STATUS 200`<br/>

```json
{
  "id": 3,
  "nome": "Geladeira Brastemp French",
  "descricao": "O Refrigerador Brastemp Frost Free French Door 554 Litros Inox BRO85AK – 127 Volts, traz mais tecnologia e sofisticação para a sua cozinha. Tecnologia Inverter A+++: Com a tecnologia inverter A+++, o refrigerador Brastemp economiza até 30% de energia e mantém a temperatura estável, ajudando na preservação dos alimentos.",
  "img": "https://m.media-amazon.com/images/I/41lgp8caWoL._AC_SX425_.jpg",
  "valor": "6399.00",
  "vendidos": 10,
  "quantidade_estoque": 150,
  "disponibilidade": true,
  "user": "userSeller21FSDH",
  "categorias": [
    {
      "id": 3,
      "nome": "Eletrodomésticos"
    }
  ]
}
```

<h3> Exclusão de produtos </h3><br/>

`DELETE /api/produtos/id`<br/>
Somente o dono do produto poderá excluí-lo.<br/>
Não é necessário um corpo da requisição.

`DELETE /api/produtos/id - SEM RETORNO - STATUS 204`<br/>

<h3>POSSÍVEIS ERROS</h3>

Caso o produto procurado não exista:<br />
`FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "detail": "Not found."
}
```

<hr />

<h2 align="center">Carrinho</h2>

<h3> Busca o carrinho </h3><br/>

`GET /api/users/carrinho/`
Retorna o carrinho do usuário autenticado.<br/>
Não é necessário corpo de requisição.<br/>

`FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 15,
      "carrinho_id": 7,
      "quantidade": 1,
      "produto": {
        "id": 4,
        "nome": "LEGO® Classic Blocos",
        "descricao": "LEGO® Classic Blocos Transparentes Criativos; Kit de Construção para Crianças (500 peças)",
        "img": "https://m.media-amazon.com/images/I/81+xlh0eUIL._AC_SX425_.jpg",
        "valor": "204.15",
        "vendidos": 22,
        "quantidade_estoque": 78,
        "disponibilidade": true,
        "user": "userSeller21FSDH",
        "categorias": [
          {
            "id": 4,
            "nome": "Brinquedos"
          }
        ]
      },
      "carrinho": {
        "id": 7,
        "qtd_total": 2,
        "preco_total": 748
      }
    }
  ]
}
```

<h3> Adicona produto ao carrinho </h3><br/>

`POST /api/users/carrinho/produto_id/`
Adiciona o produto no carrinho do usuário autenticado.

`FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 16,
  "carrinho_id": 7,
  "quantidade": 1,
  "produto": {
    "id": 2,
    "nome": "Teclado Mecânico Gamer",
    "descricao": "Teclado Mecânico Gamer HyperX Alloy Origins Core, RGB - HX-KB7RDX-BR",
    "img": "https://m.media-amazon.com/images/I/51fJITLrBrS.__AC_SX300_SY300_QL70_ML2_.jpg",
    "valor": "544.58",
    "vendidos": 19,
    "quantidade_estoque": 31,
    "disponibilidade": true,
    "user": "userSeller10FSDH",
    "categorias": [
      {
        "id": 2,
        "nome": "Informática"
      }
    ]
  },
  "carrinho": {
    "id": 7,
    "qtd_total": 2,
    "preco_total": 748
  }
}
```

<h3> Altera a quandidade de produto no carrinho </h3><br/>

`PATCH /api/users/carrinho/1/qtd/`
`FORMATO DA RESPOSTA - STATUS 200`

Adiciona ou remove um item do carrinho pelo query_params:<br/>
add -> para adicionar | `PATCH /api/users/carrinho/1/qtd/?add`<br/>
remove -> para remover| `PATCH /api/users/carrinho/1/qtd/?remove`<br/>

```json
{
  "id": 15,
  "carrinho_id": 7,
  "quantidade": 2,
  "produto": {
    "id": 4,
    "nome": "LEGO® Classic Blocos",
    "descricao": "LEGO® Classic Blocos Transparentes Criativos; Kit de Construção para Crianças (500 peças)",
    "img": "https://m.media-amazon.com/images/I/81+xlh0eUIL._AC_SX425_.jpg",
    "valor": "204.15",
    "vendidos": 22,
    "quantidade_estoque": 78,
    "disponibilidade": true,
    "user": "userSeller21FSDH",
    "categorias": [
      {
        "id": 4,
        "nome": "Brinquedos"
      }
    ]
  },
  "carrinho": {
    "id": 7,
    "qtd_total": 3,
    "preco_total": 952
  }
}
```

<hr />

<h2 align="center">Pedido</h2>

<h3> Busca todos os pedidos </h3><br/>

`GET /api/pedidos/`<br/>
Somente vendedor pode acessar essa rota.<br/>
Retorna pedidos do vendedor autenticado.<br/>
`FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 40,
      "status": "PEDIDO REALIZADO",
      "created_at": "2023-05-10T00:01:41.303065Z",
      "updated_at": "2023-05-10T00:01:41.303065Z",
      "produtos": [
        {
          "id": 2,
          "nome": "Teclado Mecânico Gamer",
          "descricao": "Teclado Mecânico Gamer HyperX Alloy Origins Core, RGB - HX-KB7RDX-BR",
          "img": "https://m.media-amazon.com/images/I/51fJITLrBrS.__AC_SX300_SY300_QL70_ML2_.jpg",
          "valor": "544.58",
          "valor_total": 544.58,
          "quantidade": 1
        }
      ],
      "user_id": 7
    }
  ]
}
```

`GET /api/pedidos/info/`<br/>
O usuário comum ou o vendedor pelo pedido podem acessar essa rota.<br/>
Retorna um lista de pedidos.<br/>

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "status": "EM ANDAMENTO",
      "created_at": "2023-05-10T00:01:41.303065Z",
      "updated_at": "2023-05-10T00:01:41.303065Z",
      "produtos": [
        {
          "id": 2,
          "nome": "Teclado Mecânico Gamer",
          "descricao": "Teclado Mecânico Gamer HyperX Alloy Origins Core, RGB - HX-KB7RDX-BR",
          "img": "https://m.media-amazon.com/images/I/51fJITLrBrS.__AC_SX300_SY300_QL70_ML2_.jpg",
          "valor": "544.58",
          "valor_total": 544.58,
          "quantidade": 1
        }
      ],
      "user_id": 7
    }
  ]
}
```

`GET /api/pedidos/info/seller`<br/>
Somente o vendedor pode acessar essa rota.<br/>
Retorna um lista de pedidos.<br/>

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "status": "EM ANDAMENTO",
      "created_at": "2023-05-10T00:01:41.303065Z",
      "updated_at": "2023-05-10T00:01:41.303065Z",
      "produtos": [
        {
          "id": 2,
          "nome": "Teclado Mecânico Gamer",
          "descricao": "Teclado Mecânico Gamer HyperX Alloy Origins Core, RGB - HX-KB7RDX-BR",
          "img": "https://m.media-amazon.com/images/I/51fJITLrBrS.__AC_SX300_SY300_QL70_ML2_.jpg",
          "valor": "544.58",
          "valor_total": 544.58,
          "quantidade": 1
        }
      ],
      "user_id": 7
    }
  ]
}
```

<h3> Cria pedidos </h3><br/>

`POST /api/pedidos/`<br/>
Cria pedido para o usuário autenticado, pode ser comum ou vendedor.<br/>
Não é necessário corpo na requisição.<br/>

`FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "status": "PEDIDO REALIZADO",
  "created_at": "2023-05-10T00:01:41.303065Z",
  "updated_at": "2023-05-10T00:01:41.303065Z",
  "produtos": [
    {
      "id": 2,
      "nome": "Teclado Mecânico Gamer",
      "descricao": "Teclado Mecânico Gamer HyperX Alloy Origins Core, RGB - HX-KB7RDX-BR",
      "img": "https://m.media-amazon.com/images/I/51fJITLrBrS.__AC_SX300_SY300_QL70_ML2_.jpg",
      "valor": "544.58",
      "valor_total": 544.58,
      "quantidade": 1
    }
  ],
  "user_id": 7,
  "valor_total_pedido": 544.58
}
```

<h3> Altera status do pedido </h3><br/>

`PATCH /api/pedidos/pedido_id/`<br/>
Somente o vendedor responsável pelo pedido pode acessar essa rota.<br/>
Retorna o pedido com o status alterado.<br/>

`FORMATO DA REQUISIÇÃO`<br/>

```json
{
  "status": "EM ANDAMENTO"
}
```

`FORMATO DA RESPOSTA`<br/>

```json
{
  "id": 1,
  "status": "EM ANDAMENTO",
  "created_at": "2023-05-10T00:01:41.303065Z",
  "updated_at": "2023-05-10T00:01:41.303065Z",
  "produtos": [
    {
      "id": 2,
      "nome": "Teclado Mecânico Gamer",
      "descricao": "Teclado Mecânico Gamer HyperX Alloy Origins Core, RGB - HX-KB7RDX-BR",
      "img": "https://m.media-amazon.com/images/I/51fJITLrBrS.__AC_SX300_SY300_QL70_ML2_.jpg",
      "valor": "544.58",
      "valor_total": 544.58,
      "quantidade": 1
    }
  ],
  "user_id": 7
}
```

<hr />

<p>Feito com carinho ♥ por Julia</p>
