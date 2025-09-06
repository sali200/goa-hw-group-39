
    const products = [
      { id: 1, name: "leptopi", price: 79342 },
      { id: 2, name: "mobiluri", price: 69213},
      { id: 3, name: "naushniki", price: 8924 }
    ];

    const productList = document.getElementById("product-list");
    const cart = document.getElementById("cart");
    const cartItems = [];

    function renderCart() {
      cart.innerHTML = "";
      for (let item of cartItems) {
        const div = document.createElement("div");
        div.className = "cart-item";
      }}




async function getData() {
  try {
    
    let response = await fetch("https://api.escuelajs.co/api/v1/products");

    let data = await response.json();

    console.log(data);
  } catch (error) {
    console.log("error");
  }
}

getData(); 