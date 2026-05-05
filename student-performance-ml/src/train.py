from data_loader import load_data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error
import pickle
from pathlib import Path
 
 
def train_model():
    # 1. Load data
    df = load_data()
 
    # 2. Encode categorical variables
    df_encoded = pd.get_dummies(df, drop_first=True)
 
    # 3. Define features and target
    X = df_encoded.drop(columns=['math score'])
    y = df_encoded['math score']
 
    # 4. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
 
    # 5. Train model (Random Forest - best model)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
 
    # 6. Predictions
    y_pred = model.predict(X_test)
 
    # 7. Evaluation
    print("Model Performance:")
    print("R2 Score:", r2_score(y_test, y_pred))
    print("RMSE:", root_mean_squared_error(y_test, y_pred))
 
    # 8. Save model
    model_path = Path(__file__).resolve().parents[1] / "models" / "model.pkl"
 
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
 
    print("Model saved successfully!")
 
 
if __name__ == "__main__":
    train_model()