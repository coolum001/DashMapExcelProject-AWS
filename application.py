from dash import Dash
from callbacks.callbacks import callbacks
from layout.layout import layout
from utils.functions import set_dfs
import dash_bootstrap_components as dbc

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

# Update data before launching the dashboard.
set_dfs()

app = Dash(
    __name__,
    title="Water monitoring",
    update_title=None,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
)

server = app.server
# object application for AWS Ellastic BeanStalk
application = app.server

callbacks(app)
app.layout = layout

if __name__ == "__main__":
    application.run(port=8080, debug=True)
