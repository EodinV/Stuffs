let code = 0;
let min = 999;
let max = 10000;

const button0 = document.querySelector("#button0");
const button1 = document.querySelector("#button1");
const button2 = document.querySelector("#button2");
const button3 = document.querySelector("#button3");
const button4 = document.querySelector("#button4");
const button5 = document.querySelector("#button5");
const button6 = document.querySelector("#button6");
const button7 = document.querySelector("#button7");
const button8 = document.querySelector("#button8");
const button9 = document.querySelector("#button9");




function rand_int(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}