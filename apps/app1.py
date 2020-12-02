import dash_core_components as dcc
import dash_html_components as html
from dash import dash
from dash.dependencies import Input, Output, State
from datetime import datetime

from app import app

def layout():
	return html.Div(children=[
		html.H3('App 1'),
		'This is app 1.',
		html.Br(),
		
		html.Div('Some example content: clicking the button updates the # of times it was clicked'),
		html.Br(),
		
		html.Div(children=[
			html.Button(id='app1-button', className='app-button', children='Click me!', n_clicks=0),
			html.Br(),
			html.Br(),
			html.Span('The button was clicked: '),
			html.Span(id='app1-output', children=None),
			html.Br(),
			html.Br(),
		])
	])



# Modifies the 'children' property of the element with ID 'app1-output'
# The 'children' property is whatever is stored within a HTML tag: <div>children go here</div>
# Children can be a list of elements or a single element
#
@app.callback(
	Output('app1-output', 'children'),
	[Input('app1-button', 'n_clicks')])

def update_click_count(n_clicks):
	x = ' times.'
	if(n_clicks == 0):
		html.Br(),
		msg = 'The button has never been clicked'
	else:
		html.Br(),
		msg = 'The button was last clicked on: ' + str(datetime.now())
	return n_clicks, x, html.Div(msg)

# 3) Added code within the click counter that updates a message every time the button clicks with current date/time information. It even tells you if the button has never been clicked.



