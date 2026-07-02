
const users = [
  { name: "Alice", age: 21 },
  { name: "Bob", age: 25 },
  { name: "Charlie", age: 19 },
  { name: "Diana", age: 23 },
  { name: "Ethan", age: 27 }
];

function calculateAverageAge(data) {
  let total = 0;

  for (const user of data) {
    total += user.age;
  }

  return total / data.length;
}

function findOldest(data) {
  return data.reduce((oldest, current) => {
    return current.age > oldest.age ? current : oldest;
  });
}

function capitalizeNames(data) {
  return data.map(user => ({
    ...user,
    name: user.name.toUpperCase()
  }));
}

const averageAge = calculateAverageAge(users);
const oldestUser = findOldest(users);
const updatedUsers = capitalizeNames(users);

console.log("Average Age:", averageAge);
console.log("Oldest User:", oldestUser);
console.log("Updated Users:");
updatedUsers.forEach(user => {
  console.log(`${user.name} (${user.age})`);
});

const randomIndex = Math.floor(Math.random() * users.length);
console.log("Random User:", users[randomIndex]);

const adults = users.filter(user => user.age >= 21);
console.log("Adult Count:", adults.length);
