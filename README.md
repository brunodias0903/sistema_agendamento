# 🧪 Atividade Complementar — Testes e Qualidade de Software

Este repositório foi criado para enviar os arquivos referentes à atividade complementar da disciplina **Testes e Qualidade de Software**.

---

## 🔗 Link da Atividade

📎 [Acesse pelo Google Classroom](https://classroom.google.com/c/Nzk5NDg5ODQxNTAw/a/ODE2MDk0NjgyODgx/details)

---

## 👥 Integrantes do Grupo

- **Bruno Dias de Vasconcelos**
- **Carlos Gabriel Raposo Melo**
- **Gabriel Henrique da Silva Leitão**
- **Kevin Henrique Maia Bastos**
- **Victorya Cohen Freitas Stone**

---

## 💾 Descrição

O projeto consiste no desenvolvimento e teste de um **Sistema de Agendamento de Consultas Médicas**, com foco na aplicação de conceitos de **Testes Unitários** utilizando `pytest`, `pytest-cov` e geração de relatórios de cobertura.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Pytest
- Pytest-cov

---

## ▶️ Como Executar os Testes

```bash
# Criação do ambiente virtual
python -m venv env

# Ativar o ambiente
# Windows:
env\Scripts\activate
# Linux/Mac:
source env/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar os testes
pytest

# Ver cobertura no terminal
pytest --cov=src --cov-report=term-missing

# Gerar relatório HTML
pytest --cov=src --cov-report=html
```
