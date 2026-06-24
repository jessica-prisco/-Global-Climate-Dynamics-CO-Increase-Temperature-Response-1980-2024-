import dash
from dash import html, dcc
import plotly.graph_objects as go

# -----------------------------
# DATI REALISTICI SEMPLIFICATI
# -----------------------------
years = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2024]
co2 = [338, 346, 354, 361, 369, 380, 390, 400, 414, 421]
temp = [0.25, 0.30, 0.35, 0.40, 0.45, 0.55, 0.65, 0.85, 1.00, 1.10]

fig = go.Figure()

fig.add_trace(
    go.Scatter3d(
        x=years,
        y=co2,
        z=temp,
        mode="markers+lines",
        marker=dict(
            size=8,
            color=temp,
            colorscale="Turbo",
            opacity=0.9,
            showscale=True
        ),
        line=dict(color="white", width=3),
        hovertemplate="Year: %{x}<br>CO₂: %{y} ppm<br>Temp: %{z} °C<extra></extra>"
    )
)

fig.update_layout(
    title="Global Climate Dynamics (1980–2024)",
    scene=dict(
        xaxis_title="Year",
        yaxis_title="CO₂ (ppm)",
        zaxis_title="Temp anomaly (°C)",
        camera=dict(eye=dict(x=1.8, y=1.8, z=0.8))
    ),
    template="plotly_dark",
    margin=dict(l=0, r=0, b=0, t=60)
)

# -----------------------------
# URL IMMAGINI
# -----------------------------
IMG1 = "https://www.repstatic.it/content/contenthub/img/2023/10/10/170646648-ff5019f5-5858-4192-b2ae-e4537b0b32f8.jpg"
IMG2 = "https://www.thegreensideofpink.com/wp-content/uploads/2024/04/Rocas-en-la-costa.jpg"
IMG3 = "https://media-assets.wired.it/photos/64afe0cc1e56c19140f55c5e/master/w_1600%2Cc_limit/unnamed%2520(2).jpg"
IMG4 = "https://www.ultimavoce.it/wp-content/uploads/2019/01/Img1-1-1024x680.jpg"
IMG5 = "https://100-facts.com/wp-content/uploads/2022/08/interesnie-fakti-ob-uraganah-e1512054098592.jpg"

# -----------------------------
# DASH APP
# -----------------------------
app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "black",
        "color": "white",
        "padding": "20px"
    },
    children=[

        html.H1("Global Climate Dynamics", style={"textAlign": "center"}),
        html.H2("CO₂ Increase and Temperature Response (1980–2024)", style={"textAlign": "center", "color": "#c7d5ff"}),

        html.Div([
            html.P(
                "Questo sito presenta una visualizzazione tridimensionale della relazione tra la concentrazione "
                "di anidride carbonica (CO₂) in atmosfera e le anomalie di temperatura globale negli ultimi decenni. "
                "La CO₂ è un gas serra a lunga permanenza, e il suo aumento modifica il bilancio radiativo terrestre."
            ),
            html.P(
                "L’aumento della CO₂ intensifica l’effetto serra: una frazione maggiore della radiazione infrarossa "
                "emessa dalla superficie terrestre viene assorbita e riemessa verso il basso, aumentando il contenuto "
                "energetico del sistema climatico. Questo si traduce in un riscaldamento globale misurabile."
            ),
            html.P(
                "Analizzare questi dati permette di comprendere la velocità del cambiamento climatico, prevedere scenari "
                "futuri e supportare decisioni politiche e tecnologiche orientate alla mitigazione delle emissioni."
            )
        ], style={"maxWidth": "900px", "margin": "0 auto"}),

        dcc.Graph(figure=fig, style={"height": "650px"}),

        html.H2("Climate impacts linked to rising CO₂", style={"textAlign": "center", "marginTop": "40px", "color": "#c7d5ff"}),

        # 1) GHIACCIAI
        html.Div([
            html.Img(src=IMG1, style={"width": "100%", "borderRadius": "8px"}),
            html.P(
                "Lo scioglimento accelerato dei ghiacciai è una delle prove più evidenti del riscaldamento globale. "
                "L’aumento della CO₂ incrementa il forcing radiativo, causando un innalzamento delle temperature "
                "anche nelle regioni polari. La perdita di massa glaciale contribuisce all’innalzamento del livello "
                "del mare e altera la disponibilità di acqua dolce per milioni di persone."
            )
        ], style={"maxWidth": "900px", "margin": "30px auto"}),

        # 2) MARE
        html.Div([
            html.Img(src=IMG2, style={"width": "100%", "borderRadius": "8px"}),
            html.P(
                "L’innalzamento del livello del mare è causato dalla dilatazione termica degli oceani e dallo scioglimento "
                "dei ghiacci. L’aumento della CO₂ riscalda l’atmosfera e gli oceani, modificando il contenuto di calore "
                "marino. Questo porta a inondazioni costiere più frequenti, erosione delle coste e salinizzazione delle "
                "falde acquifere."
            )
        ], style={"maxWidth": "900px", "margin": "30px auto"}),

        # 3) CALDO ESTREMO
        html.Div([
            html.Img(src=IMG3, style={"width": "100%", "borderRadius": "8px"}),
            html.P(
                "Le ondate di calore estreme sono eventi in cui le temperature superano di molto i valori medi. "
                "L’aumento della CO₂ sposta la distribuzione statistica delle temperature verso valori più elevati, "
                "aumentando frequenza, durata e intensità delle heatwaves. Gli impatti includono stress termico, "
                "mortalità, incendi e danni agricoli."
            )
        ], style={"maxWidth": "900px", "margin": "30px auto"}),

        # 4) ACIDIFICAZIONE
        html.Div([
            html.Img(src=IMG4, style={"width": "100%", "borderRadius": "8px"}),
            html.P(
                "Una parte della CO₂ emessa viene assorbita dagli oceani, dove forma acido carbonico. Questo processo "
                "abbassa il pH dell’acqua marina, causando acidificazione. L’acidificazione compromette la capacità "
                "degli organismi marini di costruire strutture calcaree, alterando interi ecosistemi e catene trofiche."
            )
        ], style={"maxWidth": "900px", "margin": "30px auto"}),

        # 5) EVENTI ESTREMI
        html.Div([
            html.Img(src=IMG5, style={"width": "100%", "borderRadius": "8px"}),
            html.P(
                "L’aumento della CO₂ e del contenuto energetico del sistema climatico è associato a una maggiore "
                "probabilità di eventi meteorologici estremi. Un’atmosfera più calda trattiene più vapore acqueo, "
                "alimentando sistemi convettivi più intensi. Uragani, tempeste e precipitazioni estreme diventano "
                "più frequenti e distruttivi."
            )
        ], style={"maxWidth": "900px", "margin": "30px auto"}),

        html.Hr(),

        html.Div([
            html.P("created by Jessica Prisco & AI"),
            html.P("this is a project for the develophe course, if you want work with me send an email at this adress : jessica.prisco22@gmail.com")
        ], style={"textAlign": "center"})
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
