from src.Plotting.plots import plot_curs_dist, plot_curs_time, plot_cur_runtime
from src.Cur.cur_decompositions import leverage_cur, subspace_cur
from sklearn.datasets import load_boston
import pandas as pd

if __name__ == '__main__':
    print("demo run")
    #boston = pd.DataFrame(load_boston(return_X_y=True)[0])
    #plot_curs_dist(boston, 10, 13, 25, "./Figs/boston/")
    #plot_curs_time(boston, 10, 13, 25, "./Figs/boston/")
    boston = pd.DataFrame(load_boston(return_X_y=True)[0])
    boston = boston - boston.mean(axis=0)
    #plot_cur_runtime(boston, 4, 10, 20, 15, "./Figs/boston/", data_name="Boston")