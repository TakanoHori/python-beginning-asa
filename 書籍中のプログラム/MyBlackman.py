"""
python wrapper for https://github.com/mmorise/beginning_asa/blob/main/書籍中のプログラム/MyBlackman.m

-- 注意 --
実装に関係することはコメントしています。
関数の説明については書籍を参考にしてください。
"""
import numpy as np

def func(N):
    n=np.arange(0,N+1).reshape(-1,1)
    win=0.42-0.5*np.cos(2*np.pi*n/N)+0.08*np.cos(4*np.pi*n/N)
    return win

if __name__ == "__main__":
    func()