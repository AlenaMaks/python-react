function manyChecks() {
  let a = Math.floor(Math.random() * 20) + 1;
  console.log(`a = ${a}`);

  let result = ''
  if (a > 10) result += 'a is bigger than 10'
  else result += 'a is less than or equal to 10 '

  if (a === 5) result += 'an example of a special case'
  else result += ''

  if (a === 15) result += 'but a is not 15'
  else result += ''

  if (a > 5) result += 'and a is greater than 5'
  else result += 'and a is less than or equal to 5 '
  
  if (a % 2) result += ' and a is odd'
  else result += ' and a is even '

  return (result)
}

console.log(manyChecks());

// (a > 10 ? 'a is bigger than 10' : 'a is less than or equal to 10 ' 
// + (a === 5 ? 'an example of a special case' : '')) 
// + (a === 15 ? 'but a is not 15' : '') 
// + (a > 5 ? 'and a is greater than 5' : 'and a is less than or equal to 5 ') 
// + (a % 2 ? ' and a is odd' : ' and a is even ');