
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_crud_restaurant():

    # 1. Crear restaurante
    nuevo_restaurante = {
        "name": "Restaurante de Prueba",
        "category": "Comida mexicana",
        "city": "Puebla",
        "price": 2,
        "description": "Restaurante para pruebas automáticas",
        "address": "Centro, Puebla"
    }

    respuesta = client.post(
        "/api/v1/restaurants/",
        json=nuevo_restaurante
    )

    assert respuesta.status_code == 200

    restaurante = respuesta.json()
    restaurante_id = restaurante["id"]

    # 2. Consultar restaurante
    respuesta = client.get(
        f"/api/v1/restaurants/{restaurante_id}"
    )

    assert respuesta.status_code == 200
    assert respuesta.json()["name"] == "Restaurante de Prueba"

    # 3. Actualizar restaurante
    datos_actualizados = {
        "name": "Restaurante Actualizado",
        "category": "Comida italiana",
        "city": "Puebla",
        "price": 3,
        "description": "Descripción actualizada",
        "address": "Cholula, Puebla"
    }

    respuesta = client.put(
        f"/api/v1/restaurants/{restaurante_id}",
        json=datos_actualizados
    )

    assert respuesta.status_code == 200
    assert respuesta.json()["name"] == "Restaurante Actualizado"

    # 4. Eliminar restaurante
    respuesta = client.delete(
        f"/api/v1/restaurants/{restaurante_id}"
    )

    assert respuesta.status_code == 200

    # 5. Comprobar que ya no existe
    respuesta = client.get(
        f"/api/v1/restaurants/{restaurante_id}"
    )

    assert respuesta.status_code == 404
