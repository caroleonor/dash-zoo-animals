import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Pick variables
tabtitle='zoo'
myheading = 'Pavilions in the Expo'
myfavoritecolor='#DBB312' # More colors are here: https://htmlcolorcodes.com/
x_list=['Tech', 'Art', 'History','expo']
y_list=[7, 11, 18,26]
mytitle='??'
githublink='https://github.com/caroleonor/dash-zoo-animals/edit/master/app.py'

########### Set up the chart
mydata = [go.Bar(x=x_list,
                y=y_list,
                marker=dict(color=myfavoritecolor))]
mylayout = go.Layout(
    title = mytitle,
    xaxis = dict(title = 'Labels go here!'),
    yaxis = dict(title = 'Numbers go here!'))
myfigure = go.Figure(data=mydata, layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Display the chart
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(id='figure-1', figure=myfigure),
    html.A('Code on Github', href=githublink)])

########### Execute your code
if __name__ == '__main__':
    app.run_server()
