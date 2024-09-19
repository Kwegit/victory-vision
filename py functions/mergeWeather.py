import pandas as pd
import os

path = '../Datas'

le_merge = pd.read_csv(os.path.join(path, 'merge.csv'))
le_weather = pd.read_csv(os.path.join(path, 'weather.csv'))

le_weather['year'] = le_weather['year'].astype(int)
le_weather['Rainfall'] = le_weather['Rainfall'].astype(int)

le_weather_columns = le_weather[['races_name','year','AirTemp','Humidity','Pressure','Rainfall','TrackTemp','WindDirection','WindSpeed']]

le_le_merge_avg = le_weather_columns.groupby(['races_name', 'year']).mean()

le_le_merge = pd.merge( le_merge, le_le_merge_avg, on=['races_name','year'])

le_le_merge.to_csv(os.path.join(path, 'le_vrai_merge.csv'), index=True)

print('finito pipo')

