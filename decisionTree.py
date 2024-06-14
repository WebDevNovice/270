import main
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt


def drop_columns_dt(dataframe: pd.DataFrame):
    games_drop_labels =['GAME_STATUS_TEXT','GAME_DATE_EST','FG_PCT_home', 'FT_PCT_home', 
    'FG3_PCT_home','FG_PCT_away', 'FT_PCT_away','FG3_PCT_away','PTS_home', 'AST_home',
    'REB_home','PTS_away', 'AST_away', 'REB_away','GAME_ID','GAME_STATUS_TEXT','SEASON', 
    'GAME_DATE_EST','HOME_TEAM_ID', 'VISITOR_TEAM_ID']
    return dataframe.drop(games_drop_labels,axis=1)
def create_dataframe():
    df = pd.DataFrame(pd.read_csv(r"C:\Users\grant\OneDrive\Desktop\CS201R\project\270\games.csv"))
    return df
def decisionTree():
    df = create_dataframe()
    htsm, harr, atsm, aarr = main.clean_data(df)
    df = main.new_metrics_df(htsm, harr, atsm, aarr, df)
    df = drop_columns_dt(df)
    # Identify the columns
    cols = list(df.columns)
    # Move the third column (index 2) to the last position
    col_to_move = cols.pop(2)
    cols.append(col_to_move)
    # Reorder the DataFrame columns
    df = df[cols]
    clf = DecisionTreeClassifier(max_depth=6)
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.15)
    clf.fit(X_train, y_train)
    test_score = clf.score(X_test, y_test)
    train_score = clf.score(X_train, y_train)
    print(f"Test Score: {test_score}\nTrain Score: {train_score}")
    tree.plot_tree(clf)


decisionTree()

    



