const { partialDeepStrictEqual } = require('node:assert');
const fs = require('node:fs');

function parseInput() {
    const data = fs.readFileSync('input.txt', 'utf-8');
    const banks = data.split(/\r?\n/);
    return banks;
}

function findLargestPossibleJoltage(bank) {
    let tens = -1;
    let idx = -1;
    let ones = -1;

    for (let i = 0; i < bank.length; i++) {
        if (i < bank.length - 1 && bank[i] > tens) {
            tens = bank[i];
            idx = i;
            ones = -1;
        } else if (bank[i] > ones) {
            ones = bank[i];
        }
    }

    return Number(String(tens) + String(ones));
}

function part1() {
    const banks = parseInput();
    const sum = banks.reduce((total, bank) => total += findLargestPossibleJoltage(bank), 0);
    console.log('Total Joltage Output:', sum);
}

function findNBatteryJoltage(bank, n) {
    let joltage = bank.slice(bank.length-n, bank.length);
    let limit = 0;
    // For each number in joltage
    for (let i = 0; i < n; i++) {
        let maxIdx = bank.length-n+i;
        let max = bank[maxIdx];
        // For each number in bank between the limit and the ith element of joltage (but in bank) in reverse order
        for (let j = bank.length-n+i; j >= limit; j--) {
            if (bank[j] >= max) {
                max = bank[j];
                maxIdx = j;
            }
        }
        limit = maxIdx + 1;
        joltage = joltage.slice(0, i) + max + joltage.slice(i+1, joltage.length);
    }
    return Number(joltage);
}

function part2() {
    const banks = parseInput();
    const sum = banks.reduce((total, bank) => total += findNBatteryJoltage(bank, 12), 0);
    console.log('12-Battery Total Joltage Output:', sum);
}

function main() {
    part1();
    part2();
}

main();