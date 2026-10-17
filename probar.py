"""Cliente de prueba: lanza el servidor por stdio y llama sus herramientas."""
import asyncio
import sys
from mcp import Client, StdioServerParameters


async def main():
    srv = StdioServerParameters(command=sys.executable, args=["servidor.py"])
    async with Client(srv) as c:
        tools = await c.list_tools()
        print("Herramientas:", [t.name for t in tools.tools])
        r = await c.call_tool("ventas_del_dia", {})
        print("ventas_del_dia ->", r.content[0].text)
        r = await c.call_tool("producto_mas_vendido", {})
        print("producto_mas_vendido ->", r.content[0].text)
        res = await c.read_resource("menu://carta")
        print("menu://carta ->\n" + res.contents[0].text)


asyncio.run(main())
