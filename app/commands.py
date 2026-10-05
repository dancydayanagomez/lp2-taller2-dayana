"""
Comandos personalizados de terminal (Flask CLI).

Permiten ejecutar tareas administrativas desde la terminal, por ejemplo:

    flask init-db     -> crea las tablas en la base de datos
    flask seed-db     -> carga los productos del JSON a la base de datos

Estos comandos se registran en create_app().
"""

import json
from flask.cli import with_appcontext
import click
from app.extensions import db
from app.models import Categoria, Producto

@click.command("init-db")
@with_appcontext
def init_db():
    db.create_all()
    click.echo("Base de datos creada.")

@click.command("reset-db")
@with_appcontext
def reset_db():
    db.drop_all()
    db.create_all()
    click.echo("Base de datos reiniciada.")

@click.command("seed-db")
@with_appcontext
def seed_db():
    with open("app/data/productos.json") as f:
        data = json.load(f)

    for item in data:
        categoria = Categoria.query.filter_by(nombre=item["categoria"]).first()
        if not categoria:
            categoria = Categoria(nombre=item["categoria"])
            db.session.add(categoria)
            db.session.flush()

        if Producto.query.filter_by(sku=item["sku"]).first():
            continue

        producto = Producto(
            sku=item["sku"],
            marca=item["marca"],
            nombre=item["nombre"],
            precio=item["precio"],
            foto=item.get("foto"),
            stock=item.get("stock", 0),
            activo=item.get("activo", True),
            categoria_id=categoria.id
        )
        db.session.add(producto)

    db.session.commit()
    click.echo("Datos insertados.")

def init_app(app):
    app.cli.add_command(init_db)
    app.cli.add_command(reset_db)
    app.cli.add_command(seed_db)

