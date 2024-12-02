from flask import Blueprint, render_template

# Definir el blueprint
gestion_bp = Blueprint('gestion', __name__, url_prefix='/gestion')

# Ruta para subirBlogs
@gestion_bp.route('/menuGestion')
def menuGestion():
    return render_template('gestion/gestion.html')

# Ruta para subirBlogs
@gestion_bp.route('/subirBlogs')
def subirBlogs():
    return render_template('gestion/subirBlogs.html')

# Ruta para subirEvento
@gestion_bp.route('/subirEvento')
def subirEvento():
    return render_template('gestion/subirEvento.html')

# Ruta para subirNovedades
@gestion_bp.route('/subirNovedades')
def subirNovedades():
    return render_template('gestion/subirNovedades.html')

# Ruta para subirNovedades
@gestion_bp.route('/editarBlogs')
def editarBlogs():
    return render_template('gestion/editarBlogs.html')

# Ruta para subirNovedades
@gestion_bp.route('/editarEventos')
def editarEventos():
    return render_template('gestion/editarEventos.html')

# Ruta para subirNovedades
@gestion_bp.route('/editarNovedades')
def editarNovedades():
    return render_template('gestion/editarNovedades.html')
