// პრიმიტიული მონაცემები ინახება stack memory-ში, რაც ნიშნავს, რომ ისინი ინახება სწრაფად და პირდაპირ. ეს მონაცემები immutable ანუ უცვლადია.
let fruits = ["apple", "banana"];
fruits.push("orange"); 

let numbers = [1, 2];
numbers.push(3, 4); 

let empty = [];
empty.push("first"); 


let colors = ["red", "green", "blue"];
colors.pop(); 

let stack = [10, 20, 30];
let last = stack.pop(); 

let single = ["only"];
single.pop(); 


let names = ["salome", "nika"];
names.unshift("ana"); 

let nums = [2, 3];
nums.unshift(1); 

let letters = ["b", "c"];
letters.unshift("a", "aa"); 
