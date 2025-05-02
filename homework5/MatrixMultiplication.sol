// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MatrixMultiplication {

    struct ECPoint {
            uint256 x;
            uint256 y;
    }
    function ecEq(ECPoint memory p1, ECPoint memory p2) internal pure returns (bool) {
        return (p1.x == p2.x && p1.y == p2.y);
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
    function generator() internal pure returns (ECPoint memory) {
        return ECPoint(1, 2);
    }
    function matmul(uint256[] calldata matrix, uint256 n, ECPoint[] calldata s, uint256[] calldata o) public view returns (bool verified) {
        require(matrix.length == n * n, "Matrix size mismatch");
        require(s.length == n, "Vector s size mismatch");
        require(o.length == n, "Vector o size mismatch");

        for (uint256 i = 0; i < n; i++) {
            ECPoint memory acc = ECPoint(0, 0);

            for (uint256 j = 0; j < n; j++) {
                uint256 coeff = matrix[i * n + j];
                ECPoint memory term = ecMul(s[j], coeff);
                acc = ecAdd(acc, term);
            }

            ECPoint memory expected = ecMul(generator(), o[i]);

            if (!ecEq(acc, expected)) {
                return false; 
            }
        }

        return true; 
    }
}
