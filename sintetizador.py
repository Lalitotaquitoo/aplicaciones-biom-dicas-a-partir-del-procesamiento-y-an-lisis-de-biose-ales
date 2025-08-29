import pyttsx3
from typing import Union

class SintetizadorVoz:
    def __init__(self) -> None:
        self.motor = pyttsx3.init()
        self.motor.setProperty('volume', 1.0)  

    def hablar(self, texto: str, velocidad: int) -> None:
        self.motor.setProperty('rate', velocidad)
        self.motor.say(texto)
        self.motor.runAndWait()


    def cambiar_voz(self, id_voz: int) -> None:
        voces = self.motor.getProperty('voices')
        if 0 <= id_voz < len(voces):
            print(len(voces))
            self.motor.setProperty('voice', voces[id_voz].id)
            print(f"Cambiando a la voz: {voces[id_voz].id}")  # Debugging

        else:
            raise ValueError("El índice de voz está fuera de rango.")

    def cambiar_volumen(self, volumen: Union[float, int]) -> None:
        if 0.0 <= volumen <= 1.0:
            self.motor.setProperty('volume', volumen)
        else:
            raise ValueError("El volumen debe estar entre 0.0 y 1.0.")

    def cambiar_velocidad(self, velocidad: int) -> None:
        if velocidad > 0:
            self.motor.setProperty('rate', velocidad)
        else:
            raise ValueError("La velocidad debe ser un valor positivo.")

    def obtener_voces(self) -> list:
        voces = self.motor.getProperty('voices')
        return [{"id": voz.id, "nombre": voz.name} for voz in voces]
    
    
 

