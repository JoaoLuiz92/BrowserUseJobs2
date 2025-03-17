import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_openai import ChatOpenAI
from pdfminer.high_level import extract_text
import csv
from datetime import datetime, timedelta


load_dotenv()


def extract_resume_text(pdf_path):
    return extract_text(pdf_path)


def filter_recent_jobs(jobs):
    today = datetime.today()
    seven_days_ago = today - timedelta(days=7)
    
    filtered_jobs = [job for job in jobs if datetime.strptime(job['data_publicacao'], "%Y-%m-%d") >= seven_days_ago]
    return filtered_jobs


def save_jobs_to_csv(jobs, file_name="vagas_encontradas.csv"):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Título', 'Cidade', 'Modelo de Trabalho', 'Link', 'Data de Publicação']) 
        for job in jobs:
            writer.writerow([job['titulo'], job['cidade'], job['modelo_trabalho'], job['link'], job['data_publicacao']])


resume_text = extract_resume_text("CvJoao.pdf")


job_search_prompt = f"""
Com base no seguinte currículo:

{resume_text}

Encontre vagas de emprego compatíveis para este candidato no Google.
Vagas buscadas devem ser baseadas nas habilidades técnicas e experiência listadas no currículo. 
Por favor, forneça o título do cargo, a cidade, o modelo de trabalho (remoto, híbrido ou presencial), a data de publicação e o link da vaga.
Apenas inclua vagas publicadas nos últimos 7 dias.
"""


async def main():

    agent = Agent(
        task=job_search_prompt,
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )


    job_results = await agent.run()


    recent_jobs = filter_recent_jobs(job_results)


    save_jobs_to_csv(recent_jobs)
    print(f"Arquivo 'vagas_encontradas.csv' gerado com {len(recent_jobs)} vagas.")


if __name__ == "__main__":
    asyncio.run(main())
