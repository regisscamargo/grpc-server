## Sistema RPC (Remote Procedure Call)

Este projeto foi desenvolvido com fim acadêmico e contém um sistema de chamada de procedimento remoto (RPC) implementado em Python usando gRPC.

## Descrição

O RPC é um paradigma de comunicação entre processos que permite que um programa solicite um serviço de outro programa localizado em uma rede sem precisar entender os detalhes da rede. Este sistema utiliza o gRPC, um framework RPC de código aberto desenvolvido pelo Google.

## Funcionalidades

- **Usuário**: O sistema permite realizar operações CRUD (criar, ler, atualizar, excluir) em usuários.
- **Produto**: Além das operações CRUD de usuário, o sistema também oferece as mesmas operações para produtos.

## Pré-requisitos

- Python 3.x
- Instalação do gRPC

## Como usar

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter instalado o Python e o gRPC.
3. Execute o servidor gRPC usando o arquivo `app.py`.
4. Use os clientes fornecidos no diretório `clients/` para interagir com o servidor e realizar operações CRUD em usuários e produtos.

## Estrutura do Projeto

- **Protos**: Contém os arquivos de definição de serviço e mensagem protobuf.
- **Services**: Contém as implementações dos serviços gRPC para usuários e produtos.
- **Clients**: Contém exemplos de clientes para interagir com o servidor.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* se encontrar algum problema ou enviar uma solicitação de *pull request* com melhorias.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
