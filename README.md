# Consulta de Placa de Veículo com Flask + API InfoSimples

Este projeto é um microserviço construído em Python usando Flask que realiza consultas de placas de veículos na API da [InfoSimples](https://www.infosimples.com.br/). A aplicação retorna informações detalhadas do veículo, incluindo dados como marca, modelo, ano, Renavam e proprietário (dependendo do plano contratado).

---

## Tecnologias Utilizadas

- Python 3.11+
- Flask
- Requests
- API InfoSimples

---

##  Pré-requisitos

- Conta criada em [infosimples.com.br](https://www.infosimples.com.br/)
- Token de API válido
- Python instalado (recomenda-se usar virtualenv)
- Créditos ativos na InfoSimples (para consultas reais)

---

## Instalação

```bash
# Clone o repositório
git clone https://github.com/caduunisal/consulta-placa-infosimples.git
cd consulta-placa-infosimples

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt


