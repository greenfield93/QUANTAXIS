# import pandas as pd
# data = pd.read_excel('test.xlsx')
# print(data)
from QUANTAXIS.QAFetch import QA_fetch_get_stock_block
from QUANTAXIS.QAFetch.QATdx import (
    QA_fetch_get_option_day,
    QA_fetch_get_option_min,
    QA_fetch_get_index_day,
    QA_fetch_get_index_min,
    QA_fetch_get_stock_day,
    QA_fetch_get_stock_info,
    QA_fetch_get_stock_list,
    QA_fetch_get_future_list,
    QA_fetch_get_index_list,
    QA_fetch_get_future_day,
    QA_fetch_get_future_min,
    QA_fetch_get_stock_min,
    QA_fetch_get_stock_transaction,
    QA_fetch_get_index_transaction,
    QA_fetch_get_stock_xdxr,
    QA_fetch_get_bond_day,
    QA_fetch_get_bond_list,
    QA_fetch_get_bond_min,
    select_best_ip,
    QA_fetch_get_hkstock_day,
    QA_fetch_get_hkstock_list,
    QA_fetch_get_hkstock_min,
    QA_fetch_get_usstock_list,
    QA_fetch_get_usstock_day,
    QA_fetch_get_usstock_min,
)

from QUANTAXIS.QAFetch.QATdx import (

    QA_fetch_get_commodity_option_AL_contract_time_to_market,
    QA_fetch_get_commodity_option_AU_contract_time_to_market,
    QA_fetch_get_commodity_option_CU_contract_time_to_market,
    QA_fetch_get_commodity_option_SR_contract_time_to_market,
    QA_fetch_get_commodity_option_M_contract_time_to_market,
    QA_fetch_get_commodity_option_RU_contract_time_to_market,
    QA_fetch_get_commodity_option_CF_contract_time_to_market,
    QA_fetch_get_commodity_option_C_contract_time_to_market,
    QA_fetch_get_option_50etf_contract_time_to_market,
    QA_fetch_get_option_300etf_contract_time_to_market,
    QA_fetch_get_option_all_contract_time_to_market,

    QA_fetch_get_option_list,
)
from QUANTAXIS.QAUtil import (
    DATABASE,
    QA_util_get_next_day,
    QA_util_get_real_date,
    QA_util_log_info,
    QA_util_to_json_from_pandas,
    trade_date_sse
)
from QUANTAXIS.QAData.data_fq import _QA_data_stock_to_fq
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_stock_day
from QUANTAXIS.QAUtil import Parallelism
from QUANTAXIS.QAFetch.QATdx import ping, get_ip_list_by_multi_process_ping, stock_ip_list
from multiprocessing import cpu_count
data=QA_fetch_get_stock_block('tdx')
QA_util_to_json_from_pandas(data)
#QA_SU_save_stock_block
#stock_list = QA_fetch_get_stock_list().code.unique().tolist()
#print(stock_list)
#print(data)
# import numpy as np
# import pandas as pd
# sz = pd.DataFrame([['0','sz','stock_cn'],['1','sz','stock_cn'],['2','sz','stock_cn']],
            #  columns=['code', 'sse','sec'])
# sh = pd.DataFrame([['0','sh','stock_cn'],['1','sh','stock_cn']], 
            #  columns=['code', 'sse','sec'])
# print(sz)
# print(sh)
# result = pd.concat([sz, sh],sort=False).query(
                # 'sec=="stock_cn"').sort_index()
# print(result)

# print('将df1,df2横向外连接，设置层次索引')
# result = pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
                #    sort=False)
# print(result)
# result = pd.concat([df1, df2], axis=0, keys=['level1', 'level2'],
                #    sort=False)
# print(result)
# result = pd.concat([df1, df2], axis=0, keys=['level1', 'level2'],
                #    sort=False)
# print(result)
# 
# print('使用字典设置层次索引,横向外连接')
# result = pd.concat({'level1': df1, 'level2': df2}, axis=1, sort=False)
# print(result)
# print('将df1,df2横向外连接，设置层次索引和设置层次索引的级别名称')
# result = pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
                #    names=['upper', 'lower'],sort=False)
# print(result)
#将两个不相同的列的数据框合并
# df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
# print(df1)
# print(df2)
# print('df1,df2纵向外连接,忽略原index,重建索引')
# print(pd.concat([df1, df2], ignore_index=True,sort=False))