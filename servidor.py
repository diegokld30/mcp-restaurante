"""Servidor MCP de ejemplo: Mi Restaurante (solo lectura)."""
from mcp.server import MCPServer

mcp = MCPServer(
    "mi-restaurante",
    instructions="Consulta ventas y menú de Mi Restaurante. Solo lectura.",
)

# Datos de ejemplo (en producción vendrían de tu base de datos)
MENU = {
    "Bandeja paisa": 32000,
    "Ajiaco": 28000,
    "Limonada de coco": 9000,
}
VENTAS_HOY = [
    {"producto": "Bandeja paisa", "cantidad": 14},
    {"producto": "Ajiaco", "cantidad": 9},
    {"producto": "Limonada de coco", "cantidad": 21},
]


@mcp.tool()
def ventas_del_dia() -> dict:
    """Devuelve el total vendido hoy y las unidades por producto."""
    total = sum(MENU[v["producto"]] * v["cantidad"] for v in VENTAS_HOY)
    return {"total_cop": total, "detalle": VENTAS_HOY}


@mcp.tool()
def producto_mas_vendido() -> str:
    """Dice cuál es el producto con más unidades vendidas hoy."""
    top = max(VENTAS_HOY, key=lambda v: v["cantidad"])
    return f"{top['producto']} ({top['cantidad']} unidades)"


@mcp.resource("menu://carta")
def carta() -> str:
    """La carta del restaurante con precios."""
    return "\n".join(f"{p}: ${precio:,}" for p, precio in MENU.items())


@mcp.prompt()
def informe_del_dia() -> str:
    """Plantilla para pedir un informe de cierre del día."""
    return "Usa ventas_del_dia y dame un informe corto del cierre de hoy, con una recomendación."


if __name__ == "__main__":
    mcp.run()  # stdio por defecto
