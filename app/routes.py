"""
Rutas (vistas) de la Tienda Virtual.

CAMBIO CLAVE respecto al Taller 1:
ya NO leemos productos.json en cada petición. Ahora consultamos la base de
datos a través del ORM. Las funciones cargar_productos() y
buscar_producto_por_sku() desaparecen y se reemplazan por consultas
SQLAlchemy como Producto.query.all() o Producto.query.filter_by(...).
"""

from flask import render_template, request
from app.models import Producto, Categoria

def init_app(app):
    @app.route("/")
    def index():
        categoria_id = request.args.get("categoria", type=int)
        if categoria_id:
            productos = Producto.query.filter_by(categoria_id=categoria_id).all()
        else:
            productos = Producto.query.all()
        categorias = Categoria.query.all()
        return render_template("index.html", productos=productos, categorias=categorias)

    @app.route("/producto/<sku>")
    def detalle(sku):
        producto = Producto.query.filter_by(sku=sku).first_or_404()
        return render_template("detalle.html", producto=producto)

    @app.route("/categorias")
    def categorias():
        categorias = Categoria.query.all()
        return render_template("categorias.html", categorias=categorias)
