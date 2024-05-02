from flask import Flask
from src.router.routes import *

app = Flask(__name__)

app.config.from_mapping(
    secret_key = 'development'
)

app.add_url_rule(routes["index_route"], view_func=routes["indexcontroller"])

app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])

app.add_url_rule(routes["categories_route"], view_func=routes["categories_controller"])

app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])

if __name__ == '__main__':
    app.run(debug=True)
