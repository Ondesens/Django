let a = Math.floor(Math.random() * 100);
console.log('a =',a);
console.log("условие с условным (тернарным) оператором: ",(a > 10 ? a : a * 2) > 5 ? (2 * a) + 1 : (a < 3 ? 1 : 2 * (a - 2)) > 4 ? 5 : (a % 2 === 0 ? 6 : 7));

// условие с условным (тернарным) оператором перевести в if...else И switch()
// результат выводить в консоль, с пощью console.log()

// if...else
if (a > 10 ) {
    result = a
}
else {
    result = a * 2
}
if (result > 5 ) {
    result = (2 * a) + 1
}
else {
    if (a<3){
        result = 1
    }
    else {
        result = 2 * (a - 2)
    }
    if (result > 4) {
        result = (2 * a) + 1
    }
    else {
        if (a % 2 === 0) {
            result = 6
        }
        else {
            result = 7
        }
    }
}
console.log("if...else: ", result);

//switch()
switch (true) {
    case(a>10):
        result = a
        break;
    default:
        result = a * 2
        break;
}

switch (true) {
    case( result > 5 ):
        result = (2 * a) + 1
        break;
    case (a < 3) :
        result = 1
        break;
    default:
        result = 2 * (a - 2)
        switch (true) {
            case( result > 4):
                result = 5
                break;
            default:
                switch (true) {
                    case(a % 2 === 0):
                        result = 6
                        break;
                    default:
                        result = 7
                        break;
                }
    }
}
console.log("switch() =  ", result);

