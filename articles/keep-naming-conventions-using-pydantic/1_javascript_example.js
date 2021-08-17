const sumEvenNumbers = numbers => {
  evenNumbers = numbers.filter(number => number % 2 === 0);
  return evenNumbers.reduce((acc, number) => acc + number, 0);
};

const exampleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(sumEvenNumbers(exampleNumbers));
