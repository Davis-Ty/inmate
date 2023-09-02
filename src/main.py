from CountyExecutionsChart import *

from DataScraper import *
from RaceByCountyChart import *
from ExecutionDataProcessor import *
from ExecutionsStarChart import *
from YearlyExecutionsChart import *

import plotly.express as px

if __name__ == "__main__":
    URL = "https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html"
    
    # Data scraping
    scraper = DataScraper(URL)
    rows = scraper.scrape_data()

    # Data processing
    data_processor = ExecutionDataProcessor(rows)
    year_counts = data_processor.process_yearly_executions()
    county_race_counts = data_processor.process_county_race_executions()
    totalB4year = data_processor.process_total_executions_before_year(2024)

     # Chart creation and display
    yearly_executions_chart = YearlyExecutionsChart(year_counts)
    yearly_executions_chart.create_chart().write_html("yearly_executions_chart.html")

    county_executions_chart = CountyExecutionsChart(county_race_counts)
    county_executions_chart.create_chart().write_html("county_executions_chart.html")

    race_by_county_chart = RaceByCountyChart(county_race_counts)
    race_by_county_chart.create_chart().write_html("race_by_county_chart.html")

    executions_star_chart = ExecutionsStarChart(totalB4year)
    executions_star_chart.create_chart(600).write_html("executions_star_chart.html")