from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, SelectField, RadioField, validators

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Нужен для работы flash-сообщений

# Данные о поездках (из предыдущей задачи)
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

class TripForm(Form):
    country = SelectField('Select Country', choices=[
        ('Turkey', 'Turkey'), ('Spain', 'Spain'), ('France', 'France')
    ], validators=[validators.DataRequired()])
    
    operator = RadioField('Select Operator', choices=[
        ('TravelPro', 'TravelPro'), ('SunFun', 'SunFun'), ('HolidayCo', 'HolidayCo')
    ], validators=[validators.DataRequired()])

@app.route('/')
def index():
    return render_template('index.html', trips=trips)

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    form = TripForm(request.form)
    if request.method == 'POST' and form.validate():
        country = form.country.data
        operator = form.operator.data
        # Логика для работы с выбранными данными
        flash(f'You selected {country} with operator {operator}', 'success')
        return redirect(url_for('index'))
    return render_template('form_page.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
