from flask import Flask, request, render_template, json, redirect

app = Flask(__name__)
jsnfile = 'data.json'



@app.route('/', methods=['GET', "POST"])
def index():
    with open(jsnfile, 'r') as ps:
        tareas = json.load(ps)
    return render_template("index.html",  tareas=tareas)

@app.route("/add_tarea", methods = ['GET', 'POST'])
def addTarea():
    if request.method == 'GET':
        return render_template('add_tarea.html',tarea={})
    if request.method == 'POST':
        id_tarea = request.form["id_tarea"]
        nombre_tarea = request.form["nombre_tarea"]
        fecha_inicio = request.form["fecha_inicio"]
        fecha_fin = request.form["fecha_fin"]
        fecha_limite = request.form["fecha_limite"]
        estado_tarea = request.form["estado_tarea"]
        with open(jsnfile, 'r+') as ps:
            tareas = json.load(ps)
        tareas.append({"id_tarea": id_tarea, "nombre_tarea": nombre_tarea, "fecha_inicio": fecha_inicio,"fecha_fin": fecha_fin,"fecha_limite": fecha_limite ,"estado_tarea": estado_tarea})
        with open(jsnfile, 'w') as ps:
            json.dump(tareas, ps)
        return redirect('/')
    

@app.route('/update_tarea/<string:id_tarea>',methods = ['GET','POST'])
def update_tarea(id_tarea):
    with open(jsnfile) as ps:
        tareas = json.load(ps)
    if request.method == 'GET':
        tarea = [x for x in tarea if x['id_tarea'] == id_tarea][0]
        return render_template("add_tarea.html", tarea=tarea)
    if request.method == 'POST':
        for tarea in tareas:
            if(tarea['id_tarea'] == id_tarea):
                tarea['nombre_tarea'] = request.form["nombre_tarea"]
                tarea['fecha_inicio'] = request.form["fecha_inicio"]
                tarea['fecha_fin'] = request.form["fecha_fin"]
                tarea['fecha_fecha_limite'] = request.form["fecha_limite"]
                tarea['estado_tarea'] = request.form["estado_tarea"]
                break
        with open(jsnfile, 'w') as ps:
            json.dump(tareas, ps)
        return redirect('/')


@app.route('/delete_tarea/<string:id_tarea>')
def delete_tarea(id_tarea):
    with open(jsnfile) as ps:
        tareas = json.load(ps)
    new_tarea_list = []
    for tarea in tareas:
        if(tarea['id_tarea'] != id_tarea):
            new_tarea_list.append(tarea)
    with open(jsnfile, 'w') as uw:
        json.dump(new_tarea_list, uw)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)