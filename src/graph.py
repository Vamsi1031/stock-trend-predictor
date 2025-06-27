import plotly.graph_objs as go

def custom_3d_style_chart(data, title="Stock Forecast (3D Style)"):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=data[-50:],  # Display last 50 points
        x=list(range(len(data[-50:]))),
        mode="lines+markers",
        name="Predicted",
        line=dict(color="cyan", width=4),
        marker=dict(size=5, color="white", line=dict(width=1, color="cyan")),
    ))

    fig.update_layout(
        title=title,
        title_font_size=22,
        plot_bgcolor="#0E1117",
        paper_bgcolor="#0E1117",
        font=dict(color="white"),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="gray"),
        height=500,
        margin=dict(t=60, b=40, l=30, r=30),
    )

    return fig
