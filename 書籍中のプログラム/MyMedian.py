"""
python wrapper for https://github.com/mmorise/beginning_asa/blob/main/書籍中のプログラム/MyMedian.m

-- 注意 --
実装に関係することはコメントしています。
関数の説明については書籍を参考にしてください。
"""
import numpy as np

def func(x):
    y=sorted(x)
    c=(len(x)+1)/2
    median_value=(y[np.floor(c)]+y[np.ceil(c)])/2
    return median_value

if __name__ == "__main__":
    func()