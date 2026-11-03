
from pathlib import Path

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.api.v1.restaurants import router as restaurants_router
from app.services.restaurant_service import RestaurantService


# Rutas de las carpetas
BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "app" / "templates")
)


# Aplicación FastAPI
app = FastAPI(
    title="FriendlyEats FastAPI",
    description="Sistema de restaurantes locales de Puebla",
    version="1.0.0"
)


# Archivos estáticos
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


# API de restaurantes
app.include_router(restaurants_router)


# Servicio
service = RestaurantService()


# Página principal
@app.get("/")
async def home():
    return RedirectResponse(
        url="/restaurants",
        status_code=303
    )


# Mostrar restaurantes
@app.get("/restaurants")
async def restaurant_list(
    request: Request,
    city: str = None,
    category: str = None,
    price: int = None
):
    restaurants = service.filter_restaurants(city, category, price)

    return templates.TemplateResponse(
        request=request,
        name="restaurants.html",
        context={
            "restaurants": restaurants
        }
    )


# Mostrar formulario para agregar
@app.get("/restaurants/new")
async def new_restaurant_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="restaurant_form.html",
        context={
            "restaurant": None
        }
    )


# Guardar nuevo restaurante
@app.post("/restaurants/new")
async def create_restaurant(
    name: str = Form(...),
    category: str = Form(...),
    city: str = Form(...),
    price: int = Form(...),
    description: str = Form(""),
    address: str = Form("")
):
    restaurant_data = {
        "name": name,
        "category": category,
        "city": city,
        "price": price,
        "description": description,
        "address": address
    }

    service.create_restaurant(restaurant_data)

    return RedirectResponse(
        url="/restaurants",
        status_code=303
    )


# Mostrar detalles de un restaurante
@app.get("/restaurants/{restaurant_id}")
async def restaurant_detail(
    request: Request,
    restaurant_id: str
):
    restaurant = service.get_restaurant(restaurant_id)

    if not restaurant:
        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return templates.TemplateResponse(
        request=request,
        name="restaurant_detail.html",
        context={
            "restaurant": restaurant
        }
    )


# Mostrar formulario de edición
@app.get("/restaurants/{restaurant_id}/edit")
async def edit_restaurant_form(
    request: Request,
    restaurant_id: str
):
    restaurant = service.get_restaurant(restaurant_id)

    if not restaurant:
        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return templates.TemplateResponse(
        request=request,
        name="restaurant_form.html",
        context={
            "restaurant": restaurant
        }
    )


# Guardar cambios
@app.post("/restaurants/{restaurant_id}/edit")
async def update_restaurant(
    restaurant_id: str,
    name: str = Form(...),
    category: str = Form(...),
    city: str = Form(...),
    price: int = Form(...),
    description: str = Form(""),
    address: str = Form("")
):
    restaurant_data = {
        "name": name,
        "category": category,
        "city": city,
        "price": price,
        "description": description,
        "address": address
    }

    updated = service.update_restaurant(
        restaurant_id,
        restaurant_data
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return RedirectResponse(
        url=f"/restaurants/{restaurant_id}",
        status_code=303
    )


# Eliminar restaurante
@app.post("/restaurants/{restaurant_id}/delete")
async def delete_restaurant(restaurant_id: str):
    deleted = service.delete_restaurant(restaurant_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return RedirectResponse(
        url="/restaurants",
        status_code=303
    )


# Verificar funcionamiento
@app.get("/health")
async def health():
    return {"status": "ok"}
