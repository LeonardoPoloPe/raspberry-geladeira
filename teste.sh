#!/bin/bash

# Certifique-se de que estamos executando como root
if [ "$(id -u)" -ne 0 ]; then
   echo "Este script precisa ser executado como root" 
   exit 1
fi

# Exportar o pino (se já estiver exportado, pode falhar, mas continuamos)
echo "17" > /sys/class/gpio/export 2>/dev/null || true

# Aguarde um momento para o sistema processar
sleep 0.5

# Configurar como saída
echo "out" > /sys/class/gpio/gpio17/direction

# Definir como LOW (ativar relé)
echo "0" > /sys/class/gpio/gpio17/value
echo "Relé deve estar ATIVADO agora (LOW)"
sleep 3

# Definir como HIGH (desativar relé)
echo "1" > /sys/class/gpio/gpio17/value
echo "Relé deve estar DESATIVADO agora (HIGH)"
sleep 3

# Liberar o pino
echo "17" > /sys/class/gpio/unexport

echo "Teste concluído"