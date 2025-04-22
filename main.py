import RPi.GPIO as GPIO
import requests
import time

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