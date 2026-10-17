# mcp-restaurante

Servidor MCP de ejemplo del tutorial **"MCP desde cero: cómo funciona y crea tu propio servidor (actualizado 2026)"** — Diego Calderón · Arquitecto de Software.

Un servidor de solo lectura para un restaurante con:

| Tipo | Nombre | Qué hace |
|---|---|---|
| Tool | `ventas_del_dia` | Total vendido hoy y unidades por producto |
| Tool | `producto_mas_vendido` | El producto con más unidades hoy |
| Resource | `menu://carta` | La carta con precios |
| Prompt | `informe_del_dia` | Plantilla para el informe de cierre |

Probado con el SDK oficial de Python `mcp` 2.2 y 2.3 (especificación MCP 2026-07-28).

## Requisitos
- Python 3.10 o superior

## Instalación
```bash
pip install "mcp[cli]"
```

> El SDK v2 usa `from mcp.server import MCPServer`. Si ves tutoriales con `FastMCP`, son de la versión anterior.

## Probar
```bash
# Cliente de prueba por consola
python probar.py

# MCP Inspector (se abre en el navegador)
mcp dev servidor.py
```

## Conectar con Claude Desktop
Opción rápida:
```bash
mcp install servidor.py
```
Opción manual: en `claude_desktop_config.json` agrega:
```json
{
  "mcpServers": {
    "mi-restaurante": {
      "command": "python",
      "args": ["/ruta/a/servidor.py"]
    }
  }
}
```
Reinicia Claude Desktop y pregunta: *"¿Cuánto vendimos hoy en el restaurante?"*

## Antes de producción
1. **Solo lectura** si no necesitas escribir.
2. **Aislamiento**: cada usuario ve solo sus datos.
3. **Los datos no son instrucciones**: el texto que escriben los usuarios nunca se obedece.
4. **Autenticación** (OAuth) para servidores remotos por Streamable HTTP.
