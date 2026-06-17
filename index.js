function maskEmail(email) {

  let atIndex = email.indexOf("@");
  let name = email.slice(0, atIndex);
  let domain = email.slice(atIndex);

  return name[0] +
         "*".repeat(name.length - 2) +
         name[name.length - 1] +
         domain;
}
const email = "jwcesparcia@gmail.com"
console.log(maskEmail(email))