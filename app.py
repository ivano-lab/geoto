from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BASE_URL = "https://nominatim.openstreetmap.org/"
HEADERS = {"User-Agent": "TocantinsIA/1.0"}

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")

from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

BASE_URL = "https://nominatim.openstreetmap.org/"
HEADERS = {"User-Agent": "TocantinsIA/1.0"}

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")


# Buscar por nome da cidade
@app.route("/buscar_local")
def buscar_local():
    local = request.args.get("q")
    if not local:
        return jsonify({"error": "Parâmetro 'q' é obrigatório"}), 400

    url = BASE_URL + "search"
    params = {"q": local, "format": "json", "addressdetails": 1}

    resp = requests.get(url, params=params, headers=HEADERS)
    return jsonify(resp.json())


# Buscar reverso (coordenadas → nome)
@app.route("/buscar_coordenadas")
def buscar_coordenadas():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return jsonify({"error": "Parâmetros 'lat' e 'lon' são obrigatórios"}), 400

    url = BASE_URL + "reverse"
    params = {"lat": lat, "lon": lon, "format": "json"}

    resp = requests.get(url, params=params, headers=HEADERS)
    return jsonify(resp.json())


if __name__ == "__main__":
    app.run(debug=True)
