class Proceso:
    def __init__(self, nombre, tiempo_cpu):
        self.nombre = nombre
        self.tiempo_cpu = tiempo_cpu

def sjf(planificacion):
    tiempo_actual = 0
    orden_ejecucion = []

    while len(planificacion) > 0:
        procesos_disponibles = [p for p in planificacion if p.tiempo_cpu <= tiempo_actual]
        if len(procesos_disponibles) == 0:
            tiempo_actual += 1
            continue

        proceso_corto = min(procesos_disponibles, key=lambda p: p.tiempo_cpu)
        orden_ejecucion.append(proceso_corto.nombre)
        tiempo_actual += proceso_corto.tiempo_cpu
        planificacion.remove(proceso_corto)

    return orden_ejecucion

# Ejemplo de uso
if __name__ == "__main__":
    procesos = [Proceso("P1", 6), Proceso("P2", 8), Proceso("P3", 7), Proceso("P4", 3)]
    
    orden_ejecucion = sjf(procesos)
    
    print("Orden de ejecución SJF:")
    print(" -> ".join(orden_ejecucion))
