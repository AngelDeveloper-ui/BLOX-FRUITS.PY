frutas = {
    "Cohete": 5000,
    "Spin": 7500,
    "Chop": 30000,
    "Spring": 60000,
    "Bomba": 100000,
    "Humo": 250000,
    "Fuego": 250000,
    "Halcón": 300000,
    "Hielo": 350000,
    "Arena": 420000,
    "Oscuridad": 500000,
    "Revivir": 550000,
    "Diamante": 600000,
    "Luz": 650000,
    "Amor": 700000,
    "Goma": 750000,
    "Barrera": 800000,
    "Magma": 850000,
    "Puerta": 950000,
    "Terremoto": 1000000,
    "Humano: Buda": 1200000,
    "Hilo": 1500000,
    "Ave: Fénix": 1800000,
    "Rayo": 2100000,
    "Garra": 2300000,
    "Gravedad": 2500000,
    "Masa": 2800000,
    "Sombra": 3000000,
    "Veneno": 3000000,
    "Control": 3200000,
    "Espíritu": 3400000,
    "Dragón": 3500000,
    "Gas": 3600000,
    "Yeti": 4000000,
    "Kitsune": 8000000,
    "Leopardo": 5000000
}

blox_fruits_rareza = {
    "Cohete": "Común",
    "Spin": "Común",
    "Chop": "Común",
    "Spring": "Común",
    "Bomba": "Común",
    "Humo": "Rara",
    "Fuego": "Rara",
    "Halcón": "Rara",
    "Hielo": "Rara",
    "Arena": "Rara",
    "Oscuridad": "Rara",
    "Revivir": "Rara",
    "Diamante": "Rara",
    "Luz": "Rara",
    "Amor": "Épica",
    "Goma": "Épica",
    "Barrera": "Épica",
    "Magma": "Épica",
    "Puerta": "Épica",
    "Terremoto": "Legendaria",
    "Humano: Buda": "Legendaria",
    "Hilo": "Legendaria",
    "Ave: Fénix": "Legendaria",
    "Rayo": "Legendaria",
    "Garra": "Mítica",
    "Gravedad": "Mítica",
    "Masa": "Mítica",
    "Sombra": "Mítica",
    "Veneno": "Mítica",
    "Control": "Mítica",
    "Espíritu": "Mítica",
    "Dragón": "Mítica",
    "Gas": "Mítica",
    "Yeti": "Mítica",
    "Kitsune": "Legendaria",
    "Leopardo": "Legendaria"
}

pregunta = input("¿QUÉ DESEA HACER? BUSCAR EL PRECIO DE UNA FRUTA (1) O BUSCAR SU RAREZA (2): ")

if pregunta == "1":
    pregunta_fruta = input("¿DE QUÉ FRUTA QUIERE SABER EL PRECIO? :  ")
    respuesta_fruta = frutas.get(pregunta_fruta, "FRUTA NO ENCONTRADA")
    print(f"EL PRECIO DE LA FRUTA {pregunta_fruta}, ES DE : {respuesta_fruta}")
elif pregunta == "2":
    pregunta_rareza = input("DE QUE FRUTA QUIERE SABER LA RAREZA? : ")
    respuesta_rareza = blox_fruits_rareza.get(pregunta_rareza, "FRUTA NO ENCONTRADA")
    print(f"LA RAREZA DE LA FRUTA {pregunta_rareza}, ES DE : {respuesta_rareza}")
