from flask import Flask


from subprocess import call
from mainModules.matplot import clever_function






def create_app(**config_overrides):
    app = Flask(__name__)
   
    # Apply Overrides for tests
    app.config.update(config_overrides)
    app.jinja_env.globals.update(clever_function=clever_function)
 
  
    # import blueprints
    from prints.views import guest_app

    
    # register blueprints    
    app.register_blueprint(guest_app)
  
    return app
