import pandas as pd
import plotly.express as px

class CountyExecutionsChart:
    def __init__(self, county_race_counts):
        self.county_race_counts = county_race_counts

    def create_chart(self):
        counties = []
        total_executions = []

        for county, race_count in self.county_race_counts.items():
            counties.append(county)
            total_executions.append(sum(race_count.values()))

        county_executions_df = pd.DataFrame({
            "County": counties,
            "Total Executions": total_executions
        })

        fig = px.bar(county_executions_df, x="County", y="Total Executions", title="Total Number of Executions by County")
        fig.update_xaxes(type='category')
        return fig  # Return the Plotly figure object