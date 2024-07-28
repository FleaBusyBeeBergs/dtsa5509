def strip_spaces(X):
    X = X.copy()
    # strip leading spaces from column names
    X.columns = X.columns.str.strip()
    # strip leading spaces from string values
    X = X.apply(lambda x: x.str.lstrip() if x.dtype == 'object' else x)
    return X

def convert_to_category(X):
    X = X.copy()
    X['no_of_dependents'] = X['no_of_dependents'].astype('category')
    return X

def convert_to_binary(X):
    X = X.copy()
    X['education'] = X['education'].map({'Not Graduate': 0, 'Graduate': 1})
    return X

