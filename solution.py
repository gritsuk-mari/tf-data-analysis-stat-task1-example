import pandas as pd
import numpy as np


chat_id = 232852966 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 10 
    x = (x - 49 + np.exp(1)) / t 
    return x.mean() # Ваш ответ
