import pandas as pd
import plotly.express as px

class RaceByCountyChart:
    def __init__(self, county_race_counts):
        self.county_race_counts = county_race_counts

    def create_chart(self):
        counties = list(self.county_race_counts.keys())
        races = ["Black", "White", "Hispanic", "Asian", "Other"]

        data = []

        for county in counties:
            for race in races:
                data.append({
                    "County": county,
                    "Race": race,
                    "Executions": self.county_race_counts[county][race]
                })

        df = pd.DataFrame(data)
        
        # Define custom color mappings for each race
        color_discrete_map = {
            "Black": "black",
            "White": "red",
            "Hispanic": "green",  # You can choose any color you like
            "Asian": "yellow",
            "Other": "purple"
        }

        fig = px.scatter(
            df, 
            x="County", 
            y="Race", 
            size="Executions", 
            title="Executions by County and Race", 
            color="Race",
            color_discrete_map=color_discrete_map
        )
        
        return fig  # Return the Plotly figure object with custom colors for each race