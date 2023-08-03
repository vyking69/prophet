import boa
import pytest

@pytest.mark.level_up
def test_level_up(nft_env_values):
    w = nft_env_values[0]
    token = nft_env_values[1]
    nft = nft_env_values[2]

    # TODO - figure out if we should be using prank or creating new wallets here and elsewhere?

    # track a freshly minted nft, remember it's next_id() - 1
    latest_nft = nft.next_id()

    # mint the nft
    nft.mint(w)

    # add tokens to w for level up operation
    previous_token_amount = token.see_balance_of(w)
    tokens_needed_for_level_up = 10
    token.mint(w, tokens_needed_for_level_up)

    assert token.see_balance_of(w) == previous_token_amount + tokens_needed_for_level_up, "tokens added doesn't match expectations"

    # begin level up process
    token.trigger_level_up(latest_nft)

    assert token.see_balance_of(w) == previous_token_amount, "amount of tokens burned not matching expectations"




@pytest.mark.burn
def test_burn_attack(nft_env_values):
    # todo use prank to try and burn another wallet's tokens
    assert 1 == 1