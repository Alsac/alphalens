# -*- coding: utf-8 -*-
# @Time : 2021/11/5 21:54
# @Author : Alsac Wang
# @Email : yukf@whu.edu.cn
# @File : factor_test_tutorial.py

import sys
sys.path.append(r'C:\Users\wangyl\Documents\GitHub\alphalens')
import alphalens
from alphalens.tears import (create_full_tear_sheet, create_event_returns_tear_sheet)
from alphalens.utils import get_clean_factor_and_forward_returns

factor_data = get_clean_factor_and_forward_returns(factor=factor, prices=prices, groupby=None, quantiles=5,
                                                               periods=(1, 3, 5))
create_full_tear_sheet(factor_data, long_short=True, execute_num=[1],\
                       save_path=r'/home/wangyanlong/project/bt_picture/')
create_full_tear_sheet(factor_data, long_short=True, execute_num=[3], \
                       save_path=r'/home/wangyanlong/project/bt_picture/')