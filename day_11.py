def calculate_true_range(current_candle, previous_candle):
    high = current_candle['high']
    low = current_candle['low']
    previous_close = previous_candle['close']

    tr = max(
        high - low,
        abs(high - previous_close),
        abs(low - previous_close)
    )
    return tr

def calculate_atr(candles, period):
    if len(candles) < period + 1:   # we need two candles. Three TRs require four candles, TR1 = candle1 vs candle0, TR 2 = candle2 vs candle1, TR3 = candle3 vs candle2. So we need at least 4 candles to calculate ATR for period 3.
        return None  # Not enough data to calculate ATR

    tr_values = []

    for i in range(1, len(candles)):    # go through the candles starting from the second one, because we always need a previous candle to compare values. "1" is the second candle, "i" stands for "index", but could be anything, like "candle" or "candle_index"
        tr = calculate_true_range(candles[i], candles[i - 1])
        tr_values.append(tr)

    if len(tr_values) < period:
        return None  # Not enough data to calculate ATR

    atr = sum(tr_values[-period:]) / period
    return atr


atr = calculate_atr(candles, period=14)  # Example usage with a period of 14
print("ATR:", atr)