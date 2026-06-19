from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("output.csv")
df["Date"] = pd.to_datetime(df["Date"])

df = df.groupby("Date")["Sales"].sum().reset_index()
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
     html.H1("Pink Morsel Sales Dashboard",style ={'text-align' : 'center'}),
      dcc.Graph(figure=fig) 
 ])

if __name__ == "__main__":
    app.run(debug=True)