import boa
import pytest

def test_one(nft_env_values):
    w = nft_env_values[0]
    token = nft_env_values[1]
    nft = nft_env_values[2]

    assert nft.balanceOf(w) == 0, "initial wallet has an NFT before mint"
    assert nft.idToOwner(0) == "0x0000000000000000000000000000000000000000", "unminted NFT does not belong to 0x0 address"
    assert nft.totalSupply() == 0, "NFT starting with supply greater then 0"
    
    # mint first NFT
    nft.mint(w)

    assert nft.balanceOf(w) == 1, "only one NFT should be minted to wallet w"
    assert nft.idToOwner(0) == w, "owner of first NFT not wallet w"
    assert nft.totalSupply() == 1, "only one NFT has been minted--something went wrong with the count"

    # mint second NFT
    nft.mint(w)

    assert nft.balanceOf(w) == 2, "only two NFTs should be minted to wallet w"
    assert nft.idToOwner(1) == w, "owner of second NFT not wallet w"
    assert nft.totalSupply() == 2, "only two NFTs has been minted--something went wrong with the count"

    nft.burn(0)
    assert nft.balanceOf(w) == 1, "only one NFT should be minted to wallet w after burning one NFT"
    assert nft.idToOwner(0) == "0x0000000000000000000000000000000000000000", "burned NFT does not belong to 0x0 address"
    assert nft.totalSupply() == 1, "should be 1 NFT since two minted and one burned--something went wrong with the count"

    # mint third NFT
    nft.mint(w)

    assert nft.balanceOf(w) == 2, "only two NFTs should be minted to wallet w since three minted and one burned"
    assert nft.idToOwner(2) == w, "owner of third NFT not wallet w"
    assert nft.totalSupply() == 2, "only three NFTs has been minted and one burned--something went wrong with the count"

    # mint and burning sequence NFT
    nft.mint(w) # mint NFT with ID 3
    nft.mint(w) # mint NFT with ID 4
    nft.burn(4) # burn NFT with ID 4

    assert nft.balanceOf(w) == 3, "only three NFTs should be minted to wallet w since five minted and two burned"
    assert nft.idToOwner(3) == w, "owner of fourth NFT not wallet w"
    assert nft.idToOwner(4) == "0x0000000000000000000000000000000000000000", "burned NFT does not belong to 0x0 address"
    assert nft.totalSupply() == 3, "only three NFTs has been minted and one burned--something went wrong with the count"


@pytest.mark.xfail(reason="Expected failure burning an NFT before mint")
def test_burning_an_nft_before_mint(nft_env_values):
    nft = nft_env_values[2]

    # burn the NFT before mint
    nft.burn(0)

@pytest.mark.xfail(reason="Expected failure due to burning a burned NFT")
def test_burning_a_burned_nft(nft_env_values):
    w = nft_env_values[0]
    nft = nft_env_values[2]

    # mint one NFT
    nft.mint(w)

    # burn the same NFT twice
    nft.burn(0)
    nft.burn(0)