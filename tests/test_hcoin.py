from brownie import HCoin, accounts
from scripts.deploy import deploy_HCoin
from web3 import Web3


# Writting unit tests


# testing token name
def test_name():
    deploy_HCoin()
    hcoin = HCoin[-1]
    # checking name
    name = hcoin.name.call()
    assert name == "HCoin"


# token symbol
def test_symbol():
    hcoin = HCoin[-1]
    # checking symbol
    sym = hcoin.symbol.call()
    assert sym == "HCN"


# decimal value of token
def test_decimal():
    hcoin = HCoin[-1]
    dec = hcoin.decimal.call()
    assert dec == 18


# testing balanceOf() and totalSupply() function
def test_balanceOfAndTotalSupply():
    hcoin = HCoin[-1]
    initialSupply = 100000
    # calling totalSupply() function
    totalSupply = hcoin.totalSupply()
    # calling balanceOf() function
    balance = hcoin.balanceOf(accounts[0])
    assert balance == initialSupply and totalSupply == initialSupply

# checking transfer() function
def test_transfer():
    hcoin = HCoin[-1]
    toAccount = accounts[1]
    initialSenderBalance = hcoin.balanceOf(accounts[0])
    transfered = hcoin.transfer(toAccount, 100)
    receiverBalance = hcoin.balanceOf(toAccount)
    finalSenderBalance = hcoin.balanceOf(accounts[0])
    assert receiverBalance == 100 and finalSenderBalance == initialSenderBalance-receiverBalance
