from brownie import accounts, network

def getAccount():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.load("My-Rinkby")
