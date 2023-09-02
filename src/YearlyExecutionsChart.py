import pandas as pd
import plotly.express as px

class YearlyExecutionsChart:
    def __init__(self, year_counts):
        self.year_counts = year_counts

    def create_chart(self):
        year_counts_df = pd.DataFrame(list(self.year_counts.items()), columns=["Year", "Executions"])
        fig = px.bar(year_counts_df, x="Year", y="Executions", title="Executions by Year")
        fig.update_xaxes(type='category')
        return fig  # Return the Plotly figure object

