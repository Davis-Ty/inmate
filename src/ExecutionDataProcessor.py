from datetime import datetime


class ExecutionDataProcessor:
    def __init__(self, rows):
        self.rows = rows

    def process_yearly_executions(self):
        year_counts = {}
        for e in range(1, len(self.rows)):
            date_string = self.rows[e].find_all("td")[7].get_text()
            date = datetime.strptime(date_string, "%m/%d/%Y")
            year = date.year
            if year in year_counts:
                year_counts[year] += 1
            else:
                year_counts[year] = 1
        return year_counts

    def process_county_race_executions(self):
        county_race_counts = {}
        processed_counties = set()
        for e in range(1, len(self.rows)):
            county = self.rows[e].find_all("td")[9].get_text()
            if county in processed_counties:
                continue
            race = self.rows[e].find_all("td")[8].get_text()
            if county not in county_race_counts:
                county_race_counts[county] = {
                    "Black": 0,
                    "White": 0,
                    "Hispanic": 0,
                    "Asian": 0,
                    "Other": 0
                }
            if race == "Black":
                county_race_counts[county]["Black"] += 1
            elif race == "White":
                county_race_counts[county]["White"] += 1
            elif race == "Hispanic":
                county_race_counts[county]["Hispanic"] += 1
            elif race == "Asian":
                county_race_counts[county]["Asian"] += 1
            else:
                county_race_counts[county]["Other"] += 1
        return county_race_counts

    def process_total_executions_before_year(self, the_year):
        year_counts = self.process_yearly_executions()
        totalB4year = 0
        for year, count in year_counts.items():
            if year < the_year:
                totalB4year += count
        return totalB4year
