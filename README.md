# Visualizador de Dados CSV com Streamlit

Este projeto é uma aplicação simples em Streamlit que permite aos usuários carregar arquivos CSV, visualizar os dados em formato de tabela e gerar gráficos de barras e linhas para análises rápidas.

## Funcionalidades

- **Upload de Arquivos CSV:** Carregue facilmente seus arquivos de dados no formato CSV.
- **Visualização de Dados:** Exiba o conteúdo do arquivo CSV carregado em uma tabela interativa.
- **Geração de Gráficos:** Crie gráficos de barras para `preco_unitario` e gráficos de linha para `custo` automaticamente.
- **Validação de Arquivo:** Garante que apenas arquivos CSV sejam processados, exibindo mensagens de erro claras para outros formatos.

## Como Usar

Siga os passos abaixo para configurar e rodar a aplicação localmente:

### Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Recomenda-se usar um ambiente virtual.

### Instalação

1.  **Clone o repositório** (se estiver no GitHub):

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd streamlit-analise-de-dados
    ```

2.  **Instale as dependências:**

    ```bash
    pip install pandas streamlit
    ```

### Execução

Para iniciar a aplicação Streamlit, execute o seguinte comando no terminal, estando no diretório raiz do projeto:

```bash
streamlit run main.py
```

Isso abrirá a aplicação no seu navegador padrão.

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

## Exemplo de Uso

1.  **Carregue seu arquivo CSV:** Na interface da aplicação, clique em "Carregue seu arquivo CSV" e selecione um arquivo no formato `.csv`.
2.  **Visualização dos Dados:** Após o upload, a tabela com os dados do seu arquivo será exibida.
3.  **Gerar Gráficos:** Clique no botão "Gerar tabelas e gráficos" para visualizar os gráficos de `preco_unitario` e `custo`.
4.  **Mensagens de Erro:** Se você tentar carregar um arquivo que não seja CSV, uma mensagem de erro será exibida. Se nenhum arquivo for carregado, uma instrução aparecerá para salvar sua planilha Excel como `.csv`.
