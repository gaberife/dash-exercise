import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime

from app import app

#Pre-Start I had to create a file called __init__.py in order to import app1 & app2
from apps import app1, app2

# Overall app layout. The visible content is rendered based on the URL
#
app.layout = html.Div(children=[
	dcc.Location(id='url', refresh=False),

	html.Div(id='app-body', className='app-body', children=[])
])

# Layout for the index page
def layout():
	return html.Div(children=[
		dcc.Location(id='url', refresh=True),
		html.H3('Welcome to the Index page'),
		html.Label([html.A('First Application', href='/app1')]),
		html.Br(),
		html.Br(),
		html.Label([html.A('Second Application', href='/app2')]),
		html.Br(),
		html.Br(),
		html.Div(id='page-content'),
	])

# This is used for navigation between index, app1, and app2.
@app.callback(
	Output('app-body', 'children'),
	[ Input('url', 'pathname') ])
def display_page(pathname):
	if pathname == '/': #index page
		return layout()
	elif pathname == '/app1':
		return app1.layout()
	elif pathname == '/app2':
		return app2.layout()
	else:
		return html.H2('404 Page not found')
# Starts the server when running index.py
#
if __name__ == '__main__':
	print('\nStarting server at: {}'.format(datetime.today()))
	print()
	app.run_server(port=8000, debug=True)
