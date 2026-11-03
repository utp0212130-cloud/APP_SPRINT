
from app.core.firebase import db


restaurantes = [
    {
        "name": "El Rincón Poblano",
        "category": "Comida mexicana",
        "city": "Puebla",
        "price": 2,
        "description": "Platillos tradicionales de la gastronomía poblana.",
        "address": "Avenida Juárez 150, Centro, Puebla"
    },
    {
        "name": "La Casa del Mole",
        "category": "Comida mexicana",
        "city": "Puebla",
        "price": 3,
        "description": "Especialidad en mole poblano y comida tradicional.",
        "address": "Calle 5 Oriente, Centro, Puebla"
    },
    {
        "name": "Pizza Roma",
        "category": "Italiana",
        "city": "Puebla",
        "price": 2,
        "description": "Pizzas artesanales y pastas italianas.",
        "address": "Avenida Reforma, Puebla"
    },
    {
        "name": "Sushi House",
        "category": "Japonesa",
        "city": "Puebla",
        "price": 3,
        "description": "Variedad de sushi y platillos japoneses.",
        "address": "Angelópolis, Puebla"
    },
    {
        "name": "Tacos El Güero",
        "category": "Tacos",
        "city": "Puebla",
        "price": 1,
        "description": "Tacos al pastor, bistec y suadero.",
        "address": "Colonia La Paz, Puebla"
    },
    {
        "name": "Café Dulce Aroma",
        "category": "Cafetería",
        "city": "Puebla",
        "price": 2,
        "description": "Café, postres y bebidas calientes.",
        "address": "Centro Histórico, Puebla"
    },
    {
        "name": "Hamburguesas Central",
        "category": "Comida rápida",
        "city": "Puebla",
        "price": 2,
        "description": "Hamburguesas, papas y malteadas.",
        "address": "Avenida Las Torres, Puebla"
    },
    {
        "name": "Mariscos del Puerto",
        "category": "Mariscos",
        "city": "Puebla",
        "price": 3,
        "description": "Cocteles, ceviches y pescados.",
        "address": "Boulevard Atlixco, Puebla"
    },
    {
        "name": "Antojitos Lupita",
        "category": "Antojitos mexicanos",
        "city": "Cholula",
        "price": 1,
        "description": "Quesadillas, tlacoyos y chalupas.",
        "address": "San Pedro Cholula, Puebla"
    },
    {
        "name": "La Terraza Verde",
        "category": "Comida saludable",
        "city": "San Andrés Cholula",
        "price": 2,
        "description": "Ensaladas, bowls y alimentos frescos.",
        "address": "San Andrés Cholula, Puebla"
    }
]


def cargar_restaurantes():
    coleccion = db.collection("restaurants")

    for i, restaurante in enumerate(restaurantes, start=1):
        restaurante_id = f"seed-restaurante-{i:02d}"

        datos = {
            "id": restaurante_id,
            **restaurante
        }

        coleccion.document(restaurante_id).set(datos)

        print(f"Registrado: {restaurante['name']}")

    print("\n¡Se cargaron los 10 restaurantes correctamente!")


if __name__ == "__main__":
    cargar_restaurantes()
