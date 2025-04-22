#!/bin/bash

# Função para ativar o relé
ativar_rele() {
    echo "Ativando o relé..."
    sudo gpioset gpiochip0 17=0
    sleep 2
}

# Função para desativar o relé
desativar_rele() {
    echo "Desativando o relé..."
    sudo gpioget gpiochip0 17 > /dev/null
    sleep 2
}

# Loop principal
while true; do
    ativar_rele
    desativar_rele
done