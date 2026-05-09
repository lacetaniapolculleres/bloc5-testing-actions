# DAW-M485-Bloc2-Paper-01 25-26
# Solucions dels exercicis 2, 3 i 4 (s'exclouen l'1 i el 5 per la T02)

videojocs = [
    {
        "titol": "The Legend of Zelda",
        "any_llancament": 2017,
        "genere": "Aventura",
        "plataforma": "Nintendo Switch",
        "puntuacio": 9.7,
        "desenvolupador": {"nom": "Nintendo", "pais": "Japó"},
        "dlcs": ["Master Trials", "Champions' Ballad"],
        "preu": 59.99
    },
    {
        "titol": "Cyberpunk 2077",
        "any_llancament": 2020,
        "genere": "RPG",
        "plataforma": "PC",
        "puntuacio": 7.8,
        "desenvolupador": {"nom": "CD Projekt Red", "pais": "Polònia"},
        "dlcs": ["Phantom Liberty"],
        "preu": 29.99
    },
    {
        "titol": "FIFA 24",
        "any_llancament": 2023,
        "genere": "Esports",
        "plataforma": "PlayStation",
        "puntuacio": 8.2,
        "desenvolupador": {"nom": "EA Sports", "pais": "Estats Units"},
        "dlcs": [],
        "preu": 69.99
    }
]

biblioteca_personal = []


def buscar_per_titol(titol, videojocs):
    """
    Busca un videojoc pel títol (insensible a majúscules).
    Retorna el diccionari del joc o None si no el troba.
    """
    for joc in videojocs:
        if joc["titol"].lower() == titol.lower():
            return joc
    return None


def afegir_a_biblioteca(titol, videojocs, biblioteca):
    """
    Afegeix un joc a la biblioteca personal.
    Retorna un missatge indicant el resultat de l'operació.
    """
    joc = buscar_per_titol(titol, videojocs)
    if joc is None:
        return "❌ Joc no trobat"
    for b in biblioteca:
        if b["titol"].lower() == titol.lower():
            return "⚠️ Ja està a la biblioteca"
    biblioteca.append(joc)
    return "✅ Joc afegit!"


def joc_mes_car(videojocs):
    """
    Retorna el videojoc (diccionari) amb el preu més alt.
    Retorna None si la llista és buida.
    """
    if not videojocs:
        return None
    mes_car = videojocs[0]
    for joc in videojocs[1:]:
        if joc["preu"] > mes_car["preu"]:
            mes_car = joc
    return mes_car
