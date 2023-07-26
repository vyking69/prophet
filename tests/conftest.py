import pytest
import boa

@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def receiver(accounts):
    return accounts[1]


@pytest.fixture(scope="session")
def nft(owner, project):
    return owner.deploy(project.NFT)

@pytest.fixture()
def nft_env_values():
    w = boa.env.eoa
    token = boa.load("./contracts/Token.vy")
    nft = boa.load("./contracts/NFT.vy", token.address) 
    return [w, token, nft]