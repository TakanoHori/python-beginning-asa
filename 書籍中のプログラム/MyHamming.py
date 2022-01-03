"""
python wrapper for https://github.com/mmorise/beginning_asa/blob/main/書籍中のプログラム/MyHamming.m

-- 注意 --
実装に関係することはコメントしています。
関数の説明については書籍を参考にしてください。
"""
import numpy as np

def func(N):
    n=np.arange(0,N).reshape(-1,1)
    win=0.54-0.46*np.cos(2*np.pi*n/N)
    return win

if __name__ == "__main__":
    func()