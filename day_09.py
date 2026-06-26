candles = [
    {"open": 90, "high": 92, "low": 89, "close": 91, "volume": 1000},
    {"open": 91, "high": 93, "low": 90, "close": 92, "volume": 1050},
    {"open": 92, "high": 94, "low": 91, "close": 93, "volume": 1100},
    {"open": 93, "high": 95, "low": 92, "close": 94, "volume": 1080},
    {"open": 94, "high": 96, "low": 93, "close": 95, "volume": 1120},
    {"open": 95, "high": 97, "low": 94, "close": 96, "volume": 1150},
    {"open": 96, "high": 98, "low": 95, "close": 97, "volume": 1170},
    {"open": 97, "high": 99, "low": 96, "close": 98, "volume": 1200},
    {"open": 98, "high": 100, "low": 97, "close": 99, "volume": 1180},
    {"open": 99, "high": 101, "low": 98, "close": 100, "volume": 1220},
    {"open": 100, "high": 102, "low": 99, "close": 101, "volume": 1250},
    {"open": 101, "high": 103, "low": 100, "close": 102, "volume": 1280},
    {"open": 102, "high": 104, "low": 101, "close": 103, "volume": 1300},
    {"open": 103, "high": 105, "low": 102, "close": 104, "volume": 1320},
    {"open": 104, "high": 106, "low": 103, "close": 105, "volume": 1350},
    {"open": 105, "high": 107, "low": 104, "close": 106, "volume": 1370},
    {"open": 106, "high": 108, "low": 105, "close": 107, "volume": 1400},
    {"open": 107, "high": 109, "low": 106, "close": 108, "volume": 1420},
    {"open": 108, "high": 110, "low": 107, "close": 109, "volume": 1450},
    {"open": 109, "high": 111, "low": 108, "close": 110, "volume": 1480},
    {"open": 110, "high": 112, "low": 109, "close": 111, "volume": 1500},
    {"open": 111, "high": 113, "low": 110, "close": 112, "volume": 1520},
    {"open": 112, "high": 114, "low": 111, "close": 113, "volume": 1550},
    {"open": 113, "high": 115, "low": 112, "close": 114, "volume": 1580},
    {"open": 114, "high": 116, "low": 113, "close": 115, "volume": 1600},
    {"open": 115, "high": 117, "low": 114, "close": 116, "volume": 1620},
    {"open": 116, "high": 118, "low": 115, "close": 117, "volume": 1650},
    {"open": 117, "high": 119, "low": 116, "close": 118, "volume": 1680},
    {"open": 118, "high": 120, "low": 117, "close": 119, "volume": 1700},
    {"open": 119, "high": 121, "low": 118, "close": 120, "volume": 1720},
    {"open": 120, "high": 122, "low": 119, "close": 121, "volume": 1750},
    {"open": 121, "high": 123, "low": 120, "close": 122, "volume": 1780},
    {"open": 122, "high": 124, "low": 121, "close": 123, "volume": 1800},
    {"open": 123, "high": 125, "low": 122, "close": 124, "volume": 1820},
    {"open": 124, "high": 126, "low": 123, "close": 125, "volume": 1850},
    {"open": 125, "high": 127, "low": 124, "close": 126, "volume": 1880},
    {"open": 126, "high": 128, "low": 125, "close": 127, "volume": 1900},
    {"open": 127, "high": 129, "low": 126, "close": 128, "volume": 1920},
    {"open": 128, "high": 130, "low": 127, "close": 129, "volume": 1950},
    {"open": 129, "high": 131, "low": 128, "close": 130, "volume": 1980},
    {"open": 130, "high": 132, "low": 129, "close": 131, "volume": 2000},
    {"open": 131, "high": 133, "low": 130, "close": 132, "volume": 2050},
    {"open": 132, "high": 134, "low": 130, "close": 131, "volume": 2100},
    {"open": 131, "high": 133, "low": 129, "close": 130, "volume": 2150},
    {"open": 130, "high": 134, "low": 129, "close": 133, "volume": 2200},
    {"open": 133, "high": 136, "low": 132, "close": 135, "volume": 2300},
    {"open": 135, "high": 137, "low": 133, "close": 134, "volume": 2400},
    {"open": 134, "high": 139, "low": 133, "close": 138, "volume": 2600},
    {"open": 138, "high": 143, "low": 137, "close": 142, "volume": 4200},

]


def get_closing_prices(candles):
    closes = []

    for candle in candles:
        closes.append(candle["close"])

    return closes


def get_previous_high(candles):
    previous_candles = candles[:-1]
    previous_highs = []

    for candle in previous_candles:
        previous_highs.append(candle["high"])

    return max(previous_highs)


def get_average_previous_volume(candles):
    previous_candles = candles[:-1]
    previous_volumes = []

    for candle in previous_candles:
        previous_volumes.append(candle["volume"])

    return sum(previous_volumes) / len(previous_volumes)


