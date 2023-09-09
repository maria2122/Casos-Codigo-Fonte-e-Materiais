from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales.db'
db = SQLAlchemy(app)

# Definição do modelo Sale
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

# Função de inicialização para inserir registros de teste
def initialize_app():
    with app.app_context():
        db.create_all()

        # Verifique se já existem registros na tabela Sale
        if Sale.query.count() == 0:
            sale1 = Sale(product_name="Produto A", quantity=5, price=10.99)
            sale2 = Sale(product_name="Produto B", quantity=2, price=5.49)
            sale3 = Sale(product_name="Produto C", quantity=3, price=8.75)

            db.session.add(sale1)
            db.session.add(sale2)
            db.session.add(sale3)
            db.session.commit()

# Rota da página inicial
@app.route('/')
def index():
    sales = Sale.query.all()
    return render_template('index.html', sales=sales)

# Rota para adicionar vendas (continua como antes)
@app.route('/add_sale', methods=['POST'])
def add_sale():
    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = request.form['quantity']
        price = request.form['price']

        sale = Sale(product_name, quantity, price)
        db.session.add(sale)
        db.session.commit()

    return redirect(url_for('index'))

# Execute a função de inicialização quando app.py é iniciado
if __name__ == '__main__':
    initialize_app()  # Insira registros de teste
    app.run(debug=True)
