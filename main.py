import copy
import math

def fee(check):
    _fee = 20 if math.floor(buy*1.425) <= 20 \
                 else math.floor(buy*1.425)
    return _fee

if __name__ == '__main__':
    while(True):
        sell = buy = float(input("購買金額 : "))
        buy_fee = fee(buy)
        tick = float(input("金額跳動 : "))
        want = float(input("想賺多少 : "))

        while(True):
            sell += tick
            sell_fee = fee(sell)
            tax = sell * 3
            earn = (sell * 1000) - (buy * 1000) - buy_fee - sell_fee \
                    - tax
            if earn > want: break

        print("不虧的情況 : 賣價 = %.2f"%sell)
        print("手續費&稅額 : %d"%(sell_fee+buy_fee+tax))
        print("淨賺 : %d"%earn)

        if input("是否繼續(Y/N)") == 'N':
            break