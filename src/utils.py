import os
import sys
import numpy as np
import pandas as pd
import dill

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor 
from xgboost import XGBRegressor

from src.exception import CustomException

from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(x_train, y_train, x_test, y_test, models, params):
    try:
        report = {}
        best_model = None
        best_score = -float("inf")

        
        for model_name, model in models.items():

            if model_name not in params:
                raise ValueError(f"Hyperparameters not defined for {model_name}")
            param_grid = params[model_name]


            gs = GridSearchCV(model,param_grid,cv=3)
            gs.fit(x_train,y_train)

            fitted_model = gs.best_estimator_
            
            #model.fit(x_train, y_train) #Train Model

            y_train_pred = fitted_model.predict(x_train)

            y_test_pred = fitted_model.predict(x_test)

            test_score = r2_score(y_test, y_test_pred)
            
          
            report[model_name] = test_score

            if test_score > best_score:
                best_score = test_score
                best_model = fitted_model

        return report, best_model
    
    except Exception as e:
        raise CustomException(e, sys)