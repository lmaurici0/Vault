from src.controllers.controller import *
from src.controllers.error import *

routes = {
    "index_route": "/", "indexcontroller": IndexController.as_view("sucesso no index"),
    "delete_route": "/delete/product/<int:code>", "delete_controller": DeleteProdutoController.as_view("deletado"),
    "update_route": "/update/product/<int:code>", "update_controller": UpdateProdutoController.as_view("aaaaaaaaa"),
    "categories_route": "/create/categorie", "categories_controller": CategoriesController.as_view("categorias"),
    "not_found_route": 404, "not_found_controller": NotFoundController.as_view('error')
}