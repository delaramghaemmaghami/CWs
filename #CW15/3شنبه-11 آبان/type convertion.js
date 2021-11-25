let val;

// Number to string

val = String(555);
// console.log(val);
// console.log(typeof val);
// console.log(val.length);

// x = 1+2+"3"+4+5
// console.log(x);

val = String(4+4);
// console.log(val);
// console.log(typeof val);
// console.log(val.length);


// // Bool to string
val = String(true);
// console.log(val);
// console.log(typeof val);
// console.log(val.length);

// // Date to string
val = String(new Date());
// console.log(val);
// console.log(typeof val);
// console.log(val.length);



// Array to string
val = String([1,2,3,4]);
// console.log(val);
console.log(typeof val);
// console.log(val.length);
)

// toString()
val = (5).toString();
// console.log(val);
// console.log(typeof val);
// console.log(val.length);



val = (true).toString();
// console.log(val);
// console.log(typeof val);
// console.log(val.length);

val = ({1:2, 2:3}).toString();
val = ([1,3]).toString();
// console.log(val);
// console.log(typeof val);
// console.log(val.length);

// console.log("====================");

// // String to number
// val = Number('5');
// console.log(val);
// console.log(typeof val);



// val = Number(true);
// console.log(val);
// console.log(typeof val);



val = Number(false);
console.log(val);
console.log(typeof val);



val = Number(null);
// console.log(val);
// console.log(typeof val);




// console.log("====================");


// val = Number('he5llo');
// console.log(val);
// console.log(typeof val);


// val = Number([1,2,3]);
// console.log(val);
// console.log(typeof val);


val = parseInt('100.30');
// console.log(val);
// console.log(typeof val);

test = "100.34"
counter = 10
sum = Number(test) + counter 
sum = parseFloat(test) + counter 
console.log(sum)

// val = parseFloat('100.300000010000');
// console.log(val);
// console.log(typeof val);
// console.log(val.toFixed());
