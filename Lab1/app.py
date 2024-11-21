from flask import Flask, render_template, abort

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html', trips=trips)

@app.route('/operator/<operator>')
def get_tours_by_operator(operator):
    filtered_trips = [trip for trip in trips if trip['operator'].lower() == operator.lower()]
    if filtered_trips:
        return render_template('index.html', trips=filtered_trips)
    else:
        abort(404)

@app.route('/days/<int:n>')
def get_tours_by_days(n):
    filtered_trips = [trip for trip in trips if trip['days'] >= n]
    if filtered_trips:
        return render_template('index.html', trips=filtered_trips)
    else:
        abort(404)

@app.route('/turkey/expensive')
def get_most_expensive_turkey_trip():
    turkey_trips = [trip for trip in trips if trip['country'].lower() == 'turkey']
    if turkey_trips:
        most_expensive = max(turkey_trips, key=lambda x: x['price'])
        return render_template('index.html', trips=[most_expensive])
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
