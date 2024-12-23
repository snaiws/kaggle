from typing import Optional, Union, Tuple

import numpy as np
from sklearn.metrics import mean_squared_log_error
import lightgbm as lgb


def root_mean_squared_log_error(trues, preds):
    msle = mean_squared_log_error(trues, preds)
    rmsle = np.sqrt(msle)
    return rmsle

def root_mean_squared_log_error_lgbm(
    preds: np.ndarray, data: lgb.Dataset, threshold: float=0.5,
) -> Tuple[str, float, bool]:

    """Calculate Binary Accuracy"""
    label = data.get_label()
    # weight = data.get_weight()
    rmsle = root_mean_squared_log_error(label, preds)

    # # eval_name, eval_result, is_higher_better
    return 'rmsle', rmsle, False