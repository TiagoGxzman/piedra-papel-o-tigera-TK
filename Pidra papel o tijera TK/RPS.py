import random

ganadas = 0
perdidas = 0
empates = 0

def jugar():
    opciones = ['piedra', 'papel', 'tigera']
    usuario = input("Elige: piedra, papel o tigera ~~ ").lower()
    npc = random.choice(opciones)
    
    print(f"El NPC eligió {npc}")
    
    if usuario == npc:
        print("Empate crack")
        return "empate"
    else:
        if usuario == 'piedra':
            if npc == 'tigera':
                print("Tu piedrota se la metió doblada a las tigeras de NPC")
                return "ganada"
            else:
                print("La piedra de NPC te aplastó noob")
                return "perdida"
        elif usuario == 'papel':
            if npc == 'piedra':
                print("WIN, tu papel envolvió la piedra fea de NPC")
                return "ganada"
            else:
                print("Te envolvieron hasta la ch**ba, qué mal, perdiste")
                return "perdida"
        elif usuario == 'tigera':
            if npc == 'papel':
                print("Ganaste pa.")
                return "ganada"
            else:
                print("Perdiste pa.")
                return "perdida"
        else:
            print("Opción no válida")
            return "empate"

# Jugar 3 veces
for i in range(3):
    resultado = jugar()
    if resultado == "ganada":
        ganadas += 1
    elif resultado == "perdida":
        perdidas += 1
    elif resultado == "empate":
        empates += 1

# Mostrar resultados
print("Los resultados son:")
print(f"Ganadas: {ganadas}")
print(f"Perdidas: {perdidas}")
print(f"Empates: {empates}")