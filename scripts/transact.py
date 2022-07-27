from brownie import HCoin, accounts

def main():
    hcoin = HCoin[-1]
    # checking name
    name = hcoin.name.call()
    symbol = hcoin.symbol.call()
    decimal = hcoin.decimal.call()
    print((f"The name is {name} and symbol is {symbol} with decimal of {decimal}"))
    account = accounts.load("My-Rinkeby")
    #total supply
    totalSupply = hcoin.totalSupply()
    # calling balanceOf() function
    balance = hcoin.balanceOf(account)
    print(f"Token {name} have total {totalSupply} supply and account {account} have {balance} balance")
    account2 = "0x94C4B9a68Bc5B0A6a34C09D96628d95271BB34dC"
    transaction = hcoin.transfer(account2, 500, {"from":account})
    print(f"account {account} have {hcoin.balanceOf(account)} and account2 have {hcoin.balanceOf(account2)}")