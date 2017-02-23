""" this is a quick flask implementation to do some playing with HTTP verbs, see README.md for more info """

from flask import Flask, request
app = Flask(__name__)

KEYSTRING = "<!-- TEMPLATE -->"
TEMPLATE = """<html>
        <head>
        <title>HTTP Playtime</title>
        </head>
        <body>
        <center>
        <h1>HTTP Playground</h1>
        <p><a href='/'>Clear variables</a></p>
        <h3>POST Form</h3>
        <form method='POST' action='/'>
                <input type='textdata' name='text' /><br />
                <input type='submit' name='submit' />
                </form>
        
        <h3>GET Form</h3>
        <form method='GET' action='/'>
                <input type='textdata' name='text' /><br />
                <input type='submit' name='submit' />
                </form>
        
        <p>
                <a href='/?textdata=hello&submit=getlink'>GET Link</a>
                </p>
        <p>
        <!-- TEMPLATE -->
        </p>
        </body>
        </html>"""

@app.route('/', methods=['POST', 'GET'])
def index():
    """ the only function you need - exposes the homepage """
    if request.method in ('POST', 'GET') and request.values.get('submit', False):
        retval = """Request method: {}<br />
                Data:<br />
                <table border='1'>
                <tr><th>Variable</th><th>Value</th></tr>""".format(request.method)
        for key in sorted(request.values):
            retval += "<tr><td>{}</td><td>{}</td></tr>".format(key, request.values[key])
        retval += "</table>"
        return TEMPLATE.replace(KEYSTRING, retval)
    return TEMPLATE
