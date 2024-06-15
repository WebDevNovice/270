import main
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
import tabulate


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
    new_clf = DecisionTreeClassifier(max_depth=3)
    new_clf.fit(X_train, y_train)
    clf.fit(X_train, y_train)
    test_score = clf.score(X_test, y_test)
    train_score = clf.score(X_train, y_train)
    feature_names = list(df.columns)
    return train_score, test_score, clf, new_clf, feature_names

total_train = 0
total_test = 0
table_data = [['Run','Train Acc', 'Test Acc']]
tree_plots = []
max_train = 0
max_test = 0
for i in range(1, 101):
    train, test, clf, new_clf, feature_names = decisionTree()
    total_train += train
    total_test += test
    table_data.append([i, train, test])
    if train > max_train:
        max_train = train
    if test > max_test:
        max_test = test
plt.figure(figsize=(20,10))
tree.plot_tree(new_clf, filled=True, feature_names=feature_names)
filename = f'decisiontree{i}.png'
plt.savefig(filename)
plt.close()
avg_train = total_train / i
avg_test = total_test / i
print(f"Average Test Acc: {avg_test}\nAverage Train Acc: {avg_train}\nMax Test: {max_test}\nMax Train: {max_train}")
print(tabulate.tabulate(table_data[1:], headers=table_data[0], tablefmt='fancy-grid'))
