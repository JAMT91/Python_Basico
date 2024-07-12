import random

# Opciones disponibles
opciones = ("piedra", "papel", "tijera")

# Elección aleatoria de la computadora
computer = random.choice(opciones)

# Elección del usuario (puedes pedir input al usuario)
user = random.choice(opciones)  # Ejemplo: el usuario elige "piedra"

# Determinar el ganador
if user == computer:
    print("Empate")
elif (user == "piedra" and computer == "tijera") or (user == "papel" and computer == "piedra") or (user == "tijera" and computer == "papel"):
    print("¡Tú ganas!")
else:
    print("La computadora gana")