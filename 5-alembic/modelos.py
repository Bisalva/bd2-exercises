from sqlalchemy import ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

class Base(DeclarativeBase):
    pass

class ProductoProveedores(Base):
    __tablename__ = "productos_proveedores"
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), primary_key=True)
    proveedor_id: Mapped[int] = mapped_column(ForeignKey("proveedores.id"), primary_key=True)
        
class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] =  mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30), nullable=False,unique=False)
    descripcion: Mapped[str | None] = mapped_column(String(250), nullable=True)
    precio: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer, default= 0 )
        
    # Relaciones
    detalle: Mapped["DetalleProducto"] = relationship(back_populates="producto", uselist=False, cascade = "all, delete-orphan")
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    categoria: Mapped["Categoria"] = relationship(back_populates="productos") 
    proveedores: Mapped[list["Proveedor"]] = relationship(back_populates="productos", secondary = "productos_proveedores")
    
    def __str__(self):
        return f"{self.nombre}: {self.precio} ({self.stock} en stock)"
    
class DetalleProducto(Base):
    __tablename__ = "detalles_productos"
    id: Mapped[int] = mapped_column(primary_key=True)
    peso: Mapped[int] = mapped_column(Integer)
    color: Mapped[str] = mapped_column(String(20))
    material: Mapped[str] = mapped_column(String(20))
    lote: Mapped[str] = mapped_column(String(50))
    
    # Relaciones
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), unique=True)
    producto: Mapped["Producto"] = relationship(back_populates="detalle")
    
    def __str__(self):
        return f"[{self.producto.nombre}] {self.peso}gr , {self.color} - (lote: {self.lote})"

class Categoria(Base):
    __tablename__ = "categorias"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))
    
    # Relaciones
    productos: Mapped[list["Producto"]] = relationship(back_populates="categoria")
    
class Proveedor(Base):
    __tablename__ = "proveedores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    direccion:  Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(100), unique= True)
    
    # Relaciones
    productos: Mapped[list["Producto"]] = relationship(back_populates="proveedores", secondary = "productos_proveedores")
    

DB_URI = "sqlite:///productos_migrations.sqlite3"
engine = create_engine(DB_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
