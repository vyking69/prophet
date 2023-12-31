# @version 0.3.7

from vyper.interfaces import ERC20


implements: ERC20

# ERC20 Token Metadata
NAME: constant(String[20]) = "simple_token"
SYMBOL: constant(String[5]) = "ST1"
DECIMALS: constant(uint8) = 10

# ERC20 State Variables
totalSupply: public(uint256)
balanceOf: public(HashMap[address, uint256])
allowance: public(HashMap[address, HashMap[address, uint256]])

# Events
event Transfer:
    sender: indexed(address)
    receiver: indexed(address)
    amount: uint256

event Approval:
    owner: indexed(address)
    spender: indexed(address)
    amount: uint256

owner: public(address)
isMinter: public(HashMap[address, bool])
_nft_contract_address: public(address)

nonces: public(HashMap[address, uint256])
DOMAIN_SEPARATOR: public(bytes32)
DOMAIN_TYPE_HASH: constant(bytes32) = keccak256('EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)')
PERMIT_TYPE_HASH: constant(bytes32) = keccak256('Permit(address owner,address spender,uint256 value,uint256 nonce,uint256 deadline)')

# Declare the companion token contract interface
interface nft_contract_interface:
    def see_nft_tier(tokenId: uint256) -> uint8: nonpayable
    def level_up(tokenID: uint256) -> bool: nonpayable

# index matches tier - 1, so leveling up a tier 1 to tier 2 costs the price at indext 1 - 1 (index 0)
_tier_upgrade_cost: public(uint256[4])

@external
def __init__(nft_contract_address: address):
    self.owner = msg.sender
    self.totalSupply = 1000
    self.balanceOf[msg.sender] = 1000

    self._nft_contract_address = nft_contract_address

    # TODO - update costs and set it as a passable parameter?
    self._tier_upgrade_cost = [10,100,1000,10000]


    # EIP-712
    self.DOMAIN_SEPARATOR = keccak256(
        concat(
            DOMAIN_TYPE_HASH,
            keccak256(NAME),
            keccak256("1.0"),
            _abi_encode(chain.id, self)
        )
    )


@pure
@external
def name() -> String[20]:
    return NAME


@pure
@external
def symbol() -> String[5]:
    return SYMBOL


@pure
@external
def decimals() -> uint8:
    return DECIMALS

@view
@external
def see_balance_of(account: address) -> uint256:
    return self.balanceOf[account]

@external
def transfer(receiver: address, amount: uint256) -> bool:
    assert receiver not in [empty(address), self]

    self.balanceOf[msg.sender] -= amount
    self.balanceOf[receiver] += amount

    log Transfer(msg.sender, receiver, amount)
    return True


@external
def transferFrom(sender:address, receiver: address, amount: uint256) -> bool:
    assert receiver not in [empty(address), self]

    self.allowance[sender][msg.sender] -= amount
    self.balanceOf[sender] -= amount
    self.balanceOf[receiver] += amount

    log Transfer(sender, receiver, amount)
    return True


@external
def approve(spender: address, amount: uint256) -> bool:
    """
    @param spender The address that will execute on owner behalf.
    @param amount The amount of token to be transfered.
    """
    self.allowance[msg.sender][spender] = amount

    log Approval(msg.sender, spender, amount)
    return True

@internal
def _burn(_amount: uint256, _sender_address: address) -> bool:
    """
    @notice Burns the supplied amount of tokens from the sender wallet.
    @param amount The amount of token to be burned.
    """

    assert self.balanceOf[_sender_address] >= _amount

    self.balanceOf[_sender_address] -= _amount
    self.totalSupply -= _amount

    log Transfer(_sender_address, empty(address), _amount)

    return True

@external
def burn(amount: uint256) -> bool:
    return self._burn(amount, msg.sender)
   

@external
def mint(receiver: address, amount: uint256) -> bool:
    """
    @notice Function to mint tokens
    @param receiver The address that will receive the minted tokens.
    @param amount The amount of tokens to mint.
    @return A boolean that indicates if the operation was successful.
    """
    
    assert msg.sender == self.owner or self.isMinter[msg.sender], "Access is denied."
    assert receiver not in [empty(address), self]

    self.totalSupply += amount
    self.balanceOf[receiver] += amount

    log Transfer(empty(address), receiver, amount)

    return True

@external
def trigger_level_up(tokenId: uint256):
    # get tier of provided NFT
    tier: uint8 = nft_contract_interface(self._nft_contract_address).see_nft_tier(tokenId)

    assert tier >= 1, "NFT not of correct level"
    assert tier < 5, "NFT not of correct level"

    # check reference table for required amount of tokens to level up
    cost_to_level_up: uint256 = self._tier_upgrade_cost[convert(tier, uint256) - 1]
    
    # check if user has enough tokens to burn
    assert self.balanceOf[msg.sender] >= cost_to_level_up, "not enough burnable tokens to level up!"

    # burn tokens
    self._burn(cost_to_level_up, msg.sender)

    nft_contract_interface(self._nft_contract_address).level_up(tokenId)