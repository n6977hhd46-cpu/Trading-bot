candles = [
    {"open": 100, "high": 102, "low": 99, "close": 101, "volume": 1000},
    {"open": 101, "high": 103, "low": 100, "close": 102, "volume": 1100},
    {"open": 102, "high": 104, "low": 101, "close": 103, "volume": 1200},
    {"open": 103, "high": 105, "low": 102, "close": 104, "volume": 1300},
    {"open": 104, "high": 106, "low": 103, "close": 105, "volume": 1400},
    {"open": 105, "high": 107, "low": 104, "close": 106, "volume": 1500},
    {"open": 106, "high": 108, "low": 105, "close": 107, "volume": 1600},
    {"open": 107, "high": 109, "low": 106, "close": 108, "volume": 1700},
    {"open": 108, "high": 110, "low": 107, "close": 109, "volume": 1800},
    {"open": 109, "high": 111, "low": 108, "close": 110, "volume": 1900},
    {"open": 110, "high": 115, "low": 99, "close": 100, "volume": 3000},
]


def get_closing_prices(candles):
    closing_prices = []

    for candle in candles:
        closing_prices.append(candle["close"])

    return closing_prices


def calculate_ema(values, period):
    if len(values) < period:
        return None

    first_values = values[:period]
    ema = sum(first_values) / period    # Start point for calculation, start EMA here

    multiplier = 2 / (period + 1)

    for price in values[period:]:
        ema = price * multiplier + ema * (1 - multiplier) # update EMA with the next price

    return ema


def has_trend_confirmation(candles, period=10):
    closing_prices = get_closing_prices(candles)

    ema = calculate_ema(closing_prices, period)

    if ema is None:
        print("Not enough candles to calculate EMA")
        return False

    latest_close = closing_prices[-1]

    print("Latest close:", latest_close)
    print("EMA:", round(ema, 2))

    if latest_close > ema:
        print("Trend confirmation: True")
        return True
    else:
        print("Trend confirmation: False")
        return False


trend_confirmation = has_trend_confirmation(candles, period=10)

print("Final result:", trend_confirmation)
