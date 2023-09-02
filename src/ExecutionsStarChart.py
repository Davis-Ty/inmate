import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

class ExecutionsStarChart:
    def __init__(self, totalB4year):
        self.totalB4year = totalB4year

    def create_chart(self, goal):
        stars_per_line = 30
        total_lines = (self.totalB4year + stars_per_line - 1) // stars_per_line

        fig = go.Figure()

        for i in range(self.totalB4year):
            fig.add_trace(go.Scatter(
                x=[i % stars_per_line],
                y=[total_lines - 1 - i // stars_per_line],
                mode='markers',
                marker=dict(
                    symbol='star',
                    size=10,
                    color='yellow',
                    line=dict(width=1)
                ),
                name=f'Executed {i + 1}'
            ))

        for i in range(goal - self.totalB4year):
            fig.add_trace(go.Scatter(
                x=[(self.totalB4year + i) % stars_per_line],
                y=[total_lines - 1 - (self.totalB4year + i) // stars_per_line],
                mode='markers',
                marker=dict(
                    symbol='star',
                    size=10,
                    color='black',
                    line=dict(width=1)
                ),
                name=f'Need {i+1} to {self.totalB4year+i+1}'
            ))

        fig.update_layout(
            title=f'[Stars: Executions] [1 Yellow Stars: 1 Executed] [1 Black star: 1 execution to {goal}]',
            xaxis_title="",
            yaxis_title="",
            showlegend=False,
            xaxis=dict(
                showline=False,
                showgrid=False,
                zeroline=False,
                showticklabels=False,
            ),
            yaxis=dict(
                showline=False,
                showgrid=False,
                zeroline=False,
                showticklabels=False,
            ),
            width=800,
            height=total_lines * 40,
        )

        return fig  # Return the Plotly figure object
