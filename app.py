from flask import Flask, render_template, request

app = Flask(__name__)

# Sample product data
products = [
    {"name": "All-Purpose Cleaner", "price": "N$50", "description": "Effective on all surfaces."},
    {"name": "Glass Cleaner", "price": "N$40", "description": "Leaves glass streak-free."},
    {"name": "Floor Cleaner", "price": "N$60", "description": "Perfect for all floor types."},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you could handle form submission, save to DB or send email
        name = request.form.get('name')
        message = request.form.get('message')
        # For now, just thank the user
        return render_template('contact.html', success=True, name=name)
    return render_template('contact.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
