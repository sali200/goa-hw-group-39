console.log("Hello world");

let a = 10;
let b = 20;
console.log("ჯამი:", a + b);

let firstName = "Salome";
let lastName = "Kiknadze";
console.log("შეერთებული:", firstName + " " + lastName);

let x = 7;
let y = 2;
let result = x / y;
console.log("განაყოფი:", result);

// 5. შედარების ოპერატორები
console.log(5 > 3);    
console.log(5 < 3);    
console.log(5 == 5);   
console.log(5 != 3);   
console.log(5 >= 5);   
console.log(3 <= 5);   

// 6. შედარება + მათემატიკა
console.log(5 + 5 == 8 + 2); 

// 7. ლოგიკური ოპერატორები
console.log(true && false); 
console.log(true || false);  
console.log(!true);          

// 8. ლოგიკური + შედარების კომბინაცია
console.log(5 > 3 && 2 < 4);         
console.log(5 == 5 || 3 > 10);       
console.log(!(4 == 4));             
console.log(7 < 10 && 10 != 5);      
console.log(2 >= 2 || 1 > 5);        

// 9. for loop – 1-დან 10-მდე
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// 10. for loop – თითოეული სიმბოლო სტრინგში
let text = "Hello, World!";
for (let i = 0; i < text.length; i++) {
  console.log(text[i]);
}

// 11. while loop – 1-დან 10-მდე
let i = 1;
while (i <= 10) {
  console.log(i);
  i++;
}

// 12. while loop – ჯამი 50-მდე
let total = 0;
let num = 1;
while (total < 50) {
  total += num;
  num++;
}
console.log("ჯამი გახდა:", total);

// 13. ფუნქცია – საშუალო არითმეტიკული
function average(arr) {
  let sum = arr.reduce((acc, val) => acc + val, 0);
  return sum / arr.length;
}
console.log("საშუალო:", average([1, 3, 4, 5, 2])); 

// 14. ფუნქცია – რიცხვების კვადრატი
function squareList(arr) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(arr[i] ** 2);
  }
  return result;
}
console.log("კვადრატები:", squareList([3, 12, 5, 2, 6]));  

// 15. list (array) და string მეთოდები
let fruits = ["ვაშლი", "მსხალი", "ატამი"];
fruits.push("ბანანი");       
fruits.splice(1, 0, "კივი"); 
fruits.pop();                
fruits.sort();              
fruits.reverse();            
console.log("ფრუტები:", fruits);

let str = "  javascript is fun  ";
console.log(str.toUpperCase());      
console.log(str.toLowerCase());       
console.log(str.trim());             
console.log(str.replace("fun", "awesome")); 
console.log(str.split(" "));          