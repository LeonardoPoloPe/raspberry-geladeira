import RPi.GPIO as GPIO
import time

RELE_GPIO_PIN = 17  # GPIO17 = pino físico 11

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RELE_GPIO_PIN, GPIO.OUT)

print("Iniciando novo teste do relé...")

try:
    while True:
        print("Ligando relé...")
        GPIO.output(RELE_GPIO_PIN, GPIO.HIGH)  # <<< Mudei aqui!
        time.sleep(2)

        print("Desligando relé...")
        GPIO.output(RELE_GPIO_PIN, GPIO.LOW)   # <<< E aqui!
        time.sleep(2)

except KeyboardInterrupt:
    print("Teste interrompido pelo usuário.")

finally:
    GPIO.cleanup()
    print("GPIO limpo. Fim do teste.")
