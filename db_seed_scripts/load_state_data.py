from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv(
    '../assets/StateData.csv',
    error_bad_lines=False)
df = pd.DataFrame(csv_data)

# State table
state_columns = ['FIPS_Code_State', 'Name']
df_state = pd.DataFrame(columns=state_columns)

# State Revenue table
state_revenue_columns = ['State_id', 'Name', 'Year', 'Population', 'Total_Revenue', 'Total_Taxes', 'Tot_Sales_Gr_Rec_Tax', 'Total_License_Taxes', 'Total_Income_Taxes', 'Death_and_Gift_Tax', 'Docum_and_Stock_Tr_Tax', 'Severance_Tax', 'Taxes_NEC']
df_state_revenue = pd.DataFrame(columns=state_revenue_columns)

# Using first instances of each state to populate table (Assuming states maintain the same names and FIPS Codes through the time series)
for i in range(51):
    current = df.iloc[i]
    df_state.at[i, 'Name'] = current['Name']
    df_state.at[i, 'FIPS_Code_State'] = int(current['FIPS_Code_State'])


for year in range(2016, 2006, -1):
    for state in df_state['Name'].unique():
        df_current = df[(df['Year4'] == year) & (df['Name'] == state)]
        df_to_append = pd.DataFrame(columns=state_revenue_columns)
        df_to_append['State_id'] = df_current['FIPS_Code_State'].fillna(0)
        df_to_append['Name'] = df_current['Name'].fillna(0)
        df_to_append['Year'] = df_current['Year4'].fillna(0)
        df_to_append['Population'] = df_current['Population'].fillna(0)
        df_to_append['Total_Revenue'] = df_current['Total_Revenue'].fillna(0)
        df_to_append['Total_Taxes'] = df_current['Total_Taxes'].fillna(0)
        df_to_append['Tot_Sales_Gr_Rec_Tax'] = df_current['Tot_Sales___Gr_Rec_Tax'].fillna(0)
        df_to_append['Total_License_Taxes'] = df_current['Total_License_Taxes'].fillna(0)
        df_to_append['Total_Income_Taxes'] = df_current['Total_Income_Taxes'].fillna(0)
        df_to_append['Death_and_Gift_Tax'] = df_current['Death_and_Gift_Tax'].fillna(0)
        df_to_append['Docum_and_Stock_Tr_Tax'] = df_current['Docum_and_Stock_Tr_Tax'].fillna(0)
        df_to_append['Severance_Tax'] = df_current['Severance_Tax'].fillna(0)
        df_to_append['Taxes_NEC'] = df_current['Taxes_NEC'].fillna(0)
        df_state_revenue = df_state_revenue.append(df_to_append, ignore_index=True)


db_protocol = 'postgresql'
db_host = os.environ.get('DB_HOST', '')
db_user = os.environ.get('DB_USER', '')
db_password = os.environ.get('DB_PASSWORD', '')
db_name = os.environ.get('DB_NAME', '')


print('Prior to create_engine')
engine = create_engine('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_password, db_host, db_name
))

print('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_password, db_host, db_name
))


print('Prior to df.to_sql')
# import pdb; pdb.set_trace()
# Would like to use "if_exists='replace'", but it appears that pandas doesn't use drop/cascade which raises an error.
# Switching to if_exists='append'
df_state.to_sql('api_state', engine, if_exists='append', index=False)


df_state_revenue.to_sql('api_staterevenue', engine, if_exists='append', index=False)
# Do we need to stop the engine after this point?
