from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import datetime

from db.database import SessionLocal
from models.models import Gasto

router = APIRouter()
router = APIRouter()
templates = Jinja2Templates(directory="templates")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/carga_gastos", response_class=HTMLResponse)
async def formulario(request: Request):
    return templates.TemplateResponse(
        "carga_gastos.html",
        {"request": request}
    )
@router.post("/carga_gastos", response_class=HTMLResponse)
async def cargar_gastos(
    request: Request,
    gasto: str = Form(...),
    monto: str = Form(...),
    fecha: str = Form(...),
    desc: str = Form(...),
    db: Session = Depends(get_db)
):
    # Normalizar monto (por si viene con coma)
    monto_float = float(monto.replace(",", "."))

    gasto_db = Gasto(
        gasto=gasto,
        monto=monto_float,
        fecha=datetime.strptime(fecha, "%Y-%m-%d").date(),
        descripcion=desc
    )

    try:
        db.add(gasto_db)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return templates.TemplateResponse(
        "resultado_gasto.html",
        {
            "request": request,
            "gasto": gasto,
            "monto": monto_float,
            "fecha": fecha,
            "desc": desc
        }
    )
