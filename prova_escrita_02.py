# DAW-M485-Bloc2-Paper-02 24-25
# Solucions dels exercicis 1, 2, 3 i 4 (s'exclouen el 5 i el 6 per la T02)


def crear_sequencia(inici, final):
    """
    Genera una llista amb tots els números de inici fins a final (ambdós inclosos).
    Valida que siguin enters positius i que inici < final.
    Retorna llista buida si la validació falla.
    """
    if not isinstance(inici, int) or not isinstance(final, int):
        return []
    if inici < 0 or final < 0:
        return []
    if inici >= final:
        return []
    return list(range(inici, final + 1))


def numeros_senars_majors(llista, limit):
    """
    Retorna una nova llista amb els números senars majors que limit.
    Valida que llista sigui una llista no buida i limit un enter.
    Retorna llista buida si la validació falla.
    """
    if not isinstance(llista, list) or len(llista) == 0:
        return []
    if not isinstance(limit, int):
        return []
    return [x for x in llista if isinstance(x, int) and x % 2 != 0 and x > limit]


def primera_posicio(llista, element):
    """
    Troba la posició de la primera aparició d'un element a la llista.
    Retorna -1 si no existeix. No utilitza el mètode .index().
    """
    for i, val in enumerate(llista):
        if val == element:
            return i
    return -1


def diagonal_principal(matriu):
    """
    Retorna una llista amb els elements de la diagonal principal d'una matriu quadrada.
    Valida que matriu sigui una llista de llistes no buida i quadrada.
    Retorna llista buida si la validació falla.
    """
    if not isinstance(matriu, list) or len(matriu) == 0:
        return []
    n = len(matriu)
    for fila in matriu:
        if not isinstance(fila, list) or len(fila) != n:
            return []
    return [matriu[i][i] for i in range(n)]
