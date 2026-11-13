from flask import Flask, render_template

app = Flask(__name__)

# Public service locations
# Coordinates are approximate and should be verified before deployment.

places = [
    # HOSPITALS
    {"name": "Wenlock District Hospital", "category": "hospital", "lat": 12.8655, "lon": 74.8426, "address": "Hampankatta, Mangaluru"},
    {"name": "A.J. Hospital", "category": "hospital", "lat": 12.8827, "lon": 74.8534, "address": "Kuntikana, Mangaluru"},
    {"name": "Father Muller Medical College Hospital", "category": "hospital", "lat": 12.8788, "lon": 74.8548, "address": "Kankanady, Mangaluru"},
    {"name": "KMC Hospital Attavar", "category": "hospital", "lat": 12.8628, "lon": 74.8434, "address": "Attavar, Mangaluru"},
    {"name": "Yenepoya Medical College Hospital", "category": "hospital", "lat": 12.8144, "lon": 74.8943, "address": "Deralakatte"},
    {"name": "Indiana Hospital", "category": "hospital", "lat": 12.8932, "lon": 74.8583, "address": "Mangaluru"},
    {"name": "Unity Hospital", "category": "hospital", "lat": 12.8740, "lon": 74.8460, "address": "Falnir, Mangaluru"},
    {"name": "Lady Goschen Hospital", "category": "hospital", "lat": 12.8646, "lon": 74.8424, "address": "Hampankatta, Mangaluru"},

    # TEMPLES
    {"name": "Kudroli Gokarnath Temple", "category": "temple", "lat": 12.8746, "lon": 74.8435, "address": "Kudroli, Mangaluru"},
    {"name": "Mangaladevi Temple", "category": "temple", "lat": 12.8552, "lon": 74.8445, "address": "Mangaladevi, Mangaluru"},
    {"name": "Kadri Manjunath Temple", "category": "temple", "lat": 12.8884, "lon": 74.8541, "address": "Kadri, Mangaluru"},

    # SCHOOLS
    {"name": "St Aloysius School", "category": "school", "lat": 12.8706, "lon": 74.8448, "address": "Kodialbail, Mangaluru"},
    {"name": "Canara High School", "category": "school", "lat": 12.8750, "lon": 74.8470, "address": "Dongerkery, Mangaluru"},

    # COLLEGES
    {"name": "St Aloysius College", "category": "college", "lat": 12.8706, "lon": 74.8448, "address": "Kodialbail, Mangaluru"},
    {"name": "Canara College", "category": "college", "lat": 12.8750, "lon": 74.8470, "address": "Mangaluru"},

    # GOVERNMENT OFFICES
    {"name": "Dakshina Kannada Deputy Commissioner's Office", "category": "government", "lat": 12.8699, "lon": 74.8429, "address": "Mangaluru"},
    {"name": "Mangaluru City Corporation", "category": "government", "lat": 12.8691, "lon": 74.8437, "address": "Lalbagh, Mangaluru"},

    # POLICE
    {"name": "Mangaluru North Police Station", "category": "police", "lat": 12.8700, "lon": 74.8430, "address": "Mangaluru"},
    {"name": "Mangaluru South Police Station", "category": "police", "lat": 12.8620, "lon": 74.8430, "address": "Mangaluru"}
]


@app.route("/")
def home():
    return render_template("index.html", places=places)


if __name__ == "__main__":
    app.run(debug=True)