const formatNumber = num => {
    let str = num.toFixed(2), result = [], strLength;
    for (let i = 0; i < (strLength = str.length - 3); i++) {
        if ((strLength - i) % 3 === 0 && i !== 0) {
            result.push([','] + str[i]);
        } else {
            result.push(str[i]);
        }
    }
    result.push(str.slice(strLength))
    return '$' + result.join('');
}

export default formatNumber;