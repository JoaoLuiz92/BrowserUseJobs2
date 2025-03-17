import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_openai import ChatOpenAI
from pdfminer.high_level import extract_text
import csv
from datetime import datetime, timedelta

# Carregar variáveis de ambiente
load_dotenv()

LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Função para extrair texto do currículo em PDF
def extract_resume_text(pdf_path):
    return extract_text(pdf_path)

# Função para filtrar vagas dentro dos últimos 30 dias
def filter_recent_jobs(jobs):
    today = datetime.today()
    thirty_days_ago = today - timedelta(days=30)
    
    filtered_jobs = [job for job in jobs if datetime.strptime(job['data_publicacao'], "%Y-%m-%d") >= thirty_days_ago]
    return filtered_jobs

# Função para salvar vagas em um arquivo CSV
def save_jobs_to_csv(jobs, file_name="vagas_encontradas.csv"):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Título', 'Cidade', 'Modelo de Trabalho', 'Link', 'Data de Publicação']) 
        for job in jobs:
            writer.writerow([job['titulo'], job['cidade'], job['modelo_trabalho'], job['link'], job['data_publicacao']])

# Extrair texto do currículo
resume_text = extract_resume_text("CvJoao.pdf")

# Criando um prompt para buscar vagas baseadas no currículo
job_search_prompt = f"""
Com base no seguinte currículo:

{resume_text}

Encontre vagas de emprego compatíveis para este candidato no LinkedIn Jobs.
Filtre para posições remotas ou híbridas, se possível.
Por favor, forneça o título do cargo, a cidade, o modelo de trabalho (remoto, híbrido ou presencial), a data de publicação e o link da vaga.
Apenas inclua vagas publicadas nos últimos 30 dias.
"""

# Função para login no LinkedIn manualmente
async def login_to_linkedin(agent):
    print("🔄 Fazendo login no LinkedIn...")
    await agent.goto("https://www.linkedin.com/login")

    # Inserir email
    await agent.fill("input[name='session_key']", LINKEDIN_EMAIL)
    
    # Inserir senha
    await agent.fill("input[name='session_password']", LINKEDIN_PASSWORD)
    
    # Clicar no botão de login
    await agent.click("button[type='submit']")
    
    print("✅ Login realizado com sucesso!")

# Função assíncrona principal
async def main():
    # Criando o agente
    agent = Agent(
        task=job_search_prompt,
        llm=ChatOpenAI(model="gpt-4o-mini"),
        browser="chrome"  # Pode ser "firefox" dependendo do seu setup
    )

    # Verificar se as credenciais foram carregadas
    if not LINKEDIN_EMAIL or not LINKEDIN_PASSWORD:
        print("Erro: credenciais do LinkedIn não foram carregadas corretamente.")
        return

    print(f"Tentando login com o email: {LINKEDIN_EMAIL}")

    # Executando o login no LinkedIn manualmente
    await login_to_linkedin(agent)

    # Espera alguns segundos para garantir que a página carregue
    await asyncio.sleep(5)

    # Verifica se o login foi bem-sucedido
    current_url = await agent.get_current_url()
    if "feed" in current_url:
        print("Login bem-sucedido!")
    else:
        print("Falha no login. Verifique as credenciais ou se o LinkedIn exibiu CAPTCHA.")

    # Executar a busca de vagas
    job_results = await agent.run()

    # Verifica se os resultados são válidos
    if not isinstance(job_results, list):
        print("Erro ao obter os resultados da busca. O retorno não é uma lista válida.")
        return

    # Filtrar as vagas recentes
    recent_jobs = filter_recent_jobs(job_results)

    # Salvar em CSV
    save_jobs_to_csv(recent_jobs)
    print(f"Arquivo 'vagas_encontradas.csv' gerado com {len(recent_jobs)} vagas.")

# Rodando o script corretamente
if __name__ == "__main__":
    asyncio.run(main())