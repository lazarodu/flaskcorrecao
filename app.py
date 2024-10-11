from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Carros
app.config['SECRET_KEY'] = 'er4e43tre5y5'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/correcao"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    dados = Carros.query.all()
    return render_template('index.html', dados = dados)

@app.route('/add')
def add():
    return render_template('carro_add.html')

@app.route('/save', methods=['POST'])
def save():
    marca = request.form.get('marca')
    modelo = request.form.get('modelo')
    ano = request.form.get('ano')
    if marca and modelo and ano:
        carro = Carros(marca, modelo, ano)
        db.session.add(carro)
        db.session.commit()
        flash('Carro salvo com sucesso!!!')
        return redirect('/')
    else:
        flash('Preencha todos os dados!!!')
        return redirect('/add')

if __name__ == '__main__':
    app.run()
    