class Proceso:
    def __init__(self, nombre, tiempo_cpu):
        self.nombre = nombre
        self.tiempo_cpu = tiempo_cpu
        self.tiempo_ejecucion = 0

def sjf(planificacion):
    tiempo_actual = 0
    orden_ejecucion = []

    while len(planificacion) > 0:
        procesos_disponibles = [p for p in planificacion if p.tiempo_cpu <= tiempo_actual]
        if len(procesos_disponibles) == 0:
            tiempo_actual += 1
            continue

        proceso_corto = min(procesos_disponibles, key=lambda p: p.tiempo_cpu)
        orden_ejecucion.append(proceso_corto)
        proceso_corto.tiempo_ejecucion += proceso_corto.tiempo_cpu
        tiempo_actual += proceso_corto.tiempo_cpu
        planificacion.remove(proceso_corto)

    tiempo_total = sum(p.tiempo_ejecucion for p in orden_ejecucion)  # Corrección aquí
    return orden_ejecucion, tiempo_total

# Ejemplo de uso
if __name__ == "__main__":
    procesos = [Proceso("P1", 6), Proceso("P2", 8), Proceso("P3", 7), Proceso("P4", 3)]
    
    orden_ejecucion, tiempo_total = sjf(procesos)
    
    print("Orden de ejecución SJF:")
    for proceso in orden_ejecucion:
        print(f"{proceso.nombre}: Tiempo de ejecución = {proceso.tiempo_ejecucion}")
    
    print(f"Tiempo total de ejecución: {tiempo_total}")
