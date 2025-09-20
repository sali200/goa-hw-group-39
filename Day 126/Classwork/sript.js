// Heap გამოიყენება კომპლექსური მონაცემების შესანახად, (ანუ მასივები და ობიექტები)



 // stack -მარტივ მნიშვნელობებს ინახავს ( Nnumber, boollen, string, undefind, null)



 function manualIndexOf(array, element) {
  for (let i = 0; i < array.length; i++) {
          if (array[i] === element) {
      return i; 
    }
  }
  return -1;}