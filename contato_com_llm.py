from openai import OpenAI

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {"role":"system", 
            "content":"""Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marktplace online.
            Eu quero que você analise essa renha, e me retorne um JSON com as seguintes chaves:
            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha original, sem tradução
            - 'resenha_pt': a resenha traduzida para o português, deve estar sempre na língua portuguesa
            - 'avaliacao': uma avaliacao se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra'(apenas uma dessas opções)
            
            Exemplo de entrada:
            '878484654354$Pedro Silva#this is a positive review for the app'
            Exemplo de saída:
            {
                "usuario": "Pedro Silva",
                "resenha_original": "this is a positive review for the app",
                "resenha_pt": "esta é uma resenha positiva para o aplicativo",
                "avaliacao": "Positiva"
            }

             Exemplo de entrada:
            '31251325512$John Myers#Je n'aime pas cette application'
            Exemplo de saída:
            {
                "usuario": "John Myers",
                "resenha_original": "Je n'aime pas cette application",
                "resenha_pt": "não gosto desta aplicação",
                "avaliacao": "Negativa"
            }

            Regra importante: APENAS RETORNE O JSON, SEM NENHUM TEXTO ADICIONAL. NEM MESMO EXPLICAÇÕES. APENAS O JSON PURO."""
            },
            
            {"role":"user", "content": f"Resenha: {linha}"}
        ],
        temperature=0.0,
    )

    resposta = resposta_do_llm.choices[0].message.content.replace("```json", "").replace("```", "")
    print(resposta)
    return resposta