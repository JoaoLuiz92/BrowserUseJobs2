﻿# Automação de Busca de Vagas com IA e Preenchimento de Documentos

Este projeto utiliza IA para automatizar a busca por vagas de emprego compatíveis com o currículo de um usuário e preenche um documento (Word ou PDF) com os detalhes dessas vagas. A busca é feita a partir das habilidades e experiências listadas no currículo, filtrando vagas publicadas nos últimos 7 dias e com modelos de trabalho remoto ou híbrido. O projeto visa facilitar a pesquisa de vagas, gerando documentos com as informações relevantes de forma automatizada.

## Funcionalidades

- **Extração de texto do currículo em formato PDF**: O currículo do candidato é lido e suas informações são extraídas.
- **Busca de vagas compatíveis**: A IA busca vagas de emprego compatíveis com o perfil do candidato, baseadas nas habilidades e experiência listadas no currículo.
- **Filtragem de vagas recentes**: Apenas vagas publicadas nos últimos 7 dias são consideradas.
- **Geração automática de documento**: As vagas encontradas são inseridas em um documento Word ou PDF, pronto para ser enviado ao candidato ou utilizado em outras aplicações.

## Como funciona?

1. **Extração do currículo**: O currículo em formato PDF é lido e convertido para texto.
2. **Busca de vagas**: A IA utiliza o texto extraído do currículo para buscar vagas compatíveis no Google.
3. **Filtragem de vagas**: As vagas são filtradas para incluir apenas as publicadas nos últimos 7 dias.
4. **Preenchimento de documento**: Um documento Word ou PDF é automaticamente preenchido com as informações das vagas encontradas.

## Tecnologias Utilizadas

- **Python**: A principal linguagem de programação utilizada no projeto.
- **OpenAI GPT-4**: Utilizado para buscar vagas de emprego com base no currículo.
- **pdfminer.six**: Para extrair texto de arquivos PDF.
- **python-docx**: Para criar e preencher documentos Word.
- **reportlab**: Para gerar arquivos PDF.
- **dotenv**: Para carregar variáveis de ambiente de forma segura.

## Como Rodar o Projeto

### Pré-requisitos

Crie um ambiente virtual (opcional, mas recomendado) e instale as dependências necessárias com o pip:
```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```
## Passos

###

### Clone este repositório : 
 ```
git clone https://github.com/seu-usuario/automacao-busca-vagas.git
cd automacao-busca-vagas

 ``` 

### Coloque o currículo em formato PDF:
    - No diretório raiz do projeto e nomeie o arquivo como SeuCV.pdf (ou altere o nome no código conforme necessário).

### Configurar variáveis de ambiente:
Crie um arquivo .env na raiz do projeto e adicione sua chave da API OpenAI.
```
OPENAI_API_KEY=your_openai_api_key

```


## Execute o script :
```
python auto_apply.py

```
# Estrutura do Projeto
```
├── .env               # Arquivo de configuração de variáveis de ambiente
├── auto_apply.py            # Script principal para buscar vagas e preencher documentos
├── requirements.txt   # Dependências do projeto
├── README.md          # Este arquivo
└── CvJoao.pdf         # Exemplo de currículo em PDF (substitua com o seu próprio)
```

# Contribuindo
Se você quiser contribuir com este projeto, sinta-se à vontade para abrir issues ou enviar pull requests. Ficarei feliz em revisar e melhorar o código!

# Licença
Este projeto está licenciado sob a MIT License.

# Contato

João Luiz Da Rosa Junior - LinkedIn
Email: jluizdarosajr@gmail.com
