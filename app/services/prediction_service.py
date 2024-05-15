from sklearn.preprocessing import MinMaxScaler

def get_prediction(df, ticker):
    return {"date": "2023-01-01", "predicted_price": 100.0}

def preprocess_data(df):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[['Close']])
    return scaled_data, scaler