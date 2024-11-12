from main import app
from src.http.midllware import ExceptionMiddleware
from src.http.nomenclature.router import nomenclature_blueprint

app.app.register_blueprint(nomenclature_blueprint)
