// Import the encryptors functions here.
const encryptors = require('./encryptors.js');
const { caesarCipher, symbolCipher, reverseCipher } = encryptors;

const encodeMessage = (str) => {
    return symbolCipher(reverseCipher(caesarCipher(str, 11)));    
}
  
const decodeMessage = (str) => {
    return caesarCipher(reverseCipher(symbolCipher(str)), -11);    
}
  
// User input / output.
  
const handleInput = (userInput) => {
    const str = userInput.toString().trim();
    let output;
    if (process.argv[2] === 'encode') {
      output = encodeMessage(str);
    } 
    if (process.argv[2] === 'decode') {
      output = decodeMessage(str);
    } 
    
    process.stdout.write(output + '\n');
    process.exit();
}
  

process.stdout.write('Enter the message you would like to encrypt...\n> ');
process.stdin.on('data', handleInput);