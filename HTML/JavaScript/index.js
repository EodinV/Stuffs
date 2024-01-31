let xp = 0;
let health = 100;
let gold = 50;
let stamina = 300;
let currentWeapon = 0;
let fighting;
let monsterHealth;
let inventory = ["stick"];

const button1 = document.querySelector("#button1");
const button2 = document.querySelector("#button2");
const button3 = document.querySelector("#button3");
const text = document.querySelector("#text");
const xpText = document.querySelector("#xpText");
const healthText = document.querySelector("#healthText");
const goldText = document.querySelector("#goldText");
const staminaText = document.querySelector("#staminaText");
const monsterStats = document.querySelector("#monsterStats");
const monsterNameText = document.querySelector("#monsterName");
const monsterHealthText = document.querySelector("#monsterHealth");

const locations = [
    {
        name: "town square",
        "button text": ["Got to ze store", "Go to ze cave", "Fight ze Dragon"],
        "button functions": [goStore, goCave, fightDragon],
        text: "You are in ze town square, you see a sign that says \"Store.\""
    },
    {
        name: "store",
        "button text": ["Buy 10 health (10 gold)", "Buy weapon (30 gold)", "Go to ze town square"],
        "button functions": [buyHealth, buyWeapon, goTown],
        text: "You enter ze store."
    },
    {
        name: "fight",
        "button text": ["Heavy Attack", "Quick Attack", "Back away"],
        "button funcctions": [heavyAttackM, lightAttackM, goTown],
        text: "The cave is full of monsters, just waiting to give their lives to up your XP."
    },
    {
        name: "fightDragon",
        "button text": ["Heavy Attack", "Quick Attack", "Back away"],
        "button functions": [heavyAttackD, lightAttackD, goTown],
        text: "The Dragon looks at you, waiting for you to give up and go away."
    }
]


// initialize buttons.

button1.onclick = goStore;
button2.onclick = goCave;
button3.onclick = fightDragon;

function update(location) {
    button1.innerText = location["button text"][0];
    button2.innerText = location["button text"][1];
    button3.innerText = location["button text"][2];
    button1.onclick = location["button functions"][0];
    button2.onclick = location["button functions"][1];
    button3.onclick = location["button functions"][2];
    text.innerText = location.text
}
function goTown() {
    update(locations[0]);
}

function goStore() {
    update(locations[1]);
}

function goCave() {
    update(locations[2]);
}

function fightDragon() {
    if (health >= 5) {
        xp += 1;
        healthText.innerText = health;
    } else {
        text.innerText = "You do not have enough BLOOD!!!!"
    }
}

function buyHealth() {
    if (gold >= 10) {
        gold -= 10;
        health += 10;
        goldText.innerText = gold;
        healthText.innerText = health;
    } else {
        text.innerText = "You do not have enough gold!!!!"
    }
    
}

function buyWeapon() {
    if (gold >= 30) {
        gold -= 30;
        inventory[1] += "sword";
        goldText.innerText = gold;
    } else {
        text.innerText = "You do not have enough gold!!!!"
    }
}

function heavyAttackM() {
    if (stamina >= 50) {
        if (currentWeapon = 1) {
            monsterHealth -= 15;
            stamina -= 50;
            text.innerText = "A light graze, but the beast winces in pain as your sword slices through its skin.";
            staminaText.innerText = stamina;
        } else {
            monsterHealth -= 5;
            stamina -= 50;
            text.innerText = "A heavy thump on the monsters head, a slight stagger. One would think a better weapon would be better.";
            staminaText.innerText = stamina;
            
        }
    } else {
        text.innetText = "Your heart beats too fast, you swing but you miss."   
    } 

}

function heavyAttackD() {
    if (stamina >= 50) {
        if (currentWeapon = 1) {
            monsterHealth -= 15;
            stamina -= 50;
            text.innerText = "A light graze, but the beast winces in pain as your sword slices through its skin.";
            staminaText.innerText = stamina;
        } else {
            monsterHealth -= 5;
            stamina -= 50;
            text.innerText = "A heavy thump on the monsters head, a slight stagger. One would think a better weapon would be better.";
            staminaText.innerText = stamina;
            
        }
    } else {
        text.innetText = "Your heart beats too fast, you swing but you miss."   
    } 

}

function lightAttackM() {
    if (stamina >= 25) {
        if (currentWeapon = 1) {
            monsterHealth -= 5;
            stamina -= 25;
            text.innerText = "A light graze, but the beast winces in pain as your sword slices through its skin."
        } else {
            monsterHealth -= 1;
            stamina -= 25;
            text.innerText = "A light tap on the monsters head, maybe you should find another weapon?"
            
        }
    } else {
        text.innetText = "Your heart beats too fast, your brain is foggy, you swing but you miss."   
    }
}

function lightAttackD() {
    if (stamina >= 25) {
        if (currentWeapon = 1) {
            monsterHealth -= 5;
            stamina -= 25;
            text.innerText = "A light graze, but the beast winces in pain as your sword slices through its skin."
        } else {
            monsterHealth -= 1;
            stamina -= 25;
            text.innerText = "A light tap on the monsters head, maybe you should find another weapon?"
            
        }
    } else {
        text.innetText = "Your heart beats too fast, you swing but you miss."   
    }
}