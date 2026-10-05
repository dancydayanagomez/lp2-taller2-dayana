"""
Modelos de datos (ORM SQLAlchemy).

Cada clase que hereda de db.Model representa una TABLA de la base de datos,
y cada atributo db.Column representa una COLUMNA. SQLAlchemy se encarga de
traducir estas clases a SQL y de convertir las filas en objetos Python.
"""
from app.extensions import db

class Categoria(db.Model):
    """Categoría a la que pertenece un producto (Periféricos, Audio, etc.)."""

    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    productos = db.relationship("Producto", backref="categoria", lazy=True)

    def __repr__(self):
        """Representación legible del objeto (útil al depurar)."""
        # TODO 2: Retorna algo como f"<Categoria {self.nombre}>"
        return f"<Categoria {self.nombre}>"


class Producto(db.Model):
    """Producto del catálogo de la tienda."""

    __tablename__ = "productos"

    # Clave primaria autoincremental. Nota que ahora el SKU deja de ser
    # el identificador interno: la base de datos usa un id numérico.
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(20), unique=True, nullable=False)
    marca = db.Column(db.String(80), nullable=False)
    nombre = db.Column(db.String(160), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    foto = db.Column(db.String(200))
    stock = db.Column(db.Integer, default=0, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)

    @property
    def disponible(self):
        return self.activo and self.stock > 0

    def __repr__(self):
        return f"<Producto {self.sku} - {self.nombre}>"

        TODO 6: Retorna True solamente si self.activo es verdadero
                Y self.stock es mayor que 0.
        """
        pass
