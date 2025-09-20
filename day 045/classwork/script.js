let words = ["მზე", "წვიმა", "ქარი", "თოვლი", "ღრუბელი"];
console.log("სიტყვები:");
for (let word of words) {
  console.log(word);
}

let numbers = [5, 12, 7, 3, 9];
console.log("რიცხვები:");
for (let num of numbers) {
  console.log(num);
}

let nums = [4, 6, 2, 8, 5];
console.log("რიცხვები გამრავლებული საკუთარ თავზე:");
for (let num of nums) {
  console.log(num * num);
}

let original = [1, 3, 5, 7, 9];
let doubled = [];
for (let num of original) {
  doubled.push(num * 2);
}
console.log("გაორმაგებული სია:");
console.log(doubled);