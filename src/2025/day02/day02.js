const fs = require('node:fs');

function parseRanges() {
    let data = fs.readFileSync('input.txt', 'utf8')
    splits = data.split(',');
    return splits.map(range => range.split('-').map(Number));
}

function part1() {
    let ranges = parseRanges();
    let sum = 0;

    for (range of ranges) {
        for (let id = range[0]; id <= range[1]; id++) {
            let str = String(id)
            
            if (str.slice(0, Number(str.length / 2)) == str.slice(Number(str.length / 2))) {
                sum += id;
            }
            
        }
    }
    console.log('Sum1:', sum);
}

function isInvalidId(id) {
    let str = String(id);
    for (let n = 2; n <= str.length; n++) {
        if (str.length % n == 0) {
            let size = str.length / n;
            let slices = Array();

            for (let i = 0; i < str.length; i += size) {
                slices.push(str.slice(i, i + size));
            }
            if (slices.every(slice => slice === slices[0])) {
                return true;
            }
        }
    }
    return false;
}

function part2() {
    let ranges = parseRanges();
    let sum = 0;

    for (range of ranges) {
        for (let id = range[0]; id <= range[1]; id++) {
            if (isInvalidId(id)) {
                sum += id;
            }

        }
    }
    console.log('Sum2:', sum)
}

function main(){
    part1();
    part2();
}

main();