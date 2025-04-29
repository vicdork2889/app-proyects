from funciones import get_todos,write_todos
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple3")

reloj = sg.Text('',key='reloj')
label = sg.Text("Escribe una tarea")
input_box = sg.InputText(tooltip="Enter todo", key="tarea")
boton_añadir = sg.Button("Añadir",size=12)
impresion_lista = sg.Listbox(values=get_todos(),key=('tareas'),
                             enable_events =True, size=[45,10])
boton_editar = sg.Button("editar")
boton_completar = sg.Button("completada")
boton_salida = sg.Button("salida")


putamadre = sg.Window('Lista de tareas',
                      layout =[[reloj],
                          [label],[input_box,boton_añadir],
                               [impresion_lista,boton_editar, boton_completar],
                               [boton_salida]],
                      font =('Helvetica',20))

while True:
    momento,valores = putamadre.read(timeout=10)
    putamadre["reloj"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match momento:
        case "Añadir":
            tarea = get_todos()
            nueva_tarea= valores['tarea'] + "\n"
            tarea.append(nueva_tarea)
            write_todos(tarea)
            putamadre["tareas"].update(values=tarea)

        case "editar":
            try:
                tarea_editada = valores['tareas'][0]
                nueva_tarea = valores['tarea']+'\n'
                tareas = get_todos()
                index = tareas.index(tarea_editada)
                tareas[index] = nueva_tarea
                write_todos(tareas)
                putamadre["tareas"].update(values=tareas)
            except IndexError:
                sg.popup("porfavor primero elige una tarea", font=("Helvetica",16))

        case "completada":
            try:
                tareas_a_completar = valores['tareas'][0]
                tareas = get_todos()
                tareas.remove(tareas_a_completar)
                write_todos(tareas)
                putamadre["tareas"].update(values=tareas)
                putamadre["tarea"].update(value='')
            except IndexError:
                sg.popup("porfavor primero elige una tarea", font=("Helvetica",16))

        case "salida":
            break

        case 'tareas':
            putamadre['tarea'].update(value=valores['tareas'][0])

        case sg.WIN_CLOSED:
            break

putamadre.close()




