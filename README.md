# Atividades - PDF Reader

Este repositório contém um script Python para ler e extrair texto de arquivos PDF.

## Arquivo Alvo

- `1644843613529.pdf` - Roteiro de Aula Prática sobre Projeto de Software

## Como Usar

### Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

### Instalação

1. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### Execução

Para ler o arquivo PDF `1644843613529.pdf`:

```bash
python3 read_pdf.py
```

O script irá:
- Abrir o arquivo PDF
- Extrair o texto de todas as páginas
- Exibir o conteúdo no console

## Conteúdo do PDF

O PDF contém um roteiro de aula prática sobre **Projeto de Software**, focando em:
- Desenvolvimento de práticas de projeto conforme princípios da metodologia ágil Scrum
- Uso de ferramentas como IceScrum, Trello e Asana
- Atividades práticas de desenvolvimento de aplicativos usando metodologia ágil

## Estrutura do Repositório

```
.
├── 1644843613529.pdf       # Arquivo PDF a ser lido
├── 1709317510599.pdf       # Outro arquivo PDF
├── 1709834488001.pdf       # Outro arquivo PDF
├── read_pdf.py             # Script Python para ler PDFs
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

## Dependências

- PyPDF2 >= 3.0.0 - Biblioteca para manipulação de arquivos PDF
