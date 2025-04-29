from funciones import get_todos,write_todos
import FreeSimpleGUI as sg

label = sg.Text("Escribe una tarea")
print('cometela')
input_box = sg.InputText(tooltip="Enter todo", key="tarea")
boton_añadir = sg.Button("Añadir")
impresion_lista = sg.Listbox(values=get_todos(),key=('tareas'),
                             enable_events =True, size=[45,10])
boton_editar = sg.Button("editar")
boton_completar = sg.Button("completada")
boton_salida = sg.Button("salida")


putamadre = sg.Window('Lista de tareas',
                      layout =[[label],[input_box,boton_añadir],
                               [impresion_lista,boton_editar, boton_completar],
                               [boton_salida]],
                      font =('Helvetica',20))

while True:
    momento,valores = putamadre.read()
    print(1,momento)
    print(2,valores)
    print(3,valores['tarea'])
    match momento:
        case "Añadir":
            tarea = get_todos()
            nueva_tarea= valores['tarea'] + "\n"
            tarea.append(nueva_tarea)
            write_todos(tarea)
            putamadre["tareas"].update(values=tarea)

        case "editar":
            tarea_editada = valores['tareas'][0]
            nueva_tarea = valores['tarea']+'\n'
            tareas = get_todos()
            index = tareas.index(tarea_editada)
            tareas[index] = nueva_tarea
            write_todos(tareas)
            putamadre["tareas"].update(values=tareas)

        case "completada":
            tareas_a_completar = valores['tareas'][0]
            tareas = get_todos()
            tareas.remove(tareas_a_completar)
            write_todos(tareas)
            putamadre["tareas"].update(values=tareas)
            putamadre["tarea"].update(value='')

        case "salida":
            break

        case 'tareas':
            putamadre['tarea'].update(value=valores['tareas'][0])

        case sg.WIN_CLOSED:
            break

putamadre.close()




