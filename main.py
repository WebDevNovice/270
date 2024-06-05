import pandas as pd
import numpy as np

def metric_calculator(Pts_or_Ast, Pct_or_Reb):
    '''
    This function actually does the math to 
    create the array's with the new metrics
    '''
    new_metric = []
    for i in range(len(Pts_or_Ast)):
        new_value = Pts_or_Ast[i]/Pct_or_Reb[i]
        new_metric.append(new_value)
    return new_metric

def clean_data(dataset):
    '''
    This function takes the games.csv and creates the home_team_scoring_metric, 
    home_assit_rebound_ratio, away_team_scoring_metric, away_assit_rebound_ratio
    '''
    #Home Team
    home_team_pts = np.array(dataset['PTS_home'])
    home_team_pct = np.array(dataset['FG_PCT_home'])
    home_REB = np.array(dataset['REB_home'])
    home_AST = np.array(dataset['AST_home'])
    home_team_scoring_metric = metric_calculator(home_team_pts,home_team_pct)
    home_assit_rebound_ratio = metric_calculator(home_AST,home_REB)
    #Away Team
    away_team_pts = np.array(dataset['PTS_away'])
    away_team_pct = np.array(dataset['FG_PCT_away'])
    away_team_scoring_metric = metric_calculator(away_team_pts,away_team_pct)
    away_REB = np.array(dataset['REB_away'])
    away_AST = np.array(dataset['AST_away'])
    away_assit_rebound_ratio = metric_calculator(away_AST,away_REB)
    return home_team_scoring_metric, home_assit_rebound_ratio, away_team_scoring_metric, away_assit_rebound_ratio


def new_metrics_df(array_1,array_2,array_3,array_4, dataset):
    data = {
        'HOME_TEAM_SCORING_METRIC': array_1,
        'HOME_ASSIT_REBOUND_RATIO': array_2,
        'AWAY_TEAM_SCORING_METRIC': array_3,
        'AWAY_ASSIT_REBOUND_RATIO': array_4
    }
    new_lst_df = pd.DataFrame(data)
    new_dataset = dataset.join(new_lst_df)
    return new_dataset

def drop_columns(dataframe):
    games_drop_labels =['GAME_STATUS_TEXT','GAME_DATE_EST','FG_PCT_home', 'FT_PCT_home', 
    'FG3_PCT_home','FG_PCT_away', 'FT_PCT_away','FG3_PCT_away','PTS_home', 'AST_home',
    'REB_home','PTS_away', 'AST_away', 'REB_away','GAME_ID','GAME_STATUS_TEXT','SEASON', 
    'GAME_DATE_EST','HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'HOME_TEAM_WINS']
    return dataframe.drop(games_drop_labels,axis=1)

def clean_the_data():
    dataset_games = pd.read_csv('games.csv', low_memory=False) #Read in the game data
    dataset_games_details = pd.read_csv('games_details.csv', low_memory=False)#Read in the game details data 

    dataset_games_df = pd.DataFrame(dataset_games) # Create the dataframe
    
    
    home_team_scoring_metric, home_assit_rebound_ratio, away_team_scoring_metric, away_assit_rebound_ratio = clean_data(dataset_games_df)
    
    reduced_metrics_df = new_metrics_df(home_team_scoring_metric, home_assit_rebound_ratio,
                                        away_team_scoring_metric, away_assit_rebound_ratio, dataset_games_df)
    
    

    dataset_games_df_clean = drop_columns(reduced_metrics_df)
    dataset_games_df_clean.to_csv('games_clean.csv')

def main():
    # clean_the_data()

if __name__ == "__main__":
    main()
