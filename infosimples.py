from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_TOKEN = "JSAcO4lxSL_ABqvvIlfPfohHAIZoAed6qfRCc7ZX"
API_URL = "https://api.infosimples.com/api/v2/consultas/detran/sp/debitos"
#API_URL = 'https://api.infosimples.com/api/v2/consultas/ecrvsp/veiculos/base-sp'

TEMPLATE = """
<h2>Status do Veículo</h2>
<ul>
  <li><strong>Placa:</strong> {{ data['placa'] }}</li>
  <li><strong>Renavam:</strong> {{ data['renavam'] }}</li>
  <li><strong>IPVA:</strong> {{ data['ipva'] }}</li>
  <li><strong>Multas:</strong> R$ {{ data['normalizado_multas_total'] }}</li>
  <li><strong>Status Licenciamento:</strong> {{ data['status_licenciamento'] }}</li>
  <li><strong>Último Licenciamento:</strong> {{ data['ultimo_licenciamento'] }}</li>
  <li><strong>Restrição Financeira:</strong> {{ data['restricao_financeira'] }}</li>
  <li><strong>Restrição Administrativa:</strong> {{ data['restricao_administrativa'] }}</li>
  <li><strong>Restrição Judicial:</strong> {{ data['restricao_judiciaria'] }}</li>
</ul>
"""

@app.route("/consulta", methods=["GET"])
def consulta_status():
    placa = request.args.get("placa")
    renavam = request.args.get("renavam")

    if not placa or not renavam:
        return "Parâmetros 'placa' e 'renavam' são obrigatórios", 400

    payload = {
        "placa": placa,
        "renavam": renavam,
        "token": API_TOKEN,
        "timeout": 120,
        "cache": "false"
    }

    response = requests.get(API_URL, params=payload)

    if response.status_code == 200:
        resp_json = response.json()
        if resp_json.get("data"):
            return render_template_string(TEMPLATE, data=resp_json["data"][0])
        else:
            return "Nenhum dado encontrado para os parâmetros informados.", 404
    else:
        return f"Erro {response.status_code}: {response.text}", response.status_code


if __name__ == "__main__":
    app.run(debug=True, port=5051)
