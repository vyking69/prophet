import boa

w = boa.env.eoa

token = boa.load("./contracts/Token.vy")
nft = boa.load("./contracts/NFT.vy", token.address) 

nft.mint(w)
nft.idToOwner(0)
nft.balanceOf(w)
nft.totalSupply()

nft.burn(0)
nft.idToOwner(0)
nft.balanceOf(w)
nft.totalSupply()

