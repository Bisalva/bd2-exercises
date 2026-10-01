from fastapi import FastAPI, HTTPException
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Base de datos
engine = create_engine("sqlite:///productos.sqlite3")
#engine = create_engine("postgresql+pyscopg:///productos.sqlite3")

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__= "productos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    precio: Mapped[int] = mapped_column(Integer) 
    
# API
app = FastAPI()
Session = sessionmaker(engine)

@app.get("/productos")
def listar_productos():
    with Session() as session:
        productos = session.execute(select(Producto)).scalars().all()
        return productos
    
@app.post("/productos/{nombre}/{precio}")
def insertar_producto(NOMBRE: str, precio:int):
    with Session() as session:
        nuevo_producto = Producto(nombre = NOMBRE, precio = precio)
        session.add(nuevo_producto)
        session.commit()
        session.refresh(nuevo_producto)
        return nuevo_producto
        
@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    with Session() as session:
        producto = session.get(Producto, producto_id)
        if producto is None:
            raise HTTPException(status_code=404, detail="producto no encontrado")
        return producto

    
    
    
    
    
