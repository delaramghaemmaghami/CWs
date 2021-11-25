// FUNCTION DECLARATIONS
// console.log(a);
// a = "salam";
// console.log(a);

// const add
// let test
// function add_2



// console.log( "the result is --- : ",add(5, 3) );

const add = function(x=2 ,y=4) {
    return x + y
};
// console.log(test)
let test = "dsksjd"
console.log(test)
console.log( "the result is --- : ",add(4, 2) );

function add_2(x=3, y=4) {
  // x + y;
  return x + y
}
console.log( add() );


// function add(x=2 ,y=4) {
    
//     return x + y;
// }

// console.log( add(1) );



// FUNCTION EXPRESIONS

// const add = function(x=2 ,y=4) {
//     return x + y;
// };

// console.log( add(1,2) );


// ARROW FUNCTION EXPRESIONS

// const add = function(x) {
//       return x;
//   };

// const add = () => x+y;



// console.log(add(1,4));

// IMMIDIATLEY INVOKABLE FUNCTION EXPRESSIONS - IIFEs

(function(){
  console.log('IIFE Ran..');

})();

function esm(){
  console.log('IIFE Ran..');
}

(function esm(){
  console.log('IIFE Ran..');
})()



// (function(name){
//   console.log('Hello '+ name);
// })('shideh');

