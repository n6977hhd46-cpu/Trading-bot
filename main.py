candles = [
    {"open": 100, "high": 105, "low": 98, "close": 104, "volume": 1000},
    {"open": 104, "high": 108, "low": 103, "close": 107, "volume": 1200},
    {"open": 107, "high": 110, "low": 105, "close": 109, "volume": 1300},
    {"open": 109, "high": 111, "low": 106, "close": 108, "volume": 1100},
    {"open": 108, "high": 115, "low": 107, "close": 110,"volume": 900},
]


def get_previous_high(candles):
    """
    Return the highest high from all candles except the latest candle.
    """
    previous_candles = candles[:-1]

    previous_highs = [] # creates an empty list to store the high values of previous candles

    for candle in previous_candles:
        previous_highs.append(candle["high"]) # append means add something to the end of the list. This loops through each candle in the previous_candles list and adds the high value of each candle to the previous_highs list.

    return max(previous_highs)


def get_average_previous_volume(candles):
    """
    Return the average volume from all candles except the latest candle.
    """
    previous_candles = candles[:-1]

    previous_volumes = []

    for candle in previous_candles:
        previous_volumes.append(candle["volume"])

    average_volume = sum(previous_volumes) / len(previous_volumes)

    return average_volume


def get_recent_low(candles):
    """
    Return the lowest low from all candles except the latest candle.
    """
    previous_candles = candles[:-1]

    previous_lows = []

    for candle in previous_candles:
        previous_lows.append(candle["low"])

    return min(previous_lows)


def is_breakout(candles):
    """
    Return True if the latest close is above the previous high.
    """
    latest_candle = candles[-1]
    latest_close = latest_candle["close"]

    previous_high = get_previous_high(candles)

    return latest_close > previous_high


def has_volume_confirmation(candles):
    """
    Return True if the latest volume is above the average previous volume.
    """
    latest_candle = candles[-1]
    latest_volume = latest_candle["volume"]

    average_previous_volume = get_average_previous_volume(candles)

    return latest_volume > average_previous_volume


def is_buy_signal(candles):
    """
    Return True if both breakout and volume confirmation are present.
    """
    return is_breakout(candles) and has_volume_confirmation(candles)


def calculate_trade_levels(candles, reward_multiplier):
    """
    Calculate entry price, stop-loss, take-profit, and risk value.
    """
    entry_price = candles[-1]["close"]
    stop_loss = get_recent_low(candles)

    risk = entry_price - stop_loss
    take_profit = entry_price + risk * reward_multiplier

    return {
        "entry_price": round(entry_price, 2),
        "stop_loss": round(stop_loss, 2),
        "take_profit": round(take_profit, 2),
        "risk": round(risk, 2),
        "reward_multiplier": reward_multiplier,
    }


previous_high = get_previous_high(candles)
average_volume = get_average_previous_volume(candles)
recent_low = get_recent_low(candles)

print("Previous high:", previous_high)
print("Average previous volume:", average_volume)
print("Recent low:", recent_low)

print("Breakout:", is_breakout(candles))
print("Volume confirmation:", has_volume_confirmation(candles))

if is_buy_signal(candles):
    print("Buy signal")

    trade_levels = calculate_trade_levels(candles, 3)

    print("Trade levels:")
    print("Entry price:", trade_levels["entry_price"])
    print("Stop-loss:", trade_levels["stop_loss"])
    print("Take-profit:", trade_levels["take_profit"])
    print("Risk:", trade_levels["risk"])
    print("Reward multiplier:", trade_levels["reward_multiplier"])
else:
    print("No buy signal")