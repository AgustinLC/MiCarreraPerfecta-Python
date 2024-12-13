from flask import Flask
from extensions import mysql
from config import Config
from routes.example_routes import example_bp
from routes.preference_group_routes import preference_bp
from routes.questions_routes import questions_bp
from routes.branch_routes import branch_bp
from routes.career_routes import career_bp

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    # Configuración de la aplicación
    app.config.from_object(Config)
    # Inicializar las extensiones
    mysql.init_app(app)
    # Registrar las rutas
    app.register_blueprint(example_bp, url_prefix='/api')
    app.register_blueprint(preference_bp, url_prefix='/api')
    app.register_blueprint(questions_bp, url_prefix='/api')
    app.register_blueprint(branch_bp, url_prefix='/api')
    app.register_blueprint(career_bp, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
