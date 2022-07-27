from brownie import HCoin
from  web3 import Web3

from scripts.helper import getAccount

def main():
    deploy_HCoin()

def deploy_HCoin():
    account = getAccount()
    initialSupply = Web3.toWei(1000000, "ether")
    hcoin = HCoin.deploy(initialSupply,{"from" : account})
    return hcoin