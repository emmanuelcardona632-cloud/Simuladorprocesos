
import collections
import time

class Proceso:
    def __init__(self, nombre, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_restante = tiempo_ejecucion
        self.estado = "Listo"

def simular_planificacion(lista_procesos, quantum):
    cola = collections.deque(lista_procesos)
    tiempo_total = 0

    print(f"--- INICIO DE SIMULACION (Quantum: {quantum}) ---")
    
    while cola:
        p = cola.popleft()
        p.estado = "Ejecutando"
        
        # Simula el tiempo que el proceso ocupa el CPU
        tiempo_uso = min(p.tiempo_restante, quantum)
        print(f"[Tiempo {tiempo_total}s] {p.nombre} esta en CPU por {tiempo_uso}s")
        
        # Pausa pequeña para que la simulacion se vea real en consola
        time.sleep(0.5) 
        
        p.tiempo_restante -= tiempo_uso
        tiempo_total += tiempo_uso

        if p.tiempo_restante > 0:
            p.estado = "Listo"
            print(f"  -> {p.nombre} no ha terminado. Regresa a la cola.")
            cola.append(p)
        else:
            p.estado = "Terminado"
            print(f"  -> {p.nombre} ha FINALIZADO exitosamente.")

    print(f"--- SIMULACION FINALIZADA EN {tiempo_total}s ---")

# --- Bloque de ejecucion ---
if __name__ == "__main__":
    # Creamos 3 procesos de prueba (Nombre, Tiempo total)
    procesos_iniciales = [
        Proceso("Proceso_A", 8),
        Proceso("Proceso_B", 3),
        Proceso("Proceso_C", 5)
    ]
    
    # El quantum es el tiempo maximo que cada proceso puede estar en CPU
    VALOR_QUANTUM = 3
    simular_planificacion(procesos_iniciales, VALOR_QUANTUM)
