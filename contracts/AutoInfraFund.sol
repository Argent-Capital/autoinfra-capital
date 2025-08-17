// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AutoInfraFund {
    address public manager;
    mapping(address => uint256) public investments;
    uint256 public totalCapital;

    event Invest(address indexed investor, uint256 amount);
    event Distribute(address indexed investor, uint256 amount);

    constructor() {
        manager = msg.sender;
    }

    function invest() external payable {
        require(msg.value > 0, "Zero");
        investments[msg.sender] += msg.value;
        totalCapital += msg.value;
        emit Invest(msg.sender, msg.value);
    }

    function distribute(address payable investor, uint256 amount) external {
        require(msg.sender == manager, "Only manager");
        require(address(this).balance >= amount, "Insufficient");
        (bool ok, ) = investor.call{value: amount}("");
        require(ok, "Transfer failed");
        emit Distribute(investor, amount);
    }
}
