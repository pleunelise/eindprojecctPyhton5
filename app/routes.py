from app import app
from app.forms import WerknemerForm
from flask import render_template, flash, redirect


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/werknemers', methods=['GET', 'POST'])
def werknemers():
    form = WerknemerForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.werknemer.data, form.remember_me.data))
        return redirect('/tijdslots')
    return render_template('werknemers.html', title='Werknemers', form=form)


@app.route('/tijdslots', methods=['GET', 'POST'])
def tijdslots():
    return render_template('tijdslots.html', title='Tijdslots')

@app.route('/planning', methods=['GET'])
def planning():
    return render_template('planning.html', title='Planning')
