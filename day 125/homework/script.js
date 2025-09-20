// JavaScript არის ერთთრედიანი ენა — ანუ მას აქვს მხოლოდ ერთი მთავარი ნაკადი (thread),
// რომელიც ასრულებს კოდს. ეს ნიშნავს, რომ ყველა ოპერაცია (მაგ. ფუნქციის გამოძახება, ცვლადების შეცვლა)
// ხდება თანმიმდევრულად, ერთ ხაზზე. მაგრამ...

// ...როდესაც საქმე ეხება ასინქრონულ ოპერაციებს (მაგ. სერვერზე მოთხოვნის გაგზავნა),
// JavaScript იყენებს Event Loop-ს და Callback Queue-ს, რათა არ დაბლოკოს მთავარი ნაკადი.

// Promise არის ობიექტი, რომელიც წარმოადგენს ასინქრონულ ოპერაციას.
// ის გვპირდება, რომ რაღაც მომენტში ოპერაცია დასრულდება წარმატებით (resolve) ან შეცდომით (reject).

function getDataFromServer() {
  return new Promise((resolve, reject) => {
        setTimeout(() => {
      const success = true; 
      if (success) {
        resolve("მონაცემები მიღებულია!");
      } else {
        reject("შეცდომა მოხდა!");
      }
    }, 2000); 
  });
}

// async ფუნქცია არის სინტაქსური შაქარი (syntactic sugar) Promise-ებისთვის.
// ის გვაძლევს საშუალებას, რომ დავწეროთ ასინქრონული კოდი ისე, თითქოს სინქრონულია.

async function fetchData() {
  try {
    console.log("მონაცემების მიღება დაიწყო...");
    const result = await getDataFromServer(); 
    console.log("შედეგი:", result);
  } catch (error) {
    console.error("შეცდომა:", error);
  }
}

fetchData(); 





