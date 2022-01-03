"""
python wrapper for https://github.com/mmorise/beginning_asa/blob/main/書籍中のプログラム/MinimumPhase.m

-- 注意 --
実装に関係することはコメントしています。
関数の説明については書籍を参考にしてください。
"""
import numpy as np

def func(x):
    x_len_half=int(len(x)/2)-1
    X=(np.fft.ifftn(np.log(abs(np.fft.fftn(x,s=x.shape,axes=(0,1)))),s=x.shape,axes=(0,1))).real
    w=np.concatenate([[1],2*np.ones((x_len_half)),[1],np.zeros((x_len_half))]).reshape(-1,1)
    y=(np.fft.ifftn(np.exp(np.fft.fftn(w*X)))).real
    return y

if __name__ == "__main__":
    func()