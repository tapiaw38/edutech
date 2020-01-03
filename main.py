from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import flash
from flask import copy_current_request_context
import forms
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db
from models import Consulta
from flask_mail import Message, Mail
import smtplib
import time
import threading

#nuevo objeto
app =Flask(__name__, template_folder='templates')
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
mail = Mail()



#ruta para el usuario

@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('index.html')

#--------------------------ruta cursos informatica
@app.route('/curso_infor')
def curso_infor():
    return render_template('cursos_infor/cursos_informatica.html')

@app.route('/linux_basico')
def linux_basico():
    return render_template('cursos_infor/linux_basico.html')


#---------------------------ruta de envio de mensajes
@app.route('/contacto', methods=['GET','POST'])
def contacto():

    contacto = forms.ComentarioForm(request.form)
    if request.method == 'POST' and contacto.validate():
        mensaje = Consulta(usuario = contacto.usuario.data,
                             email = contacto.email.data,
                            comentario = contacto.comentario.data)
        db.session.add(mensaje)
        db.session.commit()

        #crear funcion puente para segundo plano de mensaje
        @copy_current_request_context
        def envio_mensaje(usuario, tel, email, comentario):
            envio_email(usuario, tel, email, comentario)

        #llamar a la funcion enviar
        sender = threading.Thread(name='envio_email',target=envio_mensaje,
                                  args=(contacto.usuario,contacto.tel , contacto.email,contacto.comentario))
        sender.start()

        success_message = 'Mensaje enviado exitosamente, en breve nos pondremos en contacto contigo'
        flash(success_message)

    return render_template('contacto.html', form=contacto) 

#recibe los paramentros de la funcion cotacto
def envio_email(usuario,tel, email, comentario):

    msg = Message('Consulta enviada', sender=app.config['MAIL_USERNAME'],
                  recipients=['waltertapia153@gmail.com'])
    msg.html = render_template('email.html', user_name=usuario,
                               user_tel=tel,
                               user_mail=email,
                               user_mensaje=comentario)
    mail.send(msg)







'''
@app.route('/clientes')
def clientes():
    list_cliente=['walter tapia','leon tapia','patricia usqueda']
    return render_template('lista_clientes.html', lista=list_cliente)

@app.route('/cliente/<int:id>/')
def saluda(id=1):
    #param = request.args.get('param1','no contiene paramentro')
    return render_template('usuario.html',ides=id)
    
    @app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie','cctec')
    return response
    
        custome_cookie = request.cookies.get('custome_cookies','undefinide')
'''

#encargada de ejecutar el servidor
#debug true a la escuecha de ca,bios

if __name__== '__main__':
    csrf.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000)


