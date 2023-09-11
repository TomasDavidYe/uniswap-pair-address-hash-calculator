import unittest
from web3 import Web3

from HashService import HashService


class HashServiceTest(unittest.TestCase):

    def test_uniswap_weth_dai_pair_address(self):
        # WETH -> https://etherscan.io/address/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
        tokenA = Web3.to_checksum_address('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')

        # DAI -> https://etherscan.io/address/0x6B175474E89094C44Da98b954EedeAC495271d0F
        tokenB = Web3.to_checksum_address('0x6B175474E89094C44Da98b954EedeAC495271d0F')

        # (WETH, DAI) -> https://etherscan.io/address/0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11
        expected_pair_address = Web3.to_checksum_address('0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11')

        actual_pair_address = HashService.for_uniswap().calculate_pair_adress(
            tokenA=tokenA,
            tokenB=tokenB
        )[0]

        self.assertEqual(expected_pair_address, actual_pair_address, 'DAI vs WETH assertion failed')

    def test_uniswap_weth_wbtc_pair_address(self):
        # WETH -> https://etherscan.io/address/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
        tokenA = Web3.to_checksum_address('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')

        # WBTC -> https://etherscan.io/address/0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599
        tokenB = Web3.to_checksum_address('0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599')

        # (WETH, WBTC) -> https://etherscan.io/address/0xBb2b8038a1640196FbE3e38816F3e67Cba72D940
        expected_pair_address = Web3.to_checksum_address('0xBb2b8038a1640196FbE3e38816F3e67Cba72D940')

        actual_pair_address = HashService.for_uniswap().calculate_pair_adress(
            tokenA=tokenA,
            tokenB=tokenB
        )[0]

        self.assertEqual(expected_pair_address, actual_pair_address, 'WBTC vs WETH')

    def test_uniswap_weth_meowl_pair_address(self):
        # WETH -> https://etherscan.io/address/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
        tokenA = Web3.to_checksum_address('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')

        # MEOWL -> https://etherscan.io/address/0x1F1F26C966F483997728bEd0F9814938b2B5E294
        tokenB = Web3.to_checksum_address('0x1F1F26C966F483997728bEd0F9814938b2B5E294')

        # (WETH, WBTC) -> https://etherscan.io/address/0xBb2b8038a1640196FbE3e38816F3e67Cba72D940
        expected_pair_address = Web3.to_checksum_address('0x31B5bd644182502C27a0F1c99D5E47d7841Fad3c')

        actual_pair_address = HashService.for_uniswap().calculate_pair_adress(
            tokenA=tokenA,
            tokenB=tokenB
        )[0]

        self.assertEqual(expected_pair_address, actual_pair_address, 'WBTC vs WETH')


    def test_uniswap_usdc_occ_pair_address(self):
        # USDC -> https://etherscan.io/address/0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
        tokenA = Web3.to_checksum_address('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')

        # OCC -> https://etherscan.io/address/0x2F109021aFe75B949429fe30523Ee7C0D5B27207
        tokenB = Web3.to_checksum_address('0x2F109021aFe75B949429fe30523Ee7C0D5B27207')

        # (USDC, OCC) -> https://etherscan.io/address/0xEdF1fA564a91a5664f172470C47450af17724757
        expected_pair_address = Web3.to_checksum_address('0xEdF1fA564a91a5664f172470C47450af17724757')

        actual_pair_address = HashService.for_uniswap().calculate_pair_adress(
            tokenA=tokenA,
            tokenB=tokenB
        )[0]

        self.assertEqual(expected_pair_address, actual_pair_address, 'OCC vs USDC')        

    def test_pancake_swap_wbnb_laika_pair_address(self):
        # WBNB -> https://bscscan.com/address/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c
        tokenA = Web3.to_checksum_address('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')

        # LAIKA -> https://bscscan.com/address/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c
        tokenB = Web3.to_checksum_address('0x270877FBDAdd2E28C7EAf08e528691B95684207e')

        # (WBNB, LAIKA) -> https://bscscan.com/address/0x90070E7a97fF3d52E5C6CaC49123562d266921B9
        expected_pair_address = Web3.to_checksum_address('0x90070E7a97fF3d52E5C6CaC49123562d266921B9')

        actual_pair_address = HashService.for_pancake_swap().calculate_pair_adress(
            tokenA=tokenA,
            tokenB=tokenB
        )[0]

        self.assertEqual(expected_pair_address, actual_pair_address, 'WBNB vs LAIKA assertion failed')

    def test_pancake_swap_wbnb_autocoin_pair_address(self):
        # WBNB -> https://bscscan.com/address/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c
        tokenA = Web3.to_checksum_address('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')

        # AutoCoin -> https://bscscan.com/address/0x47b80b600d5e4d2a6c2e1bda0e2d460ef6689850
        tokenB = Web3.to_checksum_address('0x47b80b600d5e4d2a6c2e1bda0e2d460ef6689850')

        # (WBNB, AutoCoin) -> https://bscscan.com/address/0xd69ef9bf1e6ace24b2968acd42d2cf50504af800
        expected_pair_address = Web3.to_checksum_address('0xd69ef9bf1e6ace24b2968acd42d2cf50504af800')

        actual_pair_address = HashService.for_pancake_swap().calculate_pair_adress(
            tokenA=tokenA,
            tokenB=tokenB
        )[0]

        self.assertEqual(expected_pair_address, actual_pair_address, 'WBNB vs AUTOCOIN assertion failed')

    def test_pancake_swap_wbnb_safemoon_pair_address(self):
        # WBNB -> https://bscscan.com/address/0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c
        tokenA = Web3.to_checksum_address('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')

        # SafeMoon -> https://bscscan.com/address/0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3
        tokenB = Web3.to_checksum_address('0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3')  # SafeMoon

        # (WBNB, SafeMoon) -> https://bscscan.com/address/0x9adc6Fb78CEFA07E13E9294F150C1E8C1Dd566c0
        expected_pair_address = Web3.to_checksum_address('0x9adc6Fb78CEFA07E13E9294F150C1E8C1Dd566c0')

        actual_pair_address = HashService.for_pancake_swap().calculate_pair_adress(
            tokenA=tokenA,
            tokenB=tokenB
        )[0]

        self.assertEqual(expected_pair_address, actual_pair_address, 'WBNB vs SafeCoin assertion failed')


if __name__ == '__main__':
    unittest.main()
