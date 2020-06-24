from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class WerknemerForm(FlaskForm):
    werknemerId = StringField('WerknemerID', validators=[DataRequired()])
    voornaam = StringField('Voornaam', validators=[DataRequired()])
    achternaam = StringField('Achternaam', validators=[DataRequired()])
    adres = StringField('Adres', validators=[DataRequired()])
    woonplaats = StringField('Woonplaats', validators=[DataRequired()])
    salaris = StringField('Salaris', validators=[DataRequired()])
    geboortedatum = StringField('Geboortedatum', validators=[DataRequired()])
    telefoonnummer = StringField('Telefoonnummer', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')
