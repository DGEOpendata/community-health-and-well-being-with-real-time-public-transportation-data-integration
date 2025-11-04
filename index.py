python
import pandas as pd

def load_health_data(file_path):
    return pd.read_csv(file_path)


def load_transportation_data(file_path):
    return pd.read_csv(file_path)


def integrate_datasets(health_df, transport_df):
    # Example integration logic
    integrated_df = pd.merge(health_df, transport_df, on='region_id', how='inner')
    return integrated_df


def analyze_integrated_data(integrated_df):
    # Perform some basic analysis
    summary = integrated_df.groupby('region_id').agg({'life_expectancy': 'mean', 'daily_ridership': 'sum'})
    return summary


# File paths
health_data_path = 'Community_Health_Indicators_2023.csv'
transportation_data_path = 'Public_Transport_Usage_Statistics_2023.csv'

# Load datasets
health_data = load_health_data(health_data_path)
transportation_data = load_transportation_data(transportation_data_path)

# Integrate datasets
integrated_data = integrate_datasets(health_data, transportation_data)

# Analyze integrated data
analysis_result = analyze_integrated_data(integrated_data)

# Display the result
print(analysis_result)
