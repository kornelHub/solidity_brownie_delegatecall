from brownie import accounts, A, B

def deployA():
    owner = accounts[0]
    contract = A.deploy({"from": owner})
    return contract

def deployB():
    owner = accounts[0]
    contract = B.deploy({"from": owner})
    return contract

def testDelegateCall():
    onwer = accounts[0]
    contract_a = deployA()
    contract_b = deployB()

    set_vars_tx = contract_a.setVars(
        contract_b.address,
         2137,
        {"from": onwer, "value": 1*10**18})
    set_vars_tx.wait(1)

    print(f"num A: {contract_a.num()}")
    print(f"num A: {contract_a.sender()}")
    print(f"num A: {contract_a.value()}")
    print(f"num B: {contract_b.num()}")
    print(f"num B: {contract_b.num()}")
    print(f"num B: {contract_b.num()}")