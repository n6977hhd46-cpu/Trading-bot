candles = [
    {"open": 100, "high": 102, "low": 99, "close": 101, "volume": 1000},
    {"open": 101, "high": 103, "low": 100, "close": 102, "volume": 1100},
    {"open": 102, "high": 104, "low": 101, "close": 101, "volume": 1200},
    {"open": 103, "high": 105, "low": 102, "close": 103, "volume": 1300},
    {"open": 104, "high": 106, "low": 103, "close": 102, "volume": 1400},
    {"open": 105, "high": 107, "low": 104, "close": 104, "volume": 1500},
    {"open": 106, "high": 108, "low": 105, "close": 103, "volume": 1600},
    {"open": 107, "high": 109, "low": 106, "close": 105, "volume": 1700},
    {"open": 108, "high": 110, "low": 107, "close": 106, "volume": 1800},
    {"open": 109, "high": 111, "low": 108, "close": 105, "volume": 1900},
    {"open": 110, "high": 112, "low": 109, "close": 107, "volume": 2000},
    {"open": 111, "high": 113, "low": 110, "close": 108, "volume": 2100},
    {"open": 112, "high": 114, "low": 111, "close": 107, "volume": 2200},
    {"open": 113, "high": 115, "low": 112, "close": 114, "volume": 2300},
    {"open": 114, "high": 121, "low": 113, "close": 116, "volume": 4000},
]


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

    average_previous_volume = sum(previous_volumes) / len(previous_volumes)

    return average_previous_volume


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
    take_profit = entry_price + risk * reward_multiplier

    trade_levels = {
        "entry_price": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "risk": risk,
        "reward_multiplier": reward_multiplier,
    }

    return trade_levels


def get_closing_prices(candles):
    closing_prices = []

    for candle in candles:
        closing_prices.append(candle["close"])

    return closing_prices


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

    recent_prices = closing_prices[-(period + 1):]
    changes = calculate_price_changes(recent_prices)

    gains, losses = separate_gains_and_losses(changes)

    average_gain = sum(gains) / period
    average_loss = sum(losses) / period

    if average_loss == 0:
        return 100

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))

    return round(rsi, 2)


def has_acceptable_rsi(candles, max_rsi=80):
    rsi = calculate_rsi(candles)

    if rsi is None:
        return False

    return rsi <= max_rsi


def is_buy_signal(candles):
    breakout = is_breakout(candles)
    volume_confirmation = has_volume_confirmation(candles)
    acceptable_rsi = has_acceptable_rsi(candles)

    return breakout and volume_confirmation and acceptable_rsi


rsi = calculate_rsi(candles)

print("Previous high:", get_previous_high(candles))
print("Average previous volume:", get_average_previous_volume(candles))
print("Latest close:", candles[-1]["close"])
print("Latest volume:", candles[-1]["volume"])
print("RSI:", rsi)

print("Breakout:", is_breakout(candles))
print("Volume confirmation:", has_volume_confirmation(candles))
print("Acceptable RSI:", has_acceptable_rsi(candles))
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