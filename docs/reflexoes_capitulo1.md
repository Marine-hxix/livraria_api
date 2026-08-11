Diario de um Desenvolvedor

CAPÍTULO 1 - Introdução ao FastAPI

30/07/26 – Missao 1:
O que você acredita que seja um framework?
E um programa que reune em seu ambiente varias ferramentas de desenvolvimento para a criacao de um software.

Por que não criar uma aplicação utilizando apenas Python puro?
Apesar do Python ser uma otima linguagem de programacao e possuir uma biblioteca robusta ainda se faz necessario a utilizacao de frameworks complementares e especificos. Esses frameworks foram desenvolvidos para suprir as necessidades ou potencializar as outras ferramentas, onde elas são integradas a linguagem de programacao.

O que você espera aprender com o FastAPI que poderá aplicar em outros projetos?
A minha expectativa com o termino da obra e aplicar de forma segura e confiante todo o aprendizado que obtive durante a leitura. O aprendizado adquirido faz parte de minha capacitacao para dar os primeiros passos como desenvolvedor junior, de forma independente, onde o livro possa servir como consulta posterior e não mais como um manual. Quero criar outros projetos que integrara junto ao meu portfolio e que me propicie confianca.

Faça Comigo:
O que mais chamou sua atenção nas características do FastAPI?
Para ser sincero, cai de paraquedas no FastAPI, eu estava procurado ferramentas de desenvolvedor para iniciar a minha jornada como programador. Acabei procurando no YouTube um curso que abordasse o meu problema e a premissa do curso era o uso de Python, FastAPI e outras ferramentas para a construcao do app. Entretanto, nas vagas de emprego que estava visualizando, muitas empresas pediam como requisito habilidade em FastAPI.

Qual benefício você acredita que fará mais diferença nos seus projetos?
O beneficio de aprender e maximizar o uso da ferramenta.

Existe alguma característica que você ainda não compreendeu completamente?
Ate a leitura do topico nao ficou nenhuma duvida, o material esta produzindo o seu efeito, que e o entendimento do manuseio da ferramenta.

O que mais chamou sua atenção na documentação?
Apos o meu primeiro contato com a visualizacao do documento, tive uma pequena visao do poder da ferramenta e sua vasta biblioteca, mas onde a construcao do codigo e sua funcionalidade se da em poucas linhas. Ainda conservo o receio que mesmo apos a leitura da obra, ter acesso a documentacao do framework ainda sim terei compreendido de forma abstrata o usso da ferramenta.

Alguma característica apresentada nesta seção apareceu na documentação?
Sim, algumas linhas de codigos, a didatica de apresentacao sao compactuadas com a documentacao.

O que você espera aprender ao longo do livro sobre esses recursos?
Mesmo apos a leitura da obra sera necessario uma nova visitacao ou novas visitacoes. Talvez alguns pontos do livro nao facam sentido com a primeira leitura ou releituras.


Desafio de Consolidação

Explique, com suas próprias palavras, o que significa main:app.
Main significa o nome do arquivo, acredito que nele contera as principais linhas de codigo.
App e o nome da funcao criada.
Ao executar o programa, o interpretador Python inicia o arquivo Main e ja dentro do arquivo procura a funcao App para que ele seja instanciado.

Qual é a função do parâmetro --reload?
O Reload faz com que durante a fase do desenvolvimento o servidor Uvicorn esteja sempre online. Qualquer alteracao feita no app, o Uvicorn ja o atualiza.

Por que utilizamos poetry run em vez de executar o Uvicorn diretamente?
O Poetry faz o gerenciamento do ambiente virtual, como o isolamento, criacao de dependencias.. ele nao e o servidor do aplicacao.

O que acontece quando você salva o arquivo main.py enquanto o servidor está em execução?
O Uvicorn faz a atualizacao automaticamente da alteracao, sem a necessidade de interferencia do desenvolvedor.

Se o navegador exibe {"message": "Olá, Mundo!"}, descreva o caminho percorrido por essa resposta desde a função Python até a tela.
Funcao Python -> Roteamento -> Resposta HTTP(jason)-> Cliente


Desafio de Consolidação

Qual é a finalidade da documentação de uma API?
O documento e criado para auxiliar o seu uso, entendimento e manutencao do codigo.

Quais endereços disponibilizam o Swagger UI e o ReDoc em nossa aplicação?
http://127.0.0.1:8000/docs e http://127.0.0.1:8000/redoc

O que acontece quando clicamos em Execute no Swagger UI?
Apos clicar em seu painel interativo execute ele mostra o caminho percorrido pela requisicao, o status do servidor e a mensagem para o cliente final.

Qual é a principal vantagem da documentação automática em relação à documentação escrita manualmente?
O desenvolvedor se concentra em escrever o codigo, enquanto o Swagger faz todo o trabalho duro de transcricao para o documento.

Por que a documentação do FastAPI permanece sincronizada com o código da aplicação?
Eu acredito que seja por conta do Uvicor, onde ele mantem o servidor sempre online.