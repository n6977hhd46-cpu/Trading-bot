candles = [
    {"open": 100, "high": 105, "low": 98, "close": 104, "volume": 1000},
    {"open": 104, "high": 108, "low": 103, "close": 107, "volume": 1200},
    {"open": 107, "high": 110, "low": 105, "close": 109, "volume": 1300},
    {"open": 109, "high": 111, "low": 106, "close": 108, "volume": 1100},
    {"open": 108, "high": 115, "low": 107, "close": 114, "volume": 2000},
]

latest_candle = candles[-1] # latest candle
candles_except_latest = candles[:-1] # all candles except the latest

print(latest_candle)
print(latest_candle["close"]) # latest candle close price
print(latest_candle["volume"]) # latest candle volume









