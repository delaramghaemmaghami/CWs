// if(something) {
//   do something
// } else {
//   do something else
// }

// const id;

let id;
id =  23
// EQUAL TO
if(id == 60){
  console.log('Yes');
} else {
  console.log('No');
}

// // NOT EQUAL TO
// if(id != 62){
//   console.log('Yes');
// } else {
//   console.log('No');
// }

// // EQUAL TO VALUE & TYPE
// if(id === "60"){
//   console.log('Yes');
// } else {
//   console.log('No');
// }


// // No EQUAL TO VALUE & TYPE
// if(id !== 60){
//   console.log('Yes');
// } else {
//   console.log('No');
// }


// Test if undefined
// if(typeof id !== 'undefined'){
//   console.log(`The ID is ${id}`);
// } else {
//   console.log('NO ID');
// }



// IF ELSE

const color = 'blue';

if(color === 'red'){
  console.log('Color is red');
} 
else if(color === 'blue'){
  console.log('Color is blue');
} else {
  console.log('Color is not red or blue');
}

// LOGICAL OPERATORS

const age = 5;

// AND &&
if(age > 0  && age < 12){
  console.log('If');
} else if(age >= 13 && age <= 19){
  console.log('Else If');
} else {
  console.log('Else');
}

// // OR ||
if(age < 16 || age > 65){
  console.log('Yes');
} else {
  console.log('No');
}

// id = 60;
// // TERNARY OPERATOR
// console.log(id === 60 ? 'Yes' : 'No');


// if (id === 65) {
//     console.log("Yes")
// }else {
//     console.log("No")
// }

// WITHOUT BRACES
id = 60
if(id === 60)
  console.log('Yes');
  
else
  console.log('No');