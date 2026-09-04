import time
from machine import Pin, PWM

# Configura o pino do sinal do servo (ex: pino 16)
s_dir = PWM(Pin(6))
s_esq = PWM(Pin(0))
s_dir.freq(50)
s_esq.freq(50)
# Função para converter ângulo em ciclo de trabalho (duty cycle)
def servoDir_angle(angle):
    # Converte o ângulo (0-180) para um valor de ciclo de trabalho de 16 bits (0-65535)
    # 1ms pulso (0°) = ~3.276
    # 2ms pulso (180°) = ~6.553
    min_duty = 1800   # Pode precisar de ajuste fino (1000 a 2000 dependendo do modelo)
    max_duty = 8200   # Pode precisar de ajuste fino (8000 a 8500)
    
    duty_range = max_duty - min_duty
    duty_cycle = min_duty + int((angle / 180.0) * duty_range)
    s_dir.duty_u16(duty_cycle)

def servoEsq_angle(angle):
    # Converte o ângulo (0-180) para um valor de ciclo de trabalho de 16 bits (0-65535)
    # 1ms pulso (0°) = ~3.276
    # 2ms pulso (180°) = ~6.553
    min_duty = 1800   # Pode precisar de ajuste fino (1000 a 2000 dependendo do modelo)
    max_duty = 8200   # Pode precisar de ajuste fino (8000 a 8500)
    
    duty_range = max_duty - min_duty
    duty_cycle = min_duty + int((angle / 180.0) * duty_range)
    s_esq.duty_u16(duty_cycle)

# Exemplo de movimentação
while True:
    for i in range(180):
        servoDir_angle(i)
        servoEsq_angle(i)
        time.sleep(0.1)