let tomb1 = [];
//1.
for (let i = 1; i <= 100; i++) {
    tomb1.push(i);
}
//2.
tomb1 = Array.from({ length: 100 }, (_, index) => index + 1);
//3.
tomb1 = new Array(100).fill().map((_, index) => index + 1);
//MASODIK FELADAT
let tomb2 = [];
for (let i = 100; i >= 1; i--) {
    tomb2.push(i);
}
//elsoelem  
let elsoElem = tomb2[0];
console.log("Az utolsó tömb első eleme: " + elsoElem);