from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from util import products
from common.database import SessionLocal
from interfaces import product_interface

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products/")
def create_product(product: product_interface.ProductCreate, db: Session = Depends(get_db)):
    return products.create_product(db=db, product=product)

@router.get("/products/{product_id}", response_model=product_interface.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = products.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, message="Product not found")
    return db_product

@router.get("/products/", response_model=list[product_interface.Product])
def read_all_products(db: Session = Depends(get_db)):
    all_products = products.get_all_products(db)
    return all_products

@router.put("/products/{product_id}", response_model=product_interface.Product)
def update_product(product_id: int, product: product_interface.ProductBase, db: Session = Depends(get_db)):
    return products.update_product(db, product_id, product)

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return products.delete_product(db, product_id)
