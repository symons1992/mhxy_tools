# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def calc(n, level):
    original_n = n
    i = 0
    while i < level:
        n = n * 0.98 - 5
        i = i + 1
    print(f"原始伤害： {original_n}, 抗等级: {level}, 伤害:{n}".format({
        "original_n": original_n,
        "n": n,
        "level": level,
    }))
    return n

def calc_attack(n, level):
    original_n = n
    i = 0
    while i < level:
        n = n * 1.02 + 5
        i = i + 1
    print(f"原是伤害: {original_n}, 修炼等级: {level}, 最终伤害: {n}".format({
        "original_n": original_n,
        "n": n,
        "level": level,
    }))
    return n

def calc_cost_of_num(n):
    number = n / 150
    day = number / 10
    money = number * 94
    rmb = money * 0.0582

    print(f"需要提升的修炼点数：{n}\n需要购买的果子: {number}\n需要花费的游戏币: {money}\n需要充值的RMB：{rmb}\n达成的天数: {day}\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #calc_attack(1000, 17)
    #calc_attack(2000, 20)
    #calc_attack(2000, 25)
    #calc_attack(2000, 7)

    calc_cost_of_num(24310)
    #calc_cost_of_num(67750 * 2 + 30550 + 50100)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


