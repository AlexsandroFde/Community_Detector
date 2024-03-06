# Detector de Comunidades em Rede Social

Este é um script em Python que detecta comunidades em uma rede social com base em seus padrões de conexão.

## Funcionalidades

- Carregar dados da rede social de um arquivo CSV.
- Detectar comunidades usando uma abordagem baseada em modularidade.
- Exibir as comunidades detectadas.

## Como Usar

1. **Instalação das Dependências:**
   Certifique-se de ter o Python instalado. Você pode instalar a biblioteca necessária usando o pip:
    ```bash
    pip install networkx
    ```

2. **Execução do Script:**
    Execute o script Python e siga as instruções para fornecer o nome do arquivo CSV que contém os dados da rede social:

3. **Formato do Arquivo CSV:**
    O arquivo CSV deve ter o seguinte formato:
    ```
    usuario1,usuario2,usuario3,...
    usuario2,usuario1,usuario4,...
    usuario3,usuario1,usuario5,...
    ...
    ```
    Cada linha representa um usuário e suas conexões. Os usuários e conexões são separados por vírgulas.

## Exemplo

Aqui está um exemplo de como o arquivo CSV deve ser estruturado:

    Alice,Bob,Charlie,David
    Bob,Alice,Charlie
    Charlie,Alice,Bob,David
    David,Alice,Charlie
    Emily,Frank,Grace
    Frank,Emily,Grace
    Grace,Emily,Frank

## Contribuição
Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.