from datetime import datetime

#Poner formatos de numeros y porcentajes en español, miles con punto y decimales con coma
def formato_es(valor, decimales=2):
    try:
        texto = f"{float(valor):,.{decimales}f}"
        return texto.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
    except (ValueError, TypeError):
        return valor
    

def fecha_es(valor, con_hora=False):
    """Convierte una fecha a formato DD/MM/AAAA (estilo español)."""
    if valor is None:
        return ""
    
    # Si llega como texto (ej. '2026-03-19'), la convertimos primero
    if isinstance(valor, str):
        try:
            valor = datetime.strptime(valor, "%Y-%m-%d")
        except ValueError:
            return valor  # si no se puede parsear, lo devolvemos tal cual
    
    if con_hora:
        return valor.strftime("%d/%m/%Y %H:%M")
    return valor.strftime("%d/%m/%Y")