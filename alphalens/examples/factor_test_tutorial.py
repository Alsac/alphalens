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



data = pd.read_hdf(r'C:\Users\wangyl\Documents\GitHub\alphalens\alphalens\examples\predict_signal_500.hdf')
prices = (1 + data.iloc[:, -1].unstack()).cumprod()  #multi-index 2-dim data to 2-dim data for 'close' column
prices.fillna(method='ffill', inplace=True)
factor = data.loc[:, 'predict_0']  # take the column as factor
factor = factor.groupby(as_index=True, level=1).apply(lambda x:x.fillna(method='ffill'))

factor_data = get_clean_factor_and_forward_returns(factor=factor, prices=prices, groupby=None, quantiles=10, periods=(5,10,))

create_full_tear_sheet(factor_data, long_short=True, execute_num=[1])
create_full_tear_sheet(factor_data, long_short=True, execute_num=[3], save_path=r'C:\Users\wangyl\Documents\GitHub\alphalens\alphalens\examples')
create_returns_tear_sheet(factor_data, long_short=True, group_neutral=False, by_group=False, set_context=False, save_path=r'C:\Users\wangyl\Documents\GitHub\alphalens\alphalens\examples')
create_information_tear_sheet(factor_data, save_path=r'C:\Users\wangyl\Documents\GitHub\alphalens\alphalens\examples')
create_turnover_tear_sheet(factor_data, set_context=False, save_path=r'C:\Users\wangyl\Documents\GitHub\alphalens\alphalens\examples')

