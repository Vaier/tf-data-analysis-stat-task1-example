import pandas as pd
import numpy as np


chat_id = 1251251937 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = np.exp(np.log(x).mean())
    return a
