function manyChecks() {
  let a = Math.floor(Math.random() * 20) + 1;
  console.log(`a = ${a}`);

  let result = ''

  switch (true) {
    case (a > 10):
      result += 'a is bigger than 10'
      break;
    default:
      result += 'a is less than or equal to 10 '
  }

  switch (true) {
    case (a === 5):
      result += 'an example of a special case'
      break
    default:
      result += ''
  }

  switch (true) {
    case (a === 15):
      result += 'but a is not 15'
      break
    default:
      result += ''
  }

  switch (true) {
    case (a > 5):
      result += 'and a is greater than 5'
      break
    default:
      result += 'and a is less than or equal to 5 '
  }

  switch (true) {
    case (a % 2 === 1):
      result += ' and a is odd'
      break
    default:
      result += ' and a is even '
  }

  return result;
}

console.log(manyChecks());

// (a > 10 ? 'a is bigger than 10' : 'a is less than or equal to 10 ' 
// + (a === 5 ? 'an example of a special case' : '')) 
// + (a === 15 ? 'but a is not 15' : '') 
// + (a > 5 ? 'and a is greater than 5' : 'and a is less than or equal to 5 ') 
// + (a % 2 ? ' and a is odd' : ' and a is even ');