import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
MAPBOX_KEY = 'xxxxx'

app.layout = html.Div(
    [
        html.Div([

                                # Plot properties map
                                dcc.Loading(
                                    id = "map-loading",
                                    type = "default",
                                    className = "map-loading",
                                    fullscreen=False,
                                    children=dcc.Graph(id="map-d"),
                                ),

                            ], className="map-style"),
      
      
        dbc.Button("Show P", id="show-p-btn", className="me-1", n_clicks=0),
    ]
)

@app.callback(
    Output("map-d", "figure"),
    Input("show-p-btn", "n_clicks")
)
def a1(n_clicks_val):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    ctx = dash.callback_context

    print(ctx.triggered, current_time)
    
    data = []

    if n_clicks_val > 0:
      
        data.append({

                        "type": "scattermapbox",
                        "lat": coords[0],
                        "lon": coords[1],
                        "name": "Location",
                        "hovertext": "",
                        "showlegend": False,
                        "hoverinfo": "text",
                        "mode": "markers",
                        "clickmode": "event+select",
                        "marker": {
                            "symbol": "circle",
                            "size": 9,
                            "opacity": 0.8
                        }
                    }
        )
        
        layout = {

                 "autosize": True,
                 "hovermode": "closest",
                 "mapbox": {

                     "accesstoken": MAPBOX_KEY,
                     "bearing": 0,
                     "center": {
                         "lat": coords[0],
                         "lon": coords[1]
                     },
                     "pitch": 0,
                     "zoom": zoom,
                     "style": "streets",

                 },

                 "margin": {
                    "r": 0,
                    "t": 0,
                    "l": 0,
                    "b": 0,
                    "pad": 0
                }

    }
    
    return ({"data": datad, "layout": layout})
  
  else:
    
    return (dash.no_update, dash.no_update)

if __name__ == '__main__':
    app.run_server(debug=True)


