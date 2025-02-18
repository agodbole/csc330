from app import app
from flask import render_template, redirect, url_for
from app.forms import PopulationForm, DeleteForm
from app import cities


@app.route('/population', methods=['GET', 'POST'])
def population():
    form = PopulationForm()
    if form.validate_on_submit():
        cities[form.city.data] = form.population.data
        form.city.data = ''
        form.population.data = ''
        return redirect(url_for('population'))
    return render_template('population.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete_record():
    # Need to implememt DeleteForm in forms.py for application to work
    form = DeleteForm()
    if form.validate_on_submit():
        # if the city name input by user is a key in the dictionary
        # then delete it, otherwise, do nothing.
        if form.city.data in cities:
            del cities[form.city.data]
        form.city.data = ''
        # Redirect to the view_all route (view function)
        return redirect(url_for('view'))
    return render_template('delete.html', form=form)

@app.route('/')
@app.route('/view_all')
def view():
    return render_template('view_cities.html', cities=cities)
