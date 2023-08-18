import plotly_express as px
import numpy as np
import pandas as pd
from dash import Dash, dcc, Output, Input, State
from dash.html import H1, H2, Div, P, Button
from pathlib import Path

simulation_path = Path(__file__).parent / "simulations" # path will be different based on OS, dcc requires posix, this is changed in download_csv function
simulation_path.mkdir(exist_ok = True) # exist_ok -> no error if folder already exists

dropdown_options = [{"label": f"{rolls} rolls", "value": rolls} for rolls in [10, 100, 1000, 10000]]

app = Dash(__name__)

app.layout = Div([
    H1("Dice Simulator"),
    P("Choose number of dice and number of rolls"),
    dcc.Graph(id = "dice-graph"),
    Button("Save dice rolls", id = "save-button"),
    H2("Number of rolls"),
    dcc.Dropdown(id = "number-rolls", options = dropdown_options, value = 10),
    H2("Number of dices"),
    dcc.Slider(id = "number-dices", min = 1, max = 6, step = 1, value = 2),
    dcc.Store(id = "simulation-data"),
    dcc.Download(id = "download-csv")
])


@app.callback(
        Output("download-csv", "data"),
        Input("save-button", "n_clicks"), # only run when n_clicks is changed
        State("simulation-data", "data") # and the state of stored data has been changed
)
def download_csv(n_clicks, data):

    saved_filepath = (simulation_path / f"simulation{n_clicks}.csv").as_posix() # change filepath to posix (required format for dcc)

    if n_clicks:
        csv_string = pd.DataFrame(data).to_csv(index = False)

        with open(saved_filepath, "w") as file:
            file.write(csv_string) # write data to file

        return dcc.send_file(path = saved_filepath) # send file to file location


@app.callback(
        Output("simulation-data", "data"),
        Input("number-rolls", "value"),
        Input("number-dices", "value")
)
def dice_simulation(rolls, num_dices):
    dices = np.random.randint(1, 7, size = (rolls, num_dices)) # size is rolls, dices per roll as a matrix, i.e. a cols x rows matrix
    return dices


@app.callback(
    Output("dice-graph", "figure"),
    Input("simulation-data", "data")
)
def dice_simulator_histogram(dices):
    return px.histogram(np.array(dices).sum(axis = 1))


if __name__ == "__main__":
    print('Hello from the docker side')

    app.run_server(host = "0.0.0.0", debug = True, port = 8050)

