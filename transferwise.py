def withdraw(wallets, amount, currency, pref_curr):
    temp_wallet = wallets.copy()
    left_amount = 0
    if temp_wallet[currency] >= amount:
        temp_wallet[currency] -= amount
        amount = 0
    elif temp_wallet[currency] < amount:
        left_amount = amount - temp_wallet[currency]
        temp_wallet[currency] = 0.00
        for index, otherCurrency in enumerate(pref_curr):
            exchange_rate_amount = 0
            exchange_rate = getMidMarketRate(currency, otherCurrency)
            exchange_rate_amount = float(left_amount * exchange_rate)
            if temp_wallet[otherCurrency] >= exchange_rate_amount:
                temp_wallet[otherCurrency] -= exchange_rate_amount
                left_amount = 0
                break
            elif temp_wallet[otherCurrency]:
                exchange_rate = getMidMarketRate(otherCurrency, currency)
                exchange_rate_amount = float(temp_wallet[otherCurrency] * exchange_rate)
                left_amount = left_amount - exchange_rate_amount
                temp_wallet[otherCurrency] = 0
    if not left_amount or not amount:
        return temp_wallet
    else:
        return wallets


def change_format(complete_output, wallets):
    output = ''
    for key in complete_output:
        amount = str(round(float(wallets[key]), 3))
        if wallets[key] or wallets[key] != 0.0:
            if len(amount.split('.')[1]) == 3:
                if float(amount[-1]) > 0:
                    amount = amount[:-2] + str(int(amount[-2]) + 1)
                amount = str(round(float(amount), 2))
            if len(amount.split('.')[1]) < 3:
                if amount[-1] == '0':
                    print(amount)
                    amount += '0'
            if output:
                output += ', '
            output += amount + ' ' + key
    return output


def printBalances(requests):
    complete_output = []
    wallets = {i: 0 for i in ["USD", "EUR", "GBP"]}
    for query in requests:
        query_split = query.split(',')
        query_type = query_split[0]
        query_curr = query_split[2]
        query_amount = float(query_split[1])
        if query_curr not in complete_output:
            complete_output.append(query_curr)
        if query_type == 'DEPOSIT':
            wallets[query_curr] += query_amount
        elif query_type == 'WITHDRAW':
            pref_curr = [i for i in ["USD", "EUR", "GBP"] if i != query_curr]
            wallets = withdraw(wallets, query_amount, query_curr, pref_curr)
    return change_format(complete_output, wallets)


def checkDetailsAreValid(accountNumber, bankCode):
    # Write your code here
    # validation for accountNumber
    print(accountNumber)
    print(bankCode)
    if " " in accountNumber:
        accountNumber = accountNumber.replace(" ", "")
    if " " in bankCode:
        bankCode = bankCode.replace(" ", "")
    # print(accountNumber)
    acc_arr = accountNumber.split("-")
    if not str(acc_arr[0]).isdigit() or len(acc_arr[1]) != 7 or len(acc_arr[0]) > 2 or (
    "".join(bankCode[0:2])).isdigit():
        return ""
    weights = {0: 7, 1: 3, 2: 1, 3: 5, 4: 2, 5: 4, 6: 8, 7: 6, 8: 1, 9: 6, 10: 5}
    uppercase = {v: i + 10 for i, v in enumerate(ascii_uppercase)}

    step_1 = accountNumber + bankCode
    step_2 = step_1[(step_1.index("-") + 1):len(step_1)]
    out = 0
    for i, val in enumerate(step_2):
        if val.isdigit():
            out += weights[i] * int(val)
        else:
            print(str(val) + " : " + str(uppercase[val]))
            out += weights[i] * uppercase[val]
    print(out)
    if out % 2 == 0:
        out = out % 89
    else:
        out = out % 89
        out -= 89
    return str(abs(out))

    print(step_2)