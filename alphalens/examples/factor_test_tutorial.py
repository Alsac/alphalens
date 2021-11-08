# -*- coding: utf-8 -*-
# @Time : 2021/11/5 21:54
# @Author : Alsac Wang
# @Email : yukf@whu.edu.cn
# @File : factor_test_tutorial.py
# need pandas==0.20.2  python <=3.6  alphalens '0.4.0+3.g06793bd.dirty'
import pandas as pd
import sys
sys.path.append(r'C:\Users\wangyl\Documents\GitHub\alphalens')
import alphalens
from alphalens.tears import (create_full_tear_sheet, create_event_returns_tear_sheet, create_turnover_tear_sheet,create_information_tear_sheet, create_returns_tear_sheet)
from alphalens.utils import get_clean_factor_and_forward_returns



data = pd.read_hdf(r'C:\Users\wangyl\Documents\GitHub\alphalens\alphalens\examples\predict_signal_500.hdf')  # read data
prices = (1 + data.iloc[:, -1].unstack()).cumprod()  # multi-index 2-dim data to 2-dim data for 'close' column  prices的index是时间，column是股票标的，value为价格
prices.fillna(method='ffill', inplace=True)  # 缺失值填充
factor = data.loc[:, 'predict_0']  # take the column as factor
factor = factor.groupby(as_index=True, level=1).apply(lambda x:x.fillna(method='ffill'))  # 缺失值填充





#标准化因子数据，具体参数含义间函数注释
factor_data = get_clean_factor_and_forward_returns(factor=factor,prices=prices,
                                         groupby=None,
                                         binning_by_group=False,
                                         quantiles=5,
                                         bins=None,
                                         periods=(1, 5, 10),
                                         filter_zscore=20,
                                         groupby_labels=None,
                                         max_loss=0.2,
                                         zero_aware=False,
                                         cumulative_returns=True,
                                        )

#打印因子回测图
create_full_tear_sheet(factor_data,
                       long_short=True,
                       group_neutral=False,
                       by_group=False,
                       execute_num=[1,2,3],
                       save_path=r'C:\Users\wangyl\Documents\GitHub\alphalens\alphalens\examples')


