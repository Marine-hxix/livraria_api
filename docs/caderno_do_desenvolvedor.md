## Capítulo 2 — Seção 2.1
O que é uma rota em uma API?
    Quando uma funcao e criada e dita como rota, e a sua URL.

Qual é a função do decorador @app.get()?
    O intepretador Python procura essa funcao no codigo para evocar a api.

Por que uma aplicação possui várias rotas em vez de uma única?
    A medida que a aplicacao cresce se faz necessario a criacao de outras rotas, o codigo fica muito mais facil de ser lido e dada a sua manutencao posterior, sem deixar de mencionar que nao e uma boa pratica deixar tudo na mesma rota. O cliente podera ficar perdido ao longo da visualizacao.

### Minha explicação
Se você precisasse criar uma API para uma locadora de filmes, quais endpoints criaria primeiro?
1 - Tela de login.
2 - Cadastro de clientes.
2.1 - Consulta.
2.2 - Edicao.
2.3 - Delete.
3 - Cadastro de filmes.
3.1 - Consulta.
3.2 - Edicao.
3.3 - Delete.

## Capítulo 2 — Seção 2.2

### Reflexão

1. Qual é a função de um método HTTP?
    E mostrar uma funcao executada pelo cliente atraves de uma rota especifica.

2. Qual é a diferença entre GET e POST?
    Get faz a consulta.
    Post faz uma adicao.

3. Em que situação utilizaria PUT?
    Quando quer modificar ou alterar todos os campos.

4. Em que situação utilizaria PATCH?
    Usa- se para uma modificacao parcial.

5. Qual é a finalidade do DELETE?
    Ele apaga o campo ou o item desejado.

6. Por que não precisamos criar uma URL diferente para cada operação de um recurso?
    Acredito que o codigo ficaria confuso e de dificil manutencao, talves, tambem, haja um excesso de informacao para a api, no sentido de que possa ter um crash ou lentidao no Uvicorn.

### Minha explicação

Explique, com suas próprias palavras, o seguinte:

GET /livros - Faca uma consulta em "livros".
POST /livros - Crie um novo "livro".
GET /livros/1 - Faca uma consulta em "livro, cuja id e 1".
PUT /livros/1 - Crie um novo "livro, cuja id e 1".
PATCH /livros/1 - Altere o respectivo campo em "livro, cuja id e 1".
DELETE /livros/1 - Exclusao do "livro, cuja id e 1".

Determine qual combinação de método + rota você utilizaria para cada situação:
| Situação                           | Método | Rota |
| ---------------------------------- | ------ | ---- |
| Listar todos os livros             |  Get   |@app.get|
| Cadastrar um novo livro            |Post    |@app.post|
| Consultar o livro 5          |Get/livro/id5 |@app.get("/livro/5")|
| Substituir o livro 5          |Put/livro/id5|@app.put("/livro/5")|
| Alterar apenas o título do livro 5 |patch/livro/id5|@app.patch("/livro/5","/titulo")|
| Excluir o livro 5          |delete/livro/id5|@app.delete("/livro/5")|

## Capítulo 2 — Seção 2.3

### Reflexão

1. O que acontece quando uma requisição chega a uma rota FastAPI?
    O interpretador Python verifica no codido qual e a funcao responsavel pela requisicao e faz o enderecamento. A funcao e executada e a resposta e retornada ao cliente.

2. Qual é a diferença entre:
   GET /livros - faz a consulta de todo acervo da biblioteca.
   e
   GET /livros/1? - faz a consulta apenas do volume requisitado.

3. O que representa o trecho {livro_id}?
    E um paramento usado na URL para a identificao de uma recurso de acordo com a sua requisicao.

4. Por que estamos utilizando uma lista em memória neste momento?
O nosso objetivo nesse exato momento e aprender a utilizacao e comportamento basicos do FastAPI para fins didaticos e testes locais, por enquanto nao se faz necessaria a criacao de um banco de dados para a importacao e ou armazenamento de dados.

5. Qual problema encontraremos quando a aplicação precisar armazenar dados permanentemente?
    Estamos usados ficticios onde e armazenada na memoria. Ainda nao houve uma estruturacao do banco de dados para a implementacao.

### Faça uma previsão

Até agora ainda não utilizamos um banco de dados. O que você acredita que precisaremos mudar quando os livros precisarem continuar existindo mesmo depois que o servidor for reiniciado?
    Apos a inclusao com o banco de dados onde nossas informacoes serao armazendas nele, teremos uma necessidade maior da modelagem dos dados. Criamos rotas especificas para cada campo, mas a enseriamos em campos ditadas pelo programador; os proximos passos seriam a captacao dos dados enviadas pelo cliente e armazenadas pelo banco de dados. Um pouco mais adiantes faremos com que todas as nossas requisicoes seja enviada pelo cliente, como edicao, deletar e novo.

### Minha explicação

Explique, com suas próprias palavras, o caminho percorrido por esta requisição:
GET /livros/1
    Funcao Python -> Roteamento -> Enderecamento(get/livros/id)-> HTTP Status-> Cliente

## Capítulo 2 — Seção 2.4

### Reflexão

1. O que é o corpo de uma requisição HTTP?
    Definiria como o campo a ser preenchido pelo cliente de acordo com as regras estabelecidas pelo desenvolvedor.

2. Por que precisamos validar os dados enviados pelo cliente?
    Devemos desenvolver as aplicacoes baseadas em regras do plano de negocios. Apos recebermos os dados do cliente, estes deveram ser tratados e validados. O nosso banco de dados esta sendo guardado em memoria temporaria, futuramente esses dados serao alocados em um banco, onde la havera campos correspondentes as informacoes recebidas.

3. Qual é a função de um modelo Pydantic?

4. O que significa:   
   titulo: str
    Significa que o objeto criado a partir de uma determinada classe recebeu um metodo (titulo) e como tipo de dado um valor (str). 

5. O que acontece quando um campo obrigatório não é enviado?
    Ainda nao ha no codigo uma funcao que trata a informacao enviada, (valida ou invalida). Mas ja no Jason e possivel visualizar a mensagem: Validation Error.

### Pense como desenvolvedor

Imagine que você esteja desenvolvendo uma API para cadastro de usuários. Quais campos você considera obrigatórios? Quais tipos de dados cada campo deveria possuir?

    1 - Tela de login - str / int
    2 - Cadastro de clientes - str
    2.1 - Consulta - str / int
    2.2 - Edicao - str / int
    2.3 - Delete - click event
    3 - Cadastro de filmes - str / int
    3.1 - Consulta - str / int
    3.2 - Edicao - str / int
    3.3 - Delete - click event

### Minha explicação

Explique, com suas próprias palavras, o caminho percorrido por:

{
    "titulo": "FastAPI na Prática"
}

desde o momento em que o cliente envia o dado até ele chegar à função criar_livro().
    O cliente se depara com um campo a ser preenchido -> a informacao e recebida e validada pelo parametro -> 
    Resposta HTTP(ok) -> informacao armazeda na memoria temporaria -> Resposta ao cliente.

Por que você acha que validar os dados antes de executar a lógica da aplicação é importante?
    Acredito que os dados nao devam ser armazedados de qualquer forma, a tipagem correta garante a integridade e a visibilidade
    da informacao. E posteriormente com a idexacao ao banco de dados, onde se faz preciso estabelecer regras claras para a sua
    armazenagem.