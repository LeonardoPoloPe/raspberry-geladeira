import RPi.GPIO as GPIO
import time
import os

RELE_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("Controlando o relé com base no comportamento observado...")

try:
    while True:
        # Ativar o relé (configurando como saída)
        print("Ativando o relé...")
        GPIO.setup(RELE_PIN, GPIO.OUT)
        GPIO.output(RELE_PIN, GPIO.LOW)  # ou GPIO.HIGH, ambos parecem funcionar
        time.sleep(2)
        
        # Desativar o relé (configurando como entrada)
        print("Desativando o relé...")
        GPIO.setup(RELE_PIN, GPIO.IN)  # Configura como entrada (alta impedância)
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário")
    
finally:
    GPIO.cleanup()
    print("GPIO limpo")