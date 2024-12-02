from flask import Flask, render_template
from gestion import gestion_bp  # Importa el blueprint de gestión

app = Flask(__name__)

# Registrar el blueprint de gestión
app.register_blueprint(gestion_bp)

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

@app.route('/guides')
def guides():
    return render_template('guides.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/curso')
def curso():
    return render_template('curso.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/mapping')
def mapping():
    return render_template('mapping.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post_id=post_id)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=3333)  # Esto escucha en todas las interfaces
