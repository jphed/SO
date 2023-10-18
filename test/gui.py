import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

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

    tiempo_total = sum(p.tiempo_ejecucion for p in orden_ejecucion)
    return orden_ejecucion, tiempo_total

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Agregar Proceso"
        self.hi_there["command"] = self.add_process
        self.hi_there.pack(side="top")

        self.run_button = tk.Button(self, text="Ejecutar SJF", command=self.run_sjf)
        self.run_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_process(self):
        process_name = tk.simpledialog.askstring("Input", "Nombre del proceso:",
                                parent=self.master)
        process_time = tk.simpledialog.askinteger("Input", "Tiempo de CPU:",
                                parent=self.master)
        
        if process_name is not None and process_time is not None:
            procesos.append(Proceso(process_name, process_time))

    def run_sjf(self):
        orden_ejecucion, tiempo_total = sjf(procesos)

        result_text = "Orden de ejecución SJF:\n"
        
        for proceso in orden_ejecucion:
            result_text += f"{proceso.nombre}: Tiempo de ejecución = {proceso.tiempo_ejecucion}\n"
        
        result_text += f"Tiempo total de ejecución: {tiempo_total}"

        messagebox.showinfo("Resultado", result_text)

procesos = []

root = tk.Tk()
root.geometry('300x100')
app = Application(master=root)
app.mainloop()
