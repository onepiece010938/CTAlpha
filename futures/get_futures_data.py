import pandas as pd
from FinMind.data import DataLoader


def get_futures_data():
    """
    取得自1998-01-01起的台指期近月合約日頻率資料，返回pandas DataFrame
    """
    
    # 實例化DataLoader
    dl = DataLoader()

    # 使用taiwan_futures_daily方法取得自1998-01-01起的台指期日頻率資料
    futures_data = dl.taiwan_futures_daily(futures_id='TX', start_date='1998-01-01')

    # 篩選近月合約資料
    futures_data = futures_data[futures_data['contract_date'] == futures_data.groupby('date')['contract_date'].transform('min')]
    
    futures_data = futures_data[["date", "open", "max", "min", "close", "volume", "trading_session"]]
    futures_data.rename(columns={"max":"high", "min":"low"}, inplace=True)
    futures_data.set_index("date", inplace=True, drop=True)

    return futures_data


if __name__ == "__main__":
    
    futures_data = get_futures_data()
    
    futures_data.to_csv("futures_data.csv", encoding="utf-8-sig")
    
