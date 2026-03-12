# LLM Review Analyzer

Projeto em Python que utiliza um **Large Language Model (LLM)** para analisar resenhas de aplicativos, traduzir automaticamente para português e classificar o sentimento da resenha.

O sistema processa comentários de usuários a partir de um arquivo de texto, envia cada linha para um modelo de linguagem e retorna os dados estruturados em **JSON**.

## Funcionalidades

* Leitura de resenhas a partir de arquivo `.txt`
* Tradução automática para português
* Classificação de sentimento:

  * Positiva
  * Negativa
  * Neutra
* Conversão das resenhas em **JSON estruturado**
* Contagem de avaliações positivas, negativas e neutras
* Consolidação das resenhas processadas

## Estrutura do Projeto

```
.
├── main.py
├── contato_com_llm.py
├── chat_gpt_comments.txt
└── README.md
```

* **main.py** → processamento das resenhas
* **contato_com_llm.py** → comunicação com o modelo LLM
* **chat_gpt_comments.txt** → arquivo contendo as resenhas de entrada

## Exemplo de Entrada

```
878484654354$Pedro Silva#this is a positive review for the app
31251325512$John Myers#Je n'aime pas cette application
```

## Exemplo de Saída

```json
{
  "usuario": "Pedro Silva",
  "resenha_original": "this is a positive review for the app",
  "resenha_pt": "esta é uma resenha positiva para o aplicativo",
  "avaliacao": "Positiva"
}
```

## Tecnologias Utilizadas

* Python
* LLM (Google Gemma)
* LM Studio
* API compatível com OpenAI

## Como Executar

1. Clone o repositório

```
git clone https://github.com/seu-usuario/llm-review-analyzer.git
```

2. Instale as dependências

```
pip install openai
```

3. Inicie o **LM Studio** e carregue o modelo:

```
google/gemma-3-1b
```

4. Execute o projeto

```
python main.py
```

## Objetivo do Projeto

Este projeto demonstra como utilizar **LLMs para processamento de linguagem natural (NLP)** em tarefas como:

* análise de sentimento
* tradução automática
* transformação de dados não estruturados em JSON

## Autor

Thiago Farias
