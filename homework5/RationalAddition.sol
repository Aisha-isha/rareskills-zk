// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

struct ECPoint {
        uint256 x;
        uint256 y;
    }
contract RationalAddition {
    uint256 constant p = 21888242871839275222246405745257275088548364400416034343698204186575808495617;
    
    function modExp(uint256 base, uint256 exp, uint256 mod) public view returns (uint256) {
        bytes memory input = abi.encode(32, 32, 32, base, exp, mod);
        (bool success, bytes memory data) = address(5).staticcall(input);
        require(success, "modExp failed");
        return abi.decode(data, (uint256));
    }

    function ecAdd(ECPoint memory a, ECPoint memory b) internal view returns (ECPoint memory r) {
        (bool success, bytes memory result) = address(6).staticcall(abi.encodePacked(a.x, a.y, b.x, b.y));
        require(success, "ecAdd failed");
        (r.x, r.y) = abi.decode(result, (uint256, uint256));
    }

    function ecMul(ECPoint memory point, uint256 scalar) internal view returns (ECPoint memory r) {
        (bool success, bytes memory result) = address(7).staticcall(abi.encodePacked(point.x, point.y, scalar));
        require(success, "ecMul failed");
        (r.x, r.y) = abi.decode(result, (uint256, uint256));
    }

    function rationalAdd(ECPoint calldata A, ECPoint calldata B, uint256 num, uint256 den) public view returns (bool verified) {
        ECPoint memory C = ecAdd(A,B);
        uint256 invDen = modExp(den, p-2, p);
        uint256 scalar = mulmod(num, invDen, p);
        ECPoint memory G = ECPoint(1, 2);
        ECPoint memory expected = ecMul(G, scalar);
        return (C.x == expected.x && C.y == expected.y);
    }
}