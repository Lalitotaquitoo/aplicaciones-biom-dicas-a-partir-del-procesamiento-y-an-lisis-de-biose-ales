import pyautogui
import time
import os

class MonitorPuntero:
    def __init__(self, tiempo_espera):
        """
        Inicializa la clase con el tiempo de espera antes de realizar un clic.
        """
        self.tiempo_espera = tiempo_espera
        self.posicion_inicial = None
        self.tiempo_inicio = None


    def obtener_posicion_puntero(self):
        """
        Obtiene y devuelve la posición actual del puntero del ratón.
        """
        return pyautogui.position()

    def tiempo_de_permanencia(self):
        """
        Monitorea la posición del puntero y realiza un clic si el puntero
        permanece en la misma posición durante 'tiempo_espera' segundos.
        """
        self.posicion_inicial = self.obtener_posicion_puntero()
        self.tiempo_inicio = time.time()

        while True:
            posicion_actual = self.obtener_posicion_puntero()
            tiempo_actual = time.time()

            # Imprimir la posición actual del puntero
            print(f'Posición actual del puntero: {posicion_actual}', end='\r')

            # Si la posición no ha cambiado y ha pasado el tiempo de espera, haz clic
            if posicion_actual == self.posicion_inicial and (tiempo_actual - self.tiempo_inicio) >= self.tiempo_espera:
                pyautogui.click()
                print(f"\nClic realizado en la posición: {posicion_actual}")
                # Después del clic, reiniciar la posición y el tiempo de inicio
                self.posicion_inicial = self.obtener_posicion_puntero()
                self.tiempo_inicio = time.time()

            # Si la posición del puntero cambia, reinicia el temporizador
            elif posicion_actual != self.posicion_inicial:
                self.posicion_inicial = posicion_actual
                self.tiempo_inicio = time.time()

            # Pausar un poco antes de la siguiente comprobación
            time.sleep(0.1)

    def iniciar(self):
        """
        Inicia el monitoreo continuo del puntero del ratón.
        """
        try:
            while True:
                self.tiempo_de_permanencia()
        except KeyboardInterrupt:
            print("\nPrograma terminado.")

