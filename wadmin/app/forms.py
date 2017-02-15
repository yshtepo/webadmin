from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class InfoForm(FlaskForm):
    inn = TextField('inn', validators = [Required()])

class LoginInfoForm(FlaskForm):
    login = TextField('login', validators = [Required()])

class AktForm(FlaskForm):
    inn = TextField('inn', validators = [Required()])
