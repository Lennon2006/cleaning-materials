from flask import Flask, render_template, request, url_for
from datetime import datetime

# Explicitly set template folder (optional but can help)
app = Flask(__name__, template_folder='templates')

# Home page route
@app.route('/')
def home():
    return render_template("home.html", datetime=datetime)

# Products page route (renamed to avoid name conflict)
@app.route('/products')
def products_page():
    products = [
        {
            "name": "All-Purpose Cleaner",
            "description": "Strong on dirt, gentle on surfaces.",
            "price": 45.00,
            "image": "https://mrsheen.co.za/wp-content/uploads/2020/12/mr-sheen-products-all-purpose-cleaner-sparkle-fresh.jpg",
            "category": "General"
        },
        {
            "name": "Dishwashing Liquid",
            "description": "Cuts grease fast, smells amazing.",
            "price": 30.00,
            "image": "https://tmpn.com/contents/media/l_tauradish.jpg",
            "category": "Kitchen"
        },
        {
            "name": "Laundry Powder",
            "description": "Leaves clothes spotless and fresh.",
            "price": 55.00,
            "image": "https://www.oilflow.co.za/wp-content/uploads/2024/05/BLLP5.png",
            "category": "Laundry"
        },
        {
            "name": "Toilet Bowl Cleaner",
            "description": "Tough on stains, leaves a fresh scent.",
            "price": 35.00,
            "image": "https://m.media-amazon.com/images/I/81TzLur17XL.jpg",
            "category": "Bathroom"
        },
        {
            "name": "Glass & Window Cleaner",
            "description": "Streak-free shine for glass surfaces.",
            "price": 32.00,
            "image": "https://hips.hearstapps.com/hmg-prod/images/ghi-9bestwindowcleaners-1665609031.jpg",
            "category": "General"
        },
        {
            "name": "Mop Set",
            "description": "360° rotating mop with microfiber head.",
            "price": 120.00,
            "image": "https://york.global/wp-content/uploads/zestaw_mop_set_azur.jpg",
            "category": "Tools"
        },
        {
            "name": "Microfiber Cloth Pack (5)",
            "description": "Highly absorbent and reusable cloths.",
            "price": 40.00,
            "image": "https://i5.walmartimages.com/seo/MR-SIGA-Microfiber-Cleaning-Cloth-for-Kitchen-Household-Car-Cleaning-Pack-of-12-Size-12-6-x-12-6_db785677-24bd-446c-a5b2-f2fbd40060a9.66cab9db685072d0ff465877ed4e5bda.jpeg",
            "category": "Tools"
        },
        {
            "name": "Bleach Disinfectant",
            "description": "Kills 99.9% of germs and bacteria.",
            "price": 38.00,
            "image": "https://bf1af2.akinoncloudcdn.com/products/2024/09/10/83171/7fa43c4f-651d-4e86-9fb7-801fb0be3042_size3840_cropCenter.jpg",
            "category": "Disinfectants"
        },
        {
            "name": "Floor Cleaner",
            "description": "Safe for tiles and hardwood, fresh lemon scent.",
            "price": 42.00,
            "image": "https://www.golddrop.eu/uploads/TsProducts/pictures/orginal_picture_1146.jpg",
            "category": "General"
        },
        {
            "name": "Air Freshener Spray",
            "description": "Eliminates odors with long-lasting freshness.",
            "price": 28.00,
            "image": "https://image.made-in-china.com/2f0j00FNRhMpjWyqoy/Good-Quality-Bathroom-Freshener-Air-Freshener-Spray.webp",
            "category": "Air Care"
        }
    ]

    # Extract unique categories (for future filters or display)
    categories = sorted({p['category'] for p in products})

    return render_template("products.html", products=products, categories=categories, datetime=datetime)

# Contact page route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    success = False
    name = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Here you could add real email sending or database logging
        print(f"New message from {name} ({email}): {message}")
        success = True

    return render_template("contact.html", success=success, name=name, datetime=datetime)


if __name__ == '__main__':
    app.run(debug=True)
