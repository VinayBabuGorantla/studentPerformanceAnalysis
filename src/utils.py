import os
import sys
import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Save the given object to the specified file path using pickle.

    Parameters:
    - file_path (str): The path to the file where the object will be saved.
    - obj: The object to be saved.

    Raises:
    - CustomException: If an error occurs during the saving process.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(f"Error during saving: {e}", sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluate machine learning models on training and test data.

    Parameters:
    - X_train: Training features.
    - y_train: Training labels.
    - X_test: Test features.
    - y_test: Test labels.
    - models (dict): A dictionary of models to be evaluated.
    - param (dict): A dictionary of hyperparameter grids for each model.

    Returns:
    - report (dict): A dictionary containing the test scores for each model.

    Raises:
    - CustomException: If an error occurs during the evaluation process.
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(f"Error during evaluation: {e}", sys)

def load_object(file_path):
    """
    Load an object from the specified file path using pickle.

    Parameters:
    - file_path (str): The path to the file containing the saved object.

    Returns:
    - The loaded object.

    Raises:
    - CustomException: If an error occurs during the loading process.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(f"Error during loading: {e}", sys)