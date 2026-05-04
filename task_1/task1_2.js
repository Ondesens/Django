function manyChecks() {
    let a = Math.floor(Math.random() * 20) + 1;
    console.log(`a = ${a}`);
    let  result1, result2, result3;

    if ( a > 10 ) {
        result1 = 'a is bigger than 10'
    }
    else {
        result1 = 'a is less than or equal to 10 '
    }
    if (a === 5) {
        result1 +=  'an example of a special case'
    }
    if (a === 15) {
        result1 += 'but a is not 15'
    }
    if (a > 5) {
        result1 += 'and a is greater than 5'
    }
    else {
        result1 += 'and a is less than or equal to 5 '
    }
    if (a % 2) {
        result1 += ' and a is odd'
    }
    else {
        result1 += ' and a is even '
    }



    // switch
    switch (true){
        case a > 10 :
            result2 = 'a is bigger than 10'
            break;
        default:
            result2 = 'a is less than or equal to 10 '
    }
    switch (true) {
        case a === 5 :
            result2 += 'an example of a special case';
            break;
        default:
            result2 += ''
    }
    switch (true) {
        case a === 15 :
            result2 += 'but a is not 15'
            break;
    }
    switch (true) {
        case a > 5 :
            result2 += 'and a is greater than 5'
            break;
        default:
            result2 += 'and a is less than or equal to 5 '
    }
    switch (true){
        case (a % 2 === 1) :
            result2 += ' and a is odd'
            break;
        default:
            result2 += ' and a is even '
    }
    console.log(a%2)

    result3 = (a > 10 ? 'a is bigger than 10' : 'a is less than or equal to 10 ' + (a === 5 ? 'an example of a special case' : '')) + (a === 15 ? 'but a is not 15' : '')+
    (a > 5 ? 'and a is greater than 5' : 'and a is less than or equal to 5 ') + (a % 2 ? ' and a is odd' : ' and a is even ');
    return{
        ifElseResult : result1,
        switchResult : result2,
        terResult : result3
    };
}


console.log(manyChecks())

// условие с условным (тернарным) оператором перевести в if...else И switch()
// результат выводить в консоль, с пощью console.log()

