// document.getElementsByClassName

const items = document.getElementsByClassName('list-group-item');
// console.log(items);

// console.log(items[0]);
items[0].style.color = 'red';
items[2].textContent = 'Hello';

console.log(document.querySelector('ul'))
const listItems = document.querySelector('ul').getElementsByClassName('list-group-item');

// console.log(listItems);
// console.log(listItems[0]);

// document.getElementsByTagName
// let lis = document.getElementsByTagName('li');
// console.log(lis);
// console.log(lis[0]);