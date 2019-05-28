from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms import validators, ValidationError

class CompanyForm(Form):
   name = TextField("Nome da Empresa",[validators.Required("Insira o nome da empresa!")])
   submit = SubmitField("Send")