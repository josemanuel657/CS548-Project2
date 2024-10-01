import pandas as pd
import numpy as np

import plotly.express as px
import seaborn as sns

from matplotlib import pyplot as plt
from idlelib.pyparse import trans
from scipy import stats


# Importing all CSV Files
appearances = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/appearances.csv')
club_games = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/club_games.csv')
clubs = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/clubs.csv')
#competitions = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/competitions.csv')
#game_events = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/game_events.csv')
#game_lineups = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/game_lineups.csv')
games = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/games.csv')
players = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/players.csv')
player_valuations = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/player_valuations.csv')
transfers = pd.read_csv('/ProgramData/Microsoft/Windows/Start Menu/Programs/Git/CS548-Project2/data/transfers.csv')


"""
#Merging all files into 1 file.
Final = pd.merge(appearances, players, on='player_id', how='inner',suffixes=('', '_player'))
Final = Final.loc[:, ~Final.columns.str.endswith('_player')]
Final = pd.merge(Final, games, on='game_id', how='inner',suffixes=('', '_games'))
Final = Final.loc[:, ~Final.columns.str.endswith('_games')]
Final = pd.merge(Final, clubs, left_on='player_club_id', right_on='club_id', how='inner',suffixes=('', '_clubs'))
Final = Final.loc[:, ~Final.columns.str.endswith('_clubs')]
#Final = pd.merge(Final, competitions, on='competition_id', how='inner',suffixes=('', '_competitions'))
#Final = Final.loc[:, ~Final.columns.str.endswith('_competitions')]
#Final = pd.merge(Final, game_events, on='game_id', how='left',suffixes=('', '_gamevent'))
#Final = Final.loc[:, ~Final.columns.str.endswith('_gamevent')]
#Final = pd.merge(Final, game_lineups, on=['game_id', 'player_id'], how='left',suffixes=('', '_gamelineup'))
#Final = Final.loc[:, ~Final.columns.str.endswith('_gamelineup')]
Final = pd.merge(Final, player_valuations, on='player_id', how='left',suffixes=('', '_valuations'))
Final = Final.loc[:, ~Final.columns.str.endswith('_valuations')]
Final = pd.merge(Final, club_games, on=['game_id', 'club_id'], how='left',suffixes=('', '_clubgame'))
Final = Final.loc[:, ~Final.columns.str.endswith('_clubgame')]
Final = pd.merge(Final, transfers, on='player_id', how='left',suffixes=('', '_transfer'))
Final = Final.loc[:, ~Final.columns.str.endswith('_transfer')]
#print(Final.shape)

# Finding columns with NULL values
null_columns = Final.columns[Final.isnull().all()]
print(null_columns)
#2 columns found with NULL values, so dropping those columns
Final = Final.dropna(axis=1, how='all')
print(Final.columns)
"""



# 1. Top 20 Players by Goals

df_appearances_new = appearances.groupby(["player_name"])[["goals", "assists", "minutes_played"]].agg(["sum"])
df_appearances_new.reset_index(inplace=True)
df_appearances_new.columns = ["player_name", "total_goals", "total_assists", "total_minutes_played"]

df_goals = df_appearances_new.sort_values(by="total_goals", ascending=False).head(20)

df_goals['Total_Goals'] = df_goals['total_goals'].astype(str)

most_20_goals = px.bar(df_goals,
                       x='player_name',
                       y='total_goals',
                       title='Top 20 Players by Total Goals',
                       text="Total_Goals",
                       color='player_name')
most_20_goals.update_traces(textposition='outside')
most_20_goals.show()


# 2. Top 20 Players by Assists

df_assists = df_appearances_new.sort_values(by="total_assists", ascending=False).head(20)
df_assists['Total_Assists'] = df_assists['total_assists'].astype(str)
df_assists = df_assists.sort_values(by="total_assists", ascending=True)
most_20_assists_pie = px.pie(df_assists,
                             names='player_name',
                             values='total_assists',
                             title='Top 20 Players by Total Assists',
                             hole=0.3,
                             labels={'total_assists': 'Total Assists'})
most_20_assists_pie.update_traces(textposition='inside', textinfo='percent+label')
most_20_assists_pie.show()


# 3. Top 20 Players by Red Cards

aggresion_red = appearances.groupby(["player_name"])[["yellow_cards", "red_cards", "minutes_played"]].agg(["sum"])
aggresion_red.reset_index(inplace=True)
aggresion_red.columns = ["player_name", "yellow_cards", "red_cards", "total_minutes_played"]
df_red_cards = aggresion_red.sort_values(by="red_cards", ascending=False).head(20)

df_red_cards = df_red_cards.sort_values(by="red_cards", ascending=True)
most_20_red_cards = px.bar(df_red_cards,
                           x='red_cards',
                           y='player_name',
                           orientation='h',
                           title='Top 20 Players by Red Cards',
                           text="red_cards",
                           color_discrete_sequence=['crimson'])
most_20_red_cards.update_traces(textposition='outside')
most_20_red_cards.show()

# 4. Top 20 Players by Yellow Cards

df_red_cards = df_red_cards.sort_values(by="yellow_cards", ascending=False)
most_20_yellow_cards = px.bar(df_red_cards,
                              x='player_name',
                              y='yellow_cards',
                              title='Top 20 Players by Yellow Cards',
                              text="yellow_cards",
                              color_discrete_sequence=['gold'])
most_20_yellow_cards.update_traces(textposition='outside')
most_20_yellow_cards.show()

# 5. Players Analysis by Main Foot

players = players.sort_values("foot", ascending=False)
f = plt.figure(figsize=(10, 6))
ax = sns.countplot(x='foot', data=players, palette='Blues')

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=12)

plt.title("Main Foot Used Among All Players", fontsize=18)
plt.xlabel('Dominant Foot', fontsize=14)
plt.ylabel('Number of Players', fontsize=14)
plt.grid(False)

plt.show()


# 6. Players valuation over time

player_valuations['date']=pd.to_datetime(player_valuations['date'], format="%Y-%m-%d")
player_valuations['year']=player_valuations['date'].dt.year

player_valuations_new = player_valuations[(player_valuations.year > 2004 ) & (player_valuations.year < 2023 )]
high_value_player_valuations_new = player_valuations_new[(player_valuations_new.market_value_in_eur > 40000000 )]
positions = players.position.unique()

plt.figure(figsize=(10,6))
plt.scatter(player_valuations_new['date'],y=player_valuations_new['market_value_in_eur']/1000000, c='red',alpha=0.15)
plt.xlabel('date');plt.ylabel('Valuation in million euros')
plt.title('Player valuations over time',fontsize=28)
plt.show()

f = plt.figure(figsize=(10,6))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)
yeargroups1 = player_valuations_new.loc[:,['market_value_in_eur', 'year']].groupby(['year']).count() \
    .sort_values(by='year', ascending=True)
yeargroups2 = player_valuations_new.loc[:,['market_value_in_eur', 'year']] .groupby(['year']).sum() \
    .sort_values(by='year', ascending=True)
yeargroups3 = player_valuations_new.loc[:,['market_value_in_eur', 'year']].groupby(['year']).max() \
    .sort_values(by='year', ascending=True)
yeargroups4 = player_valuations_new.loc[:,['market_value_in_eur', 'year']] .groupby(['year']).min() \
    .sort_values(by='year', ascending=True)
yeargroups5 = player_valuations_new.loc[:,['market_value_in_eur', 'year']].groupby(['year']).median() \
    .sort_values(by='year', ascending=True)
yeargroups6 = player_valuations_new.loc[:,['market_value_in_eur', 'year']].groupby(['year']).mean() \
    .sort_values(by='year', ascending=True)

plt.subplot(1, 2, 1)
plt.title('Number of player valuations recorded per year')
plt.plot(yeargroups1.index,yeargroups1,color='green')
plt.ylabel('Market value (million euros)')
plt.subplot(1, 2, 2)
plt.title('Sum of player per year valuations')
plt.plot(yeargroups2.index,yeargroups2/1000000,color='blue')
plt.ylabel('Market value (million euros)')
plt.show()
plt.figure(figsize=(10,6))
plt.title('Max versus average player valuation over time',fontsize=28)
plt.plot(yeargroups3.index,yeargroups3/1000000,color='Red',label='max')
plt.plot(yeargroups5.index,yeargroups5/1000000,color='Lime',label='median')
plt.plot(yeargroups6.index,yeargroups6/1000000,color='Blue',label='mean')
plt.ylabel('Market value (million euros)')
plt.legend()
plt.show()

# Statistical Summaries

#1. Mean, Median, Mode of Goals

mean_goals = appearances['goals'].mean()
variance_goals = appearances['goals'].var()

print(f'Mean of Goals: {mean_goals}')
print(f'Variance of Goals: {variance_goals}')

#2. Mean, Median, Mode of Assists

mean_assists = appearances['assists'].mean()
variance_assists = appearances['assists'].var()

print(f'\nMean of Assists: {mean_assists}')
print(f'Variance of Assists: {variance_assists}')

#3. Mean, Median, Mode of Red Cards

mean_assists = appearances['red_cards'].mean()
variance_assists = appearances['red_cards'].var()

print(f'\nMean of Assists: {mean_assists}')
print(f'Variance of Assists: {variance_assists}')

#4. Mean, Median, Mode of Yellow Cards

mean_assists = appearances['yellow_cards'].mean()
variance_assists = appearances['yellow_cards'].var()

print(f'\nMean of Assists: {mean_assists}')
print(f'Variance of Assists: {variance_assists}')


#Final.to_csv('Final_data.csv', index=False)