def is_breakout(candles):
    latest_candle = candles[-1]
    latest_close = latest_candle["close"]
    previous_high = get_previous_high(candles)

    return latest_close > previous_high


def has_volume_confirmation(candles):
    latest_candle = candles[-1]
    latest_volume = latest_candle["volume"]
    average_previous_volume = get_average_previous_volume(candles)

    return latest_volume > average_previous_volume


def calculate_price_changes(closing_prices):
    changes = []

    for i in range(1, len(closing_prices)):
        change = closing_prices[i] - closing_prices[i - 1]
        changes.append(change)

    return changes


def separate_gains_and_losses(changes):
    gains = []
    losses = []

    for change in changes:
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    return gains, losses


def calculate_rsi(candles, period=14):
    closing_prices = get_closing_prices(candles)

    if len(closing_prices) < period + 1:
        return None

    recent_closes = closing_prices[-(period + 1):]
    changes = calculate_price_changes(recent_closes)

    gains, losses = separate_gains_and_losses(changes)

    average_gain = sum(gains) / period
    average_loss = sum(losses) / period

    if average_loss == 0:
        return 100

    relative_strength = average_gain / average_loss
    rsi = 100 - (100 / (1 + relative_strength))

    return rsi


def has_acceptable_rsi(candles, max_rsi=80):
    rsi = calculate_rsi(candles)

    if rsi is None:
        return False

    return rsi <= max_rsi


def calculate_ema(values, period):
    if len(values) < period:
        return None

    ema_values = []

    first_ema = sum(values[:period]) / period
    ema_values.append(first_ema)

    multiplier = 2 / (period + 1)

    for price in values[period:]:
        new_ema = (price * multiplier) + (ema_values[-1] * (1 - multiplier))
        ema_values.append(new_ema)

    return ema_values


def calculate_macd(candles, fast_period=12, slow_period=26, signal_period=9):
    closing_prices = get_closing_prices(candles)

    if len(closing_prices) < slow_period + signal_period:
        return None

    fast_ema_values = calculate_ema(closing_prices, fast_period)
    slow_ema_values = calculate_ema(closing_prices, slow_period)

    fast_ema_values = fast_ema_values[-len(slow_ema_values):]

    macd_line_values = []

    for fast_ema, slow_ema in zip(fast_ema_values, slow_ema_values):
        macd_line = fast_ema - slow_ema
        macd_line_values.append(macd_line)

    signal_line_values = calculate_ema(macd_line_values, signal_period)

    if signal_line_values is None:
        return None

    latest_macd_line = macd_line_values[-1]
    latest_signal_line = signal_line_values[-1]
    latest_histogram = latest_macd_line - latest_signal_line

    return {
        "macd_line": latest_macd_line,
        "signal_line": latest_signal_line,
        "histogram": latest_histogram
    }


def has_macd_confirmation(candles):
    macd = calculate_macd(candles)

    if macd is None:
        return False

    return macd["macd_line"] > macd["signal_line"] and macd["histogram"] > 0


def is_buy_signal(candles):
    return (
        is_breakout(candles)
        and has_volume_confirmation(candles)
        and has_acceptable_rsi(candles, max_rsi=90)
        and has_macd_confirmation(candles)
    )


def get_recent_low(candles):
    previous_candles = candles[:-1]
    previous_lows = []

    for candle in previous_candles:
        previous_lows.append(candle["low"])

    return min(previous_lows)


def calculate_trade_levels(candles, reward_multiplier=2):
    latest_candle = candles[-1]

    entry_price = latest_candle["close"]
    stop_loss = get_recent_low(candles)

    risk = entry_price - stop_loss
    take_profit = entry_price + (risk * reward_multiplier)

    return {
        "entry_price": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "risk": risk,
        "reward_multiplier": reward_multiplier
    }


macd = calculate_macd(candles)
rsi = calculate_rsi(candles)

print("Previous high:", get_previous_high(candles))
print("Latest close:", candles[-1]["close"])
print("Breakout:", is_breakout(candles))

print("Average previous volume:", round(get_average_previous_volume(candles), 2))
print("Latest volume:", candles[-1]["volume"])
print("Volume confirmation:", has_volume_confirmation(candles))

print("RSI:", round(rsi, 2))
print("Acceptable RSI:", has_acceptable_rsi(candles))

print("MACD line:", round(macd["macd_line"], 4))
print("Signal line:", round(macd["signal_line"], 4))
print("Histogram:", round(macd["histogram"], 4))
print("MACD confirmation:", has_macd_confirmation(candles))

print("Buy signal:", is_buy_signal(candles))

if is_buy_signal(candles):
    trade_levels = calculate_trade_levels(candles)

    print("Entry price:", trade_levels["entry_price"])
    print("Stop loss:", trade_levels["stop_loss"])
    print("Take profit:", trade_levels["take_profit"])
    print("Risk:", trade_levels["risk"])
    print("Reward multiplier:", trade_levels["reward_multiplier"])
else:
    print("No trade.")

print(macd)