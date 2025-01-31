from machine import Pin, PWM
import utime

# Configuración de los pines PWM para controlar el motor
pwm_m1 = PWM(Pin(22))
pwm_m2 = PWM(Pin(23))

# Configuración de la frecuencia PWM (por ejemplo, 1 kHz)
pwm_m1.freq(1000)
pwm_m2.freq(1000)

def set_speed(motor, duty_cycle):
    """
    Ajusta la velocidad del motor.
    :param motor: Objeto PWM (pwm_m1 o pwm_m2).
    :param duty_cycle: Ciclo de trabajo (0-100, donde 100 es máxima velocidad).
    """
    motor.duty_u16(int(duty_cycle * 65535 / 100))

while True:
    # Motor girando en una dirección al 50% de velocidad
    set_speed(pwm_m1, 25)
    set_speed(pwm_m2, 0)
    utime.sleep(2)

    # Motor detenido
    set_speed(pwm_m1, 0)
    set_speed(pwm_m2, 0)
    utime.sleep(1)

    # Motor girando en la otra dirección al 75% de velocidad
    set_speed(pwm_m1, 0)
    set_speed(pwm_m2, 25)
    utime.sleep(2)

    # Motor detenido
    set_speed(pwm_m1, 0)
    set_speed(pwm_m2, 0)
    utime.sleep(1)+
