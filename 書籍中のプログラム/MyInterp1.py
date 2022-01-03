"""
python wrapper for https://github.com/mmorise/beginning_asa/blob/main/書籍中のプログラム/MyInterp1.m

-- 注意 --
実装に関係することはコメントしています。
関数の説明については書籍を参考にしてください。
"""
import numpy as np

def func(x, y, xi):
    delta_x = x[1]-x[0]

    # MyInterp1.m#L3
    # 1つの値と配列を引数として、最小値・最大値を求める関数が見つからなかったので、for文で1つずつ比較
    for i in range(len(xi)):
        tmp = min(x[-1],xi[i])
        xi[i] = max(x[0],tmp)
    
    xi_base = [ np.floor((i-x[0])/delta_x) for i in xi]
    xi_fraction = [ (xi[i]-x[0])/delta_x-xi_base[i] for i in range(len(xi)) ]

    # diff(y): yの隣接する要素間の差分を計算
    delta_y = np.append(np.diff(y),0.0)

    # MyInterp1.m#L7
    # xi_baseの値を配列の添字として使うことをfor文で実装
    # 各配列は以下のように対応する
    # y(xi_base+1) = tmp_y
    # delta_y(xi_base+1) = tmp_delta_y
    tmp_y=np.empty((0,1))
    tmp_delta_y=np.empty((0,1))
    for i in xi_base:
        tmp_y = np.append(tmp_y,np.array([[y[int(i)+1]]]),axis=0)
        tmp_delta_y = np.append(tmp_delta_y, np.array([[delta_y[int(i)+1]]]),axis=0)
    yi = tmp_y+tmp_delta_y*xi_fraction
    return yi

if __name__ == "__main__":
    func()