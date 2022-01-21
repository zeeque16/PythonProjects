from flask import Flask, render_template, request, redirect

app = Flask(__name__)

taskList = ['Hello']
doneTasks = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        taskList.append(request.form['todo'])

        return redirect('/')
    
    else:
        return render_template('index.html', taskList=taskList, doneTasks=doneTasks)

@app.route("/delete/<int:index>", methods=['GET', 'POST'])
def delete(index):
    if (request.form.get('delete') == 'Delete'):
        del taskList[index]
    elif (request.form.get('done') == 'Done'):
        doneTasks.append(taskList[index])
        del taskList[index]

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)