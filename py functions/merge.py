import pandas as pd
import os

path = '../Datas'

le_results = pd.read_csv(os.path.join(path, 'results.csv'))
le_drivers = pd.read_csv(os.path.join(path, 'drivers.csv'))
le_constructors = pd.read_csv(os.path.join(path, 'constructors.csv'))
le_races = pd.read_csv(os.path.join(path, 'races.csv'))
le_status = pd.read_csv(os.path.join(path, 'status.csv'))

le_drivers_columns = le_drivers[['driverId','forename','surname']]
le_constructors_columns = le_constructors[['constructorId','constructor_name']]
le_races_columns = le_races[['raceId','year','round','circuitId','races_name','date']]
le_status_columns = le_status[['statusId', 'status']]

le_merge = pd.merge(le_results, le_drivers_columns, on='driverId')
le_merge = pd.merge(le_merge, le_constructors_columns, on='constructorId')
le_merge = pd.merge(le_merge, le_races_columns, on='raceId')
le_merge = pd.merge(le_merge, le_status, on='statusId')


le_cols = le_merge.columns.tolist()

print(le_cols)

le_driver_id_index = le_cols.index('driverId')
le_cols.insert(le_driver_id_index + 1, le_cols.pop(le_cols.index('forename')))
le_cols.insert(le_driver_id_index + 2, le_cols.pop(le_cols.index('surname')))

le_constructors_id_index = le_cols.index('constructorId')
le_cols.insert(le_constructors_id_index + 1, le_cols.pop(le_cols.index('constructor_name')))

le_races_id_index = le_cols.index('raceId')
le_cols.insert(le_races_id_index + 1, le_cols.pop(le_cols.index('year')))
le_cols.insert(le_races_id_index + 2, le_cols.pop(le_cols.index('round')))
le_cols.insert(le_races_id_index + 3, le_cols.pop(le_cols.index('circuitId')))
le_cols.insert(le_races_id_index + 4, le_cols.pop(le_cols.index('races_name')))
le_cols.insert(le_races_id_index + 5, le_cols.pop(le_cols.index('date')))

le_status_id_index = le_cols.index('statusId')
le_cols.insert(le_status_id_index + 1, le_cols.pop(le_cols.index('status')))

le_le_merge_la = le_merge[le_cols]

le_le_merge_la['date'] = pd.to_datetime(le_le_merge_la['date'])

le_filtre = le_le_merge_la[(le_le_merge_la['date'].dt.year >= 2018) & (le_le_merge_la['date'].dt.year <= 2024)]

le_filtre.to_csv(os.path.join(path, 'merge.csv'), index=False)

print('finito pipo')