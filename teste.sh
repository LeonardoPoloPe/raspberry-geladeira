# Exportar o pino 17
echo "17" > /sys/class/gpio/export
# Configurar como saída
echo "out" > /sys/class/gpio/gpio17/direction
# Definir como LOW
echo "0" > /sys/class/gpio/gpio17/value
# Aguardar
sleep 2
# Definir como HIGH
echo "1" > /sys/class/gpio/gpio17/value
# Liberar o pino
echo "17" > /sys/class/gpio/unexport