from sklearn.model_selection import train_test_split

X_train, X_valid, y_train, y_valid = train_test_split(data.iloc[:, 1:], data.Y,
                                                     test_size=0.3,
                                                     random_state=1)

