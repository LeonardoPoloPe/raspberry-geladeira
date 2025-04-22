import RPi.GPIO as GPIO
import requests
import time
import json

# CONFIGURAÇÃO
RELE_GPIO_PIN = 17  # Altere se desejar outro pino
API_URL = 'https://leonardopolo.com.br/geladeira/verificarstatus.php?id=1'
CHECAR_A_CADA_SEGUNDOS = 1  # Frequência de checagem

def ligar_rele():
    GPIO.output(RELE_GPIO_PIN, GPIO.HIGH)
    print("Relé LIGADO (Destravada)")

def desligar_rele():
    GPIO.output(RELE_GPIO_PIN, GPIO.LOW)
    print("Relé DESLIGADO (Travada)")

def checar_status():
    try:
        resp = requests.get(API_URL, timeout=5)
        print(f"Response status code: {resp.status_code}")
        print(f"Response content: {resp.text}")
        
        if resp.status_code != 200:
            print(f"API returned error status code: {resp.status_code}")
            return
            
        data = resp.json()
        if not data.get("success"):
            print("API retornou erro.")
            return

        status = data.get("status", "")
        print(f"Status recebido: {status}")

        if status == "Destravada":
            ligar_rele()
        elif status == "Travada":
            desligar_rele()
        else:
            print("Status desconhecido! Nenhuma ação tomada.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição HTTP: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        print(f"Conteúdo recebido: {resp.text if 'resp' in locals() else 'N/A'}")
    except Exception as e:
        print(f"Erro ao consultar API: {e}")

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RELE_GPIO_PIN, GPIO.OUT)
    desligar_rele()  # Inicializa desligado

    try:
        while True:
            checar_status()
            time.sleep(CHECAR_A_CADA_SEGUNDOS)
    except KeyboardInterrupt:
        print("Encerrando programa.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()