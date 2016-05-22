from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from forms import ContactForm

mail = Mail()

app = Flask(__name__)

app.secret_key = 'qwertyuiopasdfghjklzxcvbnm'

# add mail server config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'syedsholok@gmail.com'
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html') 

@app.route('/products')
def products():
  return render_template('products.html') 

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            return ('Please fill in all fields <p><a href="/contact">Try Again!!!</a></p>')
        else:
            msg = Message("Message from your visitor" + form.name.data,
                          sender='syedsholok@gmail.com',
                          recipients=['syedistiak75@gmail.com'])
            msg.body = """
            From: %s <%s>,
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return ("Successfully sent message!")
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

@app.errorhandler(404)
def error404(error):
	return render_template('404.html')

if __name__ == '__main__':
  app.run(debug=True)
