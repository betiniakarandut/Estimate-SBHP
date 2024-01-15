from flask import Flask

def create_app():
    """Initializes the flask application
    Imports from views.py
    registers physical_properties as a blueprint
    
    Returns:
        app
    """
    app = Flask(__name__)

    from .views import physical_properties
    app.register_blueprint(physical_properties)

    return app
