from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Product
from config import Config

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(Config)
db.init_app(app)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        quantity = request.form['quantity']

        product = Product(name, description, quantity)
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully', 'success')
        return redirect(url_for('index'))

    return render_template('add_product.html')

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get(id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.quantity = request.form['quantity']

        db.session.commit()
        flash('Product updated successfully', 'success')
        return redirect(url_for('index'))

    return render_template('edit_product.html', product=product)

@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('index'))

@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
