const firstName = 'shideh';
const lastName = 'parsa';
const age = 27;

let val;

val = firstName + lastName;

// console.log(val);

// // Concatenation
// val = firstName + ' ' + lastName;

// console.log(val);

// // Append
val = 'hello ';
val += 'world!';

// console.log(val);

val = 'Hello, my name is ' + firstName + ' and I am ' + age;

// console.log(val);


// // ES6
val = `Hello, my name is ${firstName} and I am ${age} `;

console.log(val);

// Length
val = firstName.length;

// console.log(val);


// concat()
val = firstName.concat('*', lastName, "sdf");

console.log(val);


// // Change case
val = firstName.toUpperCase();

// console.log(val);

val = firstName.toLowerCase();

// console.log(val);


val = firstName[4];  

// console.log(val);

// indexOf()
val = firstName.indexOf('z');

// console.log(val);

// charAt()
// val = firstName.charAt('2');

// console.log(val);


// // Get last char
// val = firstName.charAt(firstName.length - 1);

// console.log(val);




// substring()
// val = firstName.substring(0, 2);

// console.log(val);


// // slice()
// val = firstName.slice(0,2);

// console.log(val);

// split()
// const str = 'Hello my name is shideh';

// val = str.split(' ');

// console.log(val);

// const tags = 'ES6 , web design , web development , programming';

// val = tags.split(',');

// console.log(val);

// replace()
// val = str.replace('shideh', 'raha');

// console.log(val);


// includes()
// val = str.includes('shidehasd');

// console.log(val);