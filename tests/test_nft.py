import boa
import pytest

@pytest.mark.mint_and_burn
def test_simple_mint_and_burn(nft_env_values):
    w = nft_env_values[0]
    nft = nft_env_values[2]

    assert nft.balanceOf(w) == 0, "initial wallet has an NFT before mint"
    assert (
        nft.idToOwner(0) == "0x0000000000000000000000000000000000000000"
    ), "unminted NFT does not belong to 0x0 address"
    assert nft.totalSupply() == 0, "NFT starting with supply greater then 0"
    assert nft.next_id() == 0, "initial token counter value failure"

    # mint first NFT
    nft.mint(w)

    assert nft.balanceOf(w) == 1, "only one NFT should be minted to wallet w"
    assert nft.idToOwner(0) == w, "owner of first NFT not wallet w"
    assert (
        nft.totalSupply() == 1
    ), "only one NFT has been minted--something went wrong with the count"
    assert nft.next_id() == 1, "counter broke or something went wrong with tracking token id"

    # mint second NFT
    nft.mint(w)

    assert nft.balanceOf(w) == 2, "only two NFTs should be minted to wallet w"
    assert nft.idToOwner(1) == w, "owner of second NFT not wallet w"
    assert (
        nft.totalSupply() == 2
    ), "only two NFTs has been minted--something went wrong with the count"
    assert nft.next_id() == 2, "counter broke or something went wrong with tracking token id"

    nft.burn(0)
    assert (
        nft.balanceOf(w) == 1
    ), "only one NFT should be minted to wallet w after burning one NFT"
    assert (
        nft.idToOwner(0) == "0x0000000000000000000000000000000000000000"
    ), "burned NFT does not belong to 0x0 address"
    assert (
        nft.totalSupply() == 1
    ), "should be 1 NFT since two minted and one burned--something went wrong with the count"
    assert nft.next_id() == 2, "counter broke or something went wrong with tracking token id"

    # mint third NFT
    nft.mint(w)

    assert (
        nft.balanceOf(w) == 2
    ), "only two NFTs should be minted to wallet w since three minted and one burned"
    assert nft.idToOwner(2) == w, "owner of third NFT not wallet w"
    assert (
        nft.totalSupply() == 2
    ), "only three NFTs has been minted and one burned--something went wrong with the count"
    assert nft.next_id() == 3, "counter broke or something went wrong with tracking token id"

    # mint and burning sequence NFT
    nft.mint(w)  # mint NFT with ID 3
    nft.mint(w)  # mint NFT with ID 4
    nft.burn(4)  # burn NFT with ID 4

    assert (
        nft.balanceOf(w) == 3
    ), "only three NFTs should be minted to wallet w since five minted and two burned"
    assert nft.idToOwner(3) == w, "owner of fourth NFT not wallet w"
    assert (
        nft.idToOwner(4) == "0x0000000000000000000000000000000000000000"
    ), "burned NFT does not belong to 0x0 address"
    assert (
        nft.totalSupply() == 3
    ), "only three NFTs has been minted and one burned--something went wrong with the count"
    assert nft.next_id() == 5, "counter broke or something went wrong with tracking token id"

@pytest.mark.mint_and_burn
def test_n_burn(nft_env_values):
    w = nft_env_values[0]
    nft = nft_env_values[2]

    # number of mints and burns to test
    n = 100

    # reference number to track supply against
    initial_supply = nft.totalSupply()

    # start interval range from next_id
    # mint n nfts, with i also representing tokenID
    for i in range(nft.next_id(), n):
        nft.mint(w)
    
        # assert checks
        assert nft.totalSupply() == initial_supply + i + 1, "total supply does not match n"
        assert nft.balanceOf(w) == initial_supply + i + 1, "wallet w does not have balance that matches n"
        assert nft.idToOwner(i) == w, "latest minted nft doesn't belong to wallet w"
        assert nft.next_id() == initial_supply + i + 1, "token ID tracker broke"

    # burn n nfts
    for i in range(nft.next_id(), nft.next_id() - n + 1, -1):
        previous_supply = nft.totalSupply()
        previous_balance = nft.balanceOf(w)
        nft.burn(i-1)

        # assert checks
        assert nft.totalSupply() == previous_supply - 1, "total supply does not match n"
        assert nft.balanceOf(w) == previous_balance - 1, "wallet w does not have balance that matches n"
        assert nft.idToOwner(i) == "0x0000000000000000000000000000000000000000", "latest minted nft doesn't belong to zero address"
        assert nft.next_id() == n, "id tracking should not change during burn operations"

    

    # assert check
    assert 1 == 1

@pytest.mark.burn
@pytest.mark.xfail(reason="Expected failure burning an NFT before mint")
def test_burning_an_nft_before_mint(nft_env_values):
    nft = nft_env_values[2]

    # burn the NFT before mint
    nft.burn(0)

@pytest.mark.burn
@pytest.mark.xfail(reason="Expected failure due to burning a burned NFT")
def test_burning_a_burned_nft(nft_env_values):
    w = nft_env_values[0]
    nft = nft_env_values[2]

    # mint one NFT
    nft.mint(w)

    # burn the same NFT twice
    nft.burn(0)
    nft.burn(0)

@pytest.mark.level_up
def test_simple_level_up(nft_env_values):
    w = nft_env_values[0]
    nft = nft_env_values[2]

    working_token_id = nft.next_id()

    nft.mint(w)

    assert nft.see_nft_tier(working_token_id) == 1, "newly minted NFT not tier 1"

    nft.sample_tier_up(working_token_id)
    
    assert nft.see_nft_tier(working_token_id) == 2, "NFT did not level up to tier 2"




@pytest.mark.level_up
@pytest.mark.skip
def test_level_up(nft_env_values):
    w = nft_env_values[0]
    token = nft_env_values[1]
    nft = nft_env_values[2]

    print(w)
    print(boa.env.eoa)
    print(nft.address)
    
    # TODO - figure out if we should be using prank or creating new wallets here and elsewhere?

    # track a freshly minted nft
    latest_nft = nft.next_id()

    # mint the nft
    nft.mint(w)

    # add tokens to w for level up operation
    token.mint(w, 100000)

    # attempt to level up the latest nft
    nft.level_up(latest_nft)