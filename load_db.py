from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv(
    './assets/CountyData.csv',
    error_bad_lines=False)
df = pd.DataFrame(csv_data)

# Adjust NaN values in each column, and generally clean data set
# df['ID'] = df['ID'].fillna(0)
# df['SurveyYr'] = df['SurveyYr'].fillna(0)
# df['Name'] = df['Name'].fillna('unknown')
# df['Population'] = df['Population'].fillna(0)

new_df = df[['SurveyYr', 'Name', 'Population']].copy()

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
new_df.to_sql('truthtree_api_countydata', engine, if_exists='replace', index=False)

# conn = ctds.connect(db_host, user=db_user, password=db_password, database=db_name)
# conn.bulk_insert('table', (df.to_records(index=False).tolist()))
