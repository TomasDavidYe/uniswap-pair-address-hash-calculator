## Motivation
If you are building a Python application that integrates with the DeFi platform [**Uniswap**](https://uniswap.org/), you have probably encountered the problem that given 2 token addresses, you cannot query the ETH blockchain for their reserves if you do not have their pair address.

This pair address is computed deterministically and the Solidity code for this computation can be found [**here**](https://github.com/Uniswap/uniswap-v2-periphery/blob/master/contracts/libraries/UniswapV2Library.sol#L17-L26). The tricky part is how to transform this Solidity code into Python. Unfortunately, it is not as straightforward as one would hope.  

Well, fortunately for you my friend, we have spent 2 sleepless nights trying to figure this out so that you do not have to do the same.
Just use our [**HashService**](HashService.py) and get all the pair addresses you need.
You are welcome :)


## How can you use this package
Just instantiate the HashService from a factory method and start hashing tokens to pair addresses:

```python
import HashService
tokenA = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'  # WETH
tokenB = '0x6B175474E89094C44Da98b954EedeAC495271d0F'  # DAI
pair = HashService.for_uniswap().calculate_pair_adress(
    tokenA=tokenA,
    tokenB=tokenB
)[0]
print(pair)  # 0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11
```

For more examples, please check the [**HashServiceTest.py**](HashServiceTest.py) file.

## Contribute
Right now, we only have factories for [**UniSwap**](https://uniswap.org/) on the ETH chain and [**PancakeSwap**](https://pancakeswap.finance/) on the Binance Smart Chain. If you are missing a factory for, say SushiSwap, feel free to add it here so that the rest of the community can benefit from your effort. 




## Authors
- [**Kirill Pyzhyanov**](https://www.linkedin.com/in/kirill-pyzhyanov-936b43b6/)
- [**Tomas Ye**](https://www.linkedin.com/in/tomas-ye/)
