def calcular_tiempo(diccionario):
    # Crear una lista para almacenar los resultados
    resultados = []

    for proceso_id, proceso_info in diccionario.items():
        burst_time = proceso_info['bursttime']
        arrival_time = proceso_info['arrivaltime']

        # Calcular el tiempo de finalización (completion time)
        completion_time = max(arrival_time, resultados[-1]['completion_time'] if resultados else 0) + burst_time

        # Calcular el turnaround time
        turnaround_time = completion_time - arrival_time

        # Calcular el waiting time
        waiting_time = turnaround_time - burst_time

        # Agregar resultados a la lista de resultados
        resultados.append({
            'id': proceso_id,
            'bursttime': burst_time,
            'arrivaltime': arrival_time,
            'completion_time': completion_time,
            'turnaround_time': turnaround_time,
            'waiting_time': waiting_time
        })

    return resultados

# Ejemplo de uso con 5 procesos
diccionario_procesos = {
    1: {'bursttime': 10, 'arrivaltime': 0},
    2: {'bursttime': 5, 'arrivaltime': 3},
    3: {'bursttime': 8, 'arrivaltime': 5},
    4: {'bursttime': 2, 'arrivaltime': 9},
    5: {'bursttime': 7, 'arrivaltime': 10}
}

resultados = calcular_tiempo(diccionario_procesos)

# Inicializar variables para el promedio
promedio_turnaround = 0
promedio_waiting = 0

# Imprimir resultados y calcular promedios
for resultado in resultados:
    print(f"Proceso {resultado['id']}:")
    print(f"  Burst Time: {resultado['bursttime']}")
    print(f"  Arrival Time: {resultado['arrivaltime']}")
    print(f"  Completion Time: {resultado['completion_time']}")
    print(f"  Turnaround Time: {resultado['turnaround_time']}")
    print(f"  Waiting Time: {resultado['waiting_time']}")
    print()

    # Actualizar los promedios
    promedio_turnaround += resultado['turnaround_time']
    promedio_waiting += resultado['waiting_time']

# Calcular los promedios finales
promedio_turnaround /= len(diccionario_procesos)
promedio_waiting /= len(diccionario_procesos)

print(f"Promedio Turnaround Time: {promedio_turnaround:.1f}")
print(f"Promedio Waiting Time: {promedio_waiting:.1f}")
