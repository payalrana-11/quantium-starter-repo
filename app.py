from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("output.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)


app.layout = html.Div([
    html.H1(  "Pink Morsel Sales Dashboard" ,id="dashboard-header"),

    dcc.RadioItems(
    id="region-filter",
    options=[
      {"label": "All", "value": "all"},
      {"label": "North", "value": "north"},
      {"label": "South", "value": "south"},
      {"label": "East", "value": "east"},
      {"label": "West", "value": "west"},
     ],
     value="all"
     ),
    dcc.Graph( id="sales-graph",figure=fig) 
 ])

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df

    else:
        filtered_df = df[df["Region"] == selected_region]

    filtered_df = filtered_df.groupby("Date")["Sales"].sum().reset_index()

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        color_discrete_sequence=["#00e5ff"]  
    )

    fig.update_layout (
        {
        "paper_bgcolor": "#0b0f14",
        "plot_bgcolor": "#0b0f14",
        "font": {"color": "#00e5ff"},
        "xaxis": {"gridcolor": "#0b0f14", "color": "#00e5ff"},
        "yaxis": {"gridcolor": "#0b0f14", "color": "#00e5ff"},
       },
         xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)