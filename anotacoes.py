"""
Flask:
- Framework construído para Python para desenvolvimento de aplicações web.
- É um *microframework*: vem enxuto e permite liberdade para escolher bibliotecas adicionais.

Framework:
- Conjunto de ferramentas, bibliotecas e convenções que fornecem uma estrutura para desenvolver aplicações.

Vantagens do Flask:
- Simplicidade
- Escalabilidade
- Flexibilidade

API:
- Application Programming Interface.
- Conjunto de regras, protocolos e ferramentas que permitem que diferentes softwares se comuniquem.
- Funciona como uma "ponte" ou "porta" para comunicação entre cliente e servidor.

Fluxo de comunicação:
CLIENTE → (request) → API → Servidor
CLIENTE ← (response) ← API ← Servidor

API REST:
- REST = *Representational State Transfer*.
- Estilo de arquitetura para desenvolvimento de APIs usando princípios do protocolo HTTP.
- Principais métodos HTTP: GET, POST, PUT, PATCH, DELETE.

API RESTful:
- API que segue fielmente todos os princípios e restrições do REST, como:
  - Interface uniforme
  - Stateless
  - Cacheable
  - Separação cliente-servidor
  - Camadas
  - (Opcional) Código sob demanda

Métodos HTTP:
- GET: retorna dados.
- POST: insere dados.
- PUT: substitui todo o recurso.
- PATCH: atualiza parcialmente o recurso.
- DELETE: remove recurso específico.

| Característica          | **REST**                                                      | **RESTful**                                                    | **Não REST**                                             |
| ----------------------- | ------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------- |
| **Base**                | Usa conceitos do REST, mas pode não seguir tudo               | Segue fielmente todas as restrições do REST                    | Não segue o padrão REST                                  |
| **Métodos HTTP**        | Pode usar GET, POST, PUT, DELETE, PATCH                       | Usa métodos HTTP de forma correta e sem desvio                 | Pode usar HTTP de forma não padrão (ex: tudo com POST)   |
| **URLs**                | Pode usar padrões parecidos                                   | URLs bem definidas e orientadas a recursos (ex: `/usuarios/1`) | URLs confusas ou sem padrão (ex: `/getUsuario.php?id=1`) |
| **Stateless**           | Pode não ser totalmente stateless                             | Sempre stateless (cada requisição é independente)              | Pode depender de sessão armazenada no servidor           |
| **Cache**               | Pode não implementar cache                                    | Implementa cache quando possível                               | Normalmente não implementa cache                         |
| **Formato de dados**    | Pode variar (JSON, XML, etc.)                                 | Usa formatos bem definidos (geralmente JSON)                   | Sem padrão fixo                                          |
| **Exemplo de endpoint** | `POST /usuarios/listar` (usa POST para buscar, não é o ideal) | `GET /usuarios` (padrão correto para buscar)                   | `/listarUsuarios.php`                                    |

1. Cache
O que é:
Uma forma de guardar temporariamente dados para que, quando precisarmos deles de novo, não seja necessário 
buscar tudo do zero.

No contexto de APIs:
Quando você faz uma requisição para a API e recebe uma resposta, essa resposta pode ser armazenada 
(em cache) para que, se pedir a mesma coisa de novo, a resposta seja devolvida muito mais rápido e com 
menos consumo do servidor.

Exemplo:
Você abre a página de um produto em um site. Se o preço não muda com frequência, ele pode estar em cache
 no seu navegador ou num servidor intermediário. Assim, não precisa consultar o banco de dados toda vez.

📌 Analogia: É como guardar um número de telefone na agenda do celular para não ter que perguntar de novo.

2. Stateless
O que é:
Significa que o servidor não guarda o “estado” da sua sessão entre uma requisição e outra.

No contexto de APIs REST/RESTful:
Cada requisição que você envia precisa conter todas as informações necessárias para ser processada,
 sem depender de informações salvas do seu último acesso.

Exemplo:
Quando você faz login em um site que segue o padrão stateless, o servidor não lembra que você 
“já está logado” automaticamente — ele confia em um token ou credencial enviado em toda requisição para
 saber quem você é.

📌 Analogia: É como falar com um atendente que não te reconhece de uma ligação para outra — você precisa
 repetir todas as informações sempre.

3. Endpoint
O que é:
É um endereço (URL) específico onde um recurso ou funcionalidade da API está disponível para acesso.

No contexto de APIs:
Cada endpoint representa um ponto de comunicação onde o cliente pode fazer requisições.

Exemplo:

GET /usuarios → pega todos os usuários

GET /usuarios/5 → pega o usuário com ID 5

POST /usuarios → cria um novo usuário

📌 Analogia: Pense na API como um prédio e cada endpoint é uma porta com um número diferente — cada
 uma dá acesso a um “cômodo” com dados ou funcionalidades diferentes.

CLIENTE (Navegador / App)
      |
      | 1️⃣ Requisição para um ENDPOINT específico
      |    (ex: GET /produtos/10)
      v
API SERVER --------------------+
      |                        |
      | 2️⃣ Verifica se a resposta já está no CACHE
      |    (se sim, devolve direto — mais rápido)
      |                        |
      | 3️⃣ Se não estiver no cache, busca no banco de dados
      |    e retorna o resultado
      |                        |
      | 4️⃣ Como é STATELESS, cada requisição
      |    precisa conter todas as infos necessárias
      |    (ex: token de autenticação)
      v
CLIENTE recebe a RESPOSTA
 
Códigos de resposta HTTP:
Quando nós temos a comunicação entre dois sistemas através de uma API, nós temos a requisição e nós temos
 a resposta, que é muitas vezes chamada de responsa. Essa responsa vem acompanhada com um código de 
 resposta e esse código basicamente informa o que aconteceu aqui na sua requisição e nós temos uma 
 classificação:

100 e 199 - está destinada às respostas informativas, não dizem se deu certo ou se não deu
200 e 299 - As bem-sucedidas (o código 200 quer dizer que a requisiçã que você tentou fazer deu certo)
300 e 399 - são para redirecionamento, geralmente ela acontece quando alguém tenta acessar um recurso que mudou
de lugar
400 e 499 - erro do cliente, exemplo quando o cliente envia uma inserção de um novo registro no meu banco de
dados, mas ele errou o formato que tem que estar o CEP, nesse caso a gente vai utilizar o 400,
404 - nao encontrado
500 a 599 - erro dentro do servidor, exemplo cliente fez tudo certo mas quando vai enviar teve um erro
no banco de dados, nesse caso retorna 500 que significa internal server erro 

1xx → Informações

2xx → Sucesso

3xx → Redirecionamento

4xx → Erro do cliente

5xx → Erro do servidor
"""