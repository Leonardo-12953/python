import time
import random
import requests

URL_NUVEM = "https://httpbin.org/post"
ID_SENSOR = "SENSOR_FABRICA_01"

def ler_sensor_temperatura():
    return round(random.uniform(20.0, 35.0), 2)

print("--- Iniciando Coleta de Telemetria IoT ---")

# simula 3 leituras consecutivas do sensor
for i in range(1, 4):
    temp = ler_sensor_temperatura()

    # monta o payload do json
    payload = {
        "sensor_id": ID_SENSOR,
        "leitura_id": i,
        "temperatura": temp
    }

print(f"\n[Leitura {i} Enviando dados: {payload}]")

try:
    resposta = requests.post(URL_NUVEM, json=payload, timeout=5)

    if resposta.status_code == 200:
        print(f"-> Sucesso! Dados recebidos pela nuvem (Status {resposta.status_code}).")
    else:
        print(f"-> Falha ao entregar na nuvem. Status: {resposta.status_code}")
except Exception as e:
    print(f"-> Erro de conexão: {e}")

time.sleep(2)

print("\n--- Monitoramento Finalizado ---")
