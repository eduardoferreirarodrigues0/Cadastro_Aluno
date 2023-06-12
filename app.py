from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de alunos
alunos = []


@app.route('/homepage')
def home():
    return render_template('homepage.html')
# Rota principal - exibe a lista de alunos cadastrados
@app.route('/')
def index():
    return render_template('index.html', alunos=alunos)

# Rota para adicionar um novo aluno
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        aluno = {'id': len(alunos), 'nome': nome, 'matricula': matricula}
        alunos.append(aluno)
        return redirect('/')
    return render_template('add.html')

# Rota para editar um aluno
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    aluno = next((aluno for aluno in alunos if aluno['id'] == id), None)
    if aluno:
        if request.method == 'POST':
            aluno['nome'] = request.form['nome']
            aluno['matricula'] = request.form['matricula']
            return redirect('/')
        return render_template('edit.html', aluno=aluno)
    return "Aluno não encontrado."

# Rota para excluir um aluno
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    del alunos[id]
    return redirect('/')

if __name__ == '__main__':
    app.run()
