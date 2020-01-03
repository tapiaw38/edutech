from wtforms import Form, StringField, TextField, TextAreaField, validators, HiddenField
from wtforms.fields.html5 import EmailField


def length_honeypot(form,field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')
    
def blank_True(form,field):
    if len(field.data)>0:
        validators.Email(message='Ingrese un email valido')
        

class ComentarioForm(Form):
      # TODO: Define form fields here}
    usuario = StringField('Nombre y apellido', [validators.Length(min=4, max=30, message='Ingrese su nombre'),
                                             validators.DataRequired()])
    email = EmailField('Correo electronico', [blank_True])
    tel = StringField('Celular',[validators.Length(min=10,max=10, message="Ingrese un número correcto sin 0 y 15"),
                      validators.DataRequired()])
    comentario = TextAreaField('Mensaje',[validators.Length(min=4, max=100, message='Ingrese un mensaje valido'),
                                             validators.DataRequired()])

    honeypot = HiddenField('',[length_honeypot])