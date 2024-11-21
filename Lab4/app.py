from flask import Flask, render_template, request, redirect, flash, abort

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample trips data
trips = [
    {"country": "Turkey", "operator": "TravelPro", "price": 1500, "days": 7},
    {"country": "Spain", "operator": "SunFun", "price": 1800, "days": 10},
    {"country": "Turkey", "operator": "HolidayCo", "price": 2100, "days": 14},
    {"country": "France", "operator": "EuroTrips", "price": 1700, "days": 8},
    {"country": "Italy", "operator": "HolidayCo", "price": 1600, "days": 5},
    {"country": "Turkey", "operator": "TravelPro", "price": 2500, "days": 12},
    {"country": "USA", "operator": "HolidayCo", "price": 3000, "days": 15},
    {"country": "Turkey", "operator": "EuroTrips", "price": 1000, "days": 6},
    {"country": "Egypt", "operator": "SunFun", "price": 1400, "days": 10},
    {"country": "Turkey", "operator": "SunFun", "price": 1200, "days": 5},
]

# Index page with form and trips
@app.route('/', methods=['GET', 'POST'])
def index():
    filtered_trips = trips
    if request.method == 'POST':
        # Get form data
        country = request.form.get('country')
        operator = request.form.get('operator')
        days = request.form.get('days')

        # Validate form input
        if not country and not operator and not days:
            flash('Please provide at least one filter option!', 'danger')
            return render_template('index.html', trips=filtered_trips)

        # Filter trips by country
        if country:
            filtered_trips = [trip for trip in filtered_trips if trip['country'].lower() == country.lower()]

        # Filter trips by operator
        if operator:
            filtered_trips = [trip for trip in filtered_trips if trip['operator'].lower() == operator.lower()]

        # Filter trips by minimum number of days
        if days:
            try:
                days = int(days)
                filtered_trips = [trip for trip in filtered_trips if trip['days'] >= days]
            except ValueError:
                flash('Invalid number of days!', 'danger')

    return render_template('index.html', trips=filtered_trips)

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
