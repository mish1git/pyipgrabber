import asyncio
import aiohttp


from aiohttp import web

async def hello(request):
    import urllib.request
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    exipstring = str(external_ip)
    print(external_ip)
    file = open('ipaddress.txt', 'w')
    file.write(exipstring + '\n')
    file.close()
    return web.Response(text="Loading",
                        content_type='text/html')

app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app) 
