from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv(
    '../assets/CountyData.csv',
    error_bad_lines=False)
df = pd.DataFrame(csv_data)

# County table
county_columns = ['State_id', 'FIPS_County', 'Name', 'GFD_ID']
df_county = pd.DataFrame(columns=county_columns)

# County Revenue table
county_revenue_columns = ['County_id', 'Name', 'Year', 'Population', 'Total_Revenue', 'Total_Taxes', 'Tot_Sales_Gr_Rec_Tax', 'Total_License_Taxes', 'Total_Income_Taxes', 'Death_and_Gift_Tax', 'Docum_and_Stock_Tr_Tax', 'Severance_Tax', 'Taxes_NEC']
df_county_revenue = pd.DataFrame(columns=county_revenue_columns)

# Using unique counties in 2012 (last year of complete Census)
# df_2012 = df[(df['Year4'] == 2012)]
# for i, county in df_2012.iterrows():
    
#         df_county.at[i, 'GFD_ID'] = county['ID']
#         df_county.at[i, 'Name'] = county['Name']
#         df_county.at[i, 'State_id'] = int(county['FIPS_Code_State'])
#         df_county.at[i, 'FIPS_County'] = int(county['FIPS_County'])


for year in range(2016, 2006, -1):
    df_year = df[(df['Year4'] == year)]
    for i, county in df_year.iterrows():
        if not len(df_county[(df_county['GFD_ID'] == county['ID'])]):
            df_to_append = pd.DataFrame(columns=county_columns)
            df_to_append.at[i, 'GFD_ID'] = county['ID']
            df_to_append.at[i, 'Name'] = county['Name']
            df_to_append.at[i, 'State_id'] = int(county['FIPS_Code_State'])
            df_to_append.at[i, 'FIPS_County'] = int(county['FIPS_County'])
            df_county = df_county.append(df_to_append, ignore_index=True)

    for i, df_current in df_year.iterrows():
        df_to_append = pd.DataFrame(columns=county_revenue_columns)
        df_to_append.at[i, 'County_id'] = df_current['ID']
        df_to_append.at[i, 'Name'] = df_current['Name']
        df_to_append.at[i, 'Year'] = df_current['Year4']
        df_to_append.at[i, 'Population'] = df_current['Population']
        df_to_append.at[i, 'Total_Revenue'] = df_current['Total_Revenue']
        df_to_append.at[i, 'Total_Taxes'] = df_current['Total_Taxes']
        df_to_append.at[i, 'Tot_Sales_Gr_Rec_Tax'] = df_current['Tot_Sales___Gr_Rec_Tax']
        df_to_append.at[i, 'Total_License_Taxes'] = df_current['Total_License_Taxes']
        df_to_append.at[i, 'Total_Income_Taxes'] = df_current['Total_Income_Taxes']
        df_to_append.at[i, 'Death_and_Gift_Tax'] = df_current['Death_and_Gift_Tax']
        df_to_append.at[i, 'Docum_and_Stock_Tr_Tax'] = df_current['Docum_and_Stock_Tr_Tax']
        df_to_append.at[i, 'Severance_Tax'] = df_current['Severance_Tax']
        df_to_append.at[i, 'Taxes_NEC'] = df_current['Taxes_NEC']
        df_county_revenue = df_county_revenue.append(df_to_append, ignore_index=True)


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
df_county.to_sql('api_county', engine, if_exists='append', index=False)


df_county_revenue.to_sql('api_countyrevenue', engine, if_exists='append', index=False)
# Do we need to stop the engine after this point?
