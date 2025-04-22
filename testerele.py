import RPi.GPIO as GPIO
import time

RELE_GPIO_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RELE_GPIO_PIN, GPIO.OUT)

print("Testando lógica do relé...")

# Teste com LOW
print("Definindo como LOW...")
GPIO.output(RELE_GPIO_PIN, GPIO.LOW)
time.sleep(5)  # Observe o comportamento do relé

# Teste com HIGH
print("Definindo como HIGH...")
GPIO.output(RELE_GPIO_PIN, GPIO.HIGH)
time.sleep(5)  # Observe o comportamento do relé

GPIO.cleanup()
print("Teste concluído.")