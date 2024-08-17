# My-mangas 🥭

Este é o projeto de front-end com python que obtém e exibe mangás em uma interface simples e sem anúncios, utilizando as linguagens **TypeScript** e **Python**.

## 📂 Estrutura do Projeto

Este repositório contém o código-fonte da automação/web-scraper da aplicação. Para visualizar o projeto completo, incluindo front-end e API, veja as outras partes do sistema:

- [**Front-end**](https://github.com/GustavoSilverio/my-mangas-front): Uma aplicação com uma interface simples que mostra o catálogo de mangás disponiveis na plataforma.
- [**API**](https://github.com/GustavoSilverio/my-mangas-api): Uma API que serve os dados coletados pela automação/web-scraper. Os dados são armazenados em um banco de dados MongoDB e servidos ao front-end.

## ⚖️ Aviso Legal

Este projeto é apenas um exemplo técnico e **não deve ser usado para distribuir conteúdo protegido por direitos autorais** sem a devida autorização dos proprietários dos direitos. Nenhum conteúdo de mangás é incluído neste repositório.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para utilizar o código como base para seus próprios projetos, respeitando os termos da licença.

## 🛠️ Como Rodar o Projeto (Obrigatório python instalado na maquina)

1. Clone o repositório:
   ```bash
   git clone https://github.com/GustavoSilverio/manga-scraper.git
    ```
2. Crie um ambiente virtual:
    ```bash
    python -m venv .venv
    ```
3. Ative o ambiente virtual
    ```bash
    .venv\scripts\activate
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Rode o projeto:
    ```bash
    python main.py
    ```
5. É necessário criar um cluster (banco) no mongodb para poder armazenar os mangás, após isso crie um arquivo .env na raiz do projeto e adicione a seguinte env var:
    ```env
    MONGO_BASE_URL='mongodb+srv://USER:SENHA@********.mongodb.net/'
    ```