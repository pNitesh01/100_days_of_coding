import pandas as pd

df = pd.read_csv('squirrel_data.csv')
gray_squirrels_count = len(df[df['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(df[df['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(df[df['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data = pd.DataFrame(data_dict)
data.to_csv('squirrel_count.csv')