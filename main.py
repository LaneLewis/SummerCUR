from src.Plotting.plots import plot_curs_dist, plot_curs_time
from src.Cur.cur_decompositions import leverage_cur, subspace_cur
from sklearn.datasets import load_boston
import pandas as pd

if __name__ == '__main__':
    print("demo run")
    boston = pd.DataFrame(load_boston(return_X_y=True)[0])
    plot_curs_dist(boston, 10, 13, 25, "./Figs/boston/")
    plot_curs_time(boston, 10, 13, 25, "./Figs/boston/")