from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import webbrowser

# Open the default web browser
webbrowser.open('http://127.0.0.1:5000/')
app = Flask(__name__)

@app.route('/')
def home():
    # Load dataset
    data = pd.read_csv('data/DiabetesByFarrakh.csv')

    # Create a heatmap
    fig_heatmap = px.imshow(data.corr(), labels=dict(color='Correlation'), x=data.columns, y=data.columns, color_continuous_scale='Viridis')

    # Create other visualizations (you can customize these based on your needs)
    fig_scatter = px.scatter(data, x='Age', y='Glucose', color='Outcome', title='Scatter Plot')

    # Save the plots to HTML
    plot_heatmap = fig_heatmap.to_html(full_html=False)
    plot_scatter = fig_scatter.to_html(full_html=False)

    return render_template('index.html', plot_heatmap=plot_heatmap, plot_scatter=plot_scatter)

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
    # Open the default web browser
    webbrowser.open('http://127.0.0.1:5000/')