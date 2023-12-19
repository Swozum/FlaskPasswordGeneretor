# Gerador de Senhas - Flask App

Este é um aplicativo Flask simples para gerar senhas com base nas preferências do usuário.

## Pré-requisitos

- Python 3 instalado (recomendado: Python 3.6 ou superior)
- Gerenciador de pacotes pip

## Instalação

1. Clone o repositório ou baixe o código-fonte do aplicativo.

2. Vá para o diretório do projeto.

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Windows:

    ```bash
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```bash
    source venv/bin/activate
    ```

5. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Executando o aplicativo

1. No terminal, dentro do diretório do projeto e com o ambiente virtual ativado, execute:

    ```bash
    python app.py
    ```

2. O aplicativo Flask será executado localmente em `http://127.0.0.1:5000/`.

## Uso

- Acesse `http://127.0.0.1:5000/` em seu navegador.
- Preencha o formulário com suas preferências para gerar senhas.
- Clique no botão "Gerar Senhas" para obter senhas com base nas configurações fornecidas.

## Nota

Certifique-se de desativar o ambiente virtual após a utilização do aplicativo:

```bash
deactivate
