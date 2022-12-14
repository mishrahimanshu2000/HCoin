// SPDX-License-Identifier:MIT

pragma solidity >=0.6.0 <0.9.0;

library SafeMath {
    function multiply(uint256 a, uint256 b) internal pure returns (uint256) {
        if(a==0){
            return 0;
        }
        uint256 c = a*b;
        require(c/a == b);
        return c;
    }

    function divide(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b>0);
        uint256 c=a/b;
        return c;
    }

    function subtract(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b<=a);
        uint256 c = a-b;
        return c;
    }

    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a+b;
        require(c>=a);
        return c;
    }

    function mod(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b!=0);
        return a%b;
    }
}
