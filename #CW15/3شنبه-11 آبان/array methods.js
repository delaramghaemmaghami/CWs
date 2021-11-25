// Create some arrays
const numbers = [0,1,2,3,4,5,6,7,8];

const numbers2 = new Array(22,5, 45,3, 33,76,54, 300, 301);

const fruit = ['Apple', 'Orange',  'Banana','Pear', 'apple'];

const mixed = [22, 'Hello', true, undefined, null, {a:1, b:1}, new Date()];

// console.log(mixed);

let val;

// Get array length
// val = numbers.length;

// console.log(val);

// // // Check if is array
// // val = Array.isArray(numbers);
// // val = Array.isArray({a:1, b:2});

// // console.log(val);


// // // Get single value
// val = numbers[3];

// console.log(val);


// // // Insert into array
// numbers[2] = 100;

// console.log(numbers);


// // Find index of value
// val = numbers.indexOf(5);

// console.log(val);


// MUTATING ARRAYS
// Add on to end
// numbers.push(250);
// console.log(numbers);

//  Add on to front
// numbers.unshift(120);
// console.log(numbers);

// //  Take off from end
// numbers.pop();
// console.log(numbers);

// //  Take off from front
// numbers.shift();
// console.log(numbers);

// numbers.shift();
// console.log(numbers);

// console.clear()
// Splice values
// numbers.splice(1,3);
// console.log(numbers);


// // Reverse
// numbers.reverse();
// console.log(numbers);

// Concatenate array
val = numbers.concat(numbers2);

console.log(val);

// Sorting arrays
val = fruit.sort();
console.log(val);

val = numbers2.sort();
console.log(val);


val = numbers2.sort(function(x, y){
    return x-y;
});
console.log(val);