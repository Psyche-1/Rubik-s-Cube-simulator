(function () {
  let rotateY = 0,
    rotateX = 0;

  document.onkeydown = function (e) {
    if (e.keyCode === 37) rotateY -= 4;
    else if (e.keyCode === 38) rotateX += 4;
    else if (e.keyCode === 39) rotateY += 4;
    else if (e.keyCode === 40) rotateX -= 4;

    document.querySelector(".cube").style.transform =
      "rotateY(" + rotateY + "deg)" + "rotateX(" + rotateX + "deg)";
  };
})();
// backface-visibility: visible;  // show other side
// backface-visibility: hidden;  // hidden other side
let theme = "dark";
let chosenColor = "";
let chosenRotationCube = "type-enter";

const startCubeList = [
  ["y", "y", "y", "y", "y", "y", "y", "y", "y"], // 0	//top
  ["o", "o", "o", "o", "o", "o", "o", "o", "o"], // 1	//left_side
  ["b", "b", "b", "b", "b", "b", "b", "b", "b"], // 2	//front_side
  ["r", "r", "r", "r", "r", "r", "r", "r", "r"], // 3	//right_side
  ["w", "w", "w", "w", "w", "w", "w", "w", "w"], // 4	//bottom
  ["g", "g", "g", "g", "g", "g", "g", "g", "g"], // 5	//back_side
];

let cubeList = [
  ["y", "y", "y", "y", "y", "y", "y", "y", "y"], // 0	//top
  ["o", "o", "o", "o", "o", "o", "o", "o", "o"], // 1	//left_side
  ["b", "b", "b", "b", "b", "b", "b", "b", "b"], // 2	//front_side
  ["r", "r", "r", "r", "r", "r", "r", "r", "r"], // 3	//right_side
  ["w", "w", "w", "w", "w", "w", "w", "w", "w"], // 4	//bottom
  ["g", "g", "g", "g", "g", "g", "g", "g", "g"], // 5	//back_side
];

const colorDict = {
  y: "yellow",
  o: "orange",
  b: "blue",
  r: "red",
  w: "white",
  g: "green",
};

const colorBackwardDict = {
  yellow: "y",
  orange: "o",
  blue: "b",
  red: "r",
  white: "w",
  green: "g",
};

const themes = {
  dark: {
    yellow: "#B7B400",
    orange: "#C17A00",
    blue: "#0000AA",
    red: "#A00000",
    white: "#C0C0C0",
    green: "#008000",
  },
  neon: {
    yellow: "#FEFE22",
    orange: "#FFA420",
    blue: "#5555FF",
    red: "#F80000",
    white: "#FFFFFF",
    green: "#39FF14",
  },
  light: {
    yellow: "#FFFF00",
    orange: "#FFA500",
    blue: "#0000FF",
    red: "#FF0000",
    white: "#FFFFFF",
    green: "#00FF00",
  },
};

const body = document.querySelector("body");
const colorButtons = document.querySelectorAll(".color");
const usingThemeRadio = document.querySelectorAll(".themes");
const fragments = document.querySelectorAll("[data-color]");
const enterCubeRadios = document.querySelectorAll(".entering-types");

usingThemeRadio[0].addEventListener("click", changeThemeByRadioBtn);
usingThemeRadio[0].addEventListener("click", changeFragmentColorByTheme);
enterCubeRadios[0].addEventListener("click", chooseEnteringType);

for (const fragment of fragments) {
  fragment.addEventListener("click", changeFragmentColor);
}

for (const colorButton of colorButtons) {
  colorButton.addEventListener("click", chooseColor);
}

function changeTheme() {
  for (const colorButton of colorButtons) {
    colorButton.style = `background-color: ${
      themes[theme][colorButton.classList[0]]
    }`;
    if (theme === "light") {
      body.style = "background-color: white";
    } else {
      body.style = "background-color: black";
    }
  }
}

function changeThemeByRadioBtn(event) {
  if (event.target.nodeName !== "INPUT") {
    return;
  }
  theme = event.target.value;
  changeTheme();
}

function changeFragmentColorByTheme() {
  for (const fragment of fragments) {
    fragment.style = `background-color: ${
      themes[theme][fragment.dataset.color]
    };
    color: ${themes[theme][fragment.dataset.color]};`;
  }
}

function chooseColor(event) {
  if (chosenRotationCube === "type-enter") {
    chosenColor = event.target.textContent;
    // console.log(chosenColor);
  }
}

function chooseEnteringType(event) {
  if (event.target.nodeName !== "INPUT") {
    return;
  }
  chosenRotationCube = event.target.value;

  // for (const enterCubeRadio of enterCubeRadios[0].children) {
  //
  // }
}

function changeFragmentColor() {
  if (chosenRotationCube !== "type-enter") {
    return;
  }
  if (!chosenColor) {
    return;
  }
  // console.log(this);

  this.dataset.color = chosenColor;

  this.style = `background-color: ${themes[theme][this.dataset.color]};
  color: ${themes[theme][this.dataset.color]};`;

  cubeList[2][0] = colorBackwardDict[fragments[0].dataset.color];
  cubeList[2][1] = colorBackwardDict[fragments[1].dataset.color];
  cubeList[2][2] = colorBackwardDict[fragments[2].dataset.color];
  cubeList[2][3] = colorBackwardDict[fragments[3].dataset.color];
  cubeList[2][4] = colorBackwardDict[fragments[4].dataset.color];
  cubeList[2][5] = colorBackwardDict[fragments[5].dataset.color];
  cubeList[2][6] = colorBackwardDict[fragments[6].dataset.color];
  cubeList[2][7] = colorBackwardDict[fragments[7].dataset.color];
  cubeList[2][8] = colorBackwardDict[fragments[8].dataset.color];

  cubeList[5][0] = colorBackwardDict[fragments[9].dataset.color];
  cubeList[5][1] = colorBackwardDict[fragments[10].dataset.color];
  cubeList[5][2] = colorBackwardDict[fragments[11].dataset.color];
  cubeList[5][3] = colorBackwardDict[fragments[12].dataset.color];
  cubeList[5][4] = colorBackwardDict[fragments[13].dataset.color];
  cubeList[5][5] = colorBackwardDict[fragments[14].dataset.color];
  cubeList[5][6] = colorBackwardDict[fragments[15].dataset.color];
  cubeList[5][7] = colorBackwardDict[fragments[16].dataset.color];
  cubeList[5][8] = colorBackwardDict[fragments[17].dataset.color];

  cubeList[3][0] = colorBackwardDict[fragments[18].dataset.color];
  cubeList[3][1] = colorBackwardDict[fragments[19].dataset.color];
  cubeList[3][2] = colorBackwardDict[fragments[20].dataset.color];
  cubeList[3][3] = colorBackwardDict[fragments[21].dataset.color];
  cubeList[3][4] = colorBackwardDict[fragments[22].dataset.color];
  cubeList[3][5] = colorBackwardDict[fragments[23].dataset.color];
  cubeList[3][6] = colorBackwardDict[fragments[24].dataset.color];
  cubeList[3][7] = colorBackwardDict[fragments[25].dataset.color];
  cubeList[3][8] = colorBackwardDict[fragments[26].dataset.color];

  cubeList[1][0] = colorBackwardDict[fragments[27].dataset.color];
  cubeList[1][1] = colorBackwardDict[fragments[28].dataset.color];
  cubeList[1][2] = colorBackwardDict[fragments[29].dataset.color];
  cubeList[1][3] = colorBackwardDict[fragments[30].dataset.color];
  cubeList[1][4] = colorBackwardDict[fragments[31].dataset.color];
  cubeList[1][5] = colorBackwardDict[fragments[32].dataset.color];
  cubeList[1][6] = colorBackwardDict[fragments[33].dataset.color];
  cubeList[1][7] = colorBackwardDict[fragments[34].dataset.color];
  cubeList[1][8] = colorBackwardDict[fragments[35].dataset.color];

  cubeList[0][0] = colorBackwardDict[fragments[36].dataset.color];
  cubeList[0][1] = colorBackwardDict[fragments[37].dataset.color];
  cubeList[0][2] = colorBackwardDict[fragments[38].dataset.color];
  cubeList[0][3] = colorBackwardDict[fragments[39].dataset.color];
  cubeList[0][4] = colorBackwardDict[fragments[40].dataset.color];
  cubeList[0][5] = colorBackwardDict[fragments[41].dataset.color];
  cubeList[0][6] = colorBackwardDict[fragments[42].dataset.color];
  cubeList[0][7] = colorBackwardDict[fragments[43].dataset.color];
  cubeList[0][8] = colorBackwardDict[fragments[44].dataset.color];

  cubeList[4][0] = colorBackwardDict[fragments[45].dataset.color];
  cubeList[4][1] = colorBackwardDict[fragments[46].dataset.color];
  cubeList[4][2] = colorBackwardDict[fragments[47].dataset.color];
  cubeList[4][3] = colorBackwardDict[fragments[48].dataset.color];
  cubeList[4][4] = colorBackwardDict[fragments[49].dataset.color];
  cubeList[4][5] = colorBackwardDict[fragments[50].dataset.color];
  cubeList[4][6] = colorBackwardDict[fragments[51].dataset.color];
  cubeList[4][7] = colorBackwardDict[fragments[52].dataset.color];
  cubeList[4][8] = colorBackwardDict[fragments[53].dataset.color];
}

function createBijection() {
  fragments[0].dataset.color = colorDict[cubeList[2][0]]; //2 front_side
  fragments[1].dataset.color = colorDict[cubeList[2][1]]; // b
  fragments[2].dataset.color = colorDict[cubeList[2][2]];
  fragments[3].dataset.color = colorDict[cubeList[2][3]];
  fragments[4].dataset.color = colorDict[cubeList[2][4]];
  fragments[5].dataset.color = colorDict[cubeList[2][5]];
  fragments[6].dataset.color = colorDict[cubeList[2][6]];
  fragments[7].dataset.color = colorDict[cubeList[2][7]];
  fragments[8].dataset.color = colorDict[cubeList[2][8]];

  fragments[9].dataset.color = colorDict[cubeList[5][0]]; //back_side
  fragments[10].dataset.color = colorDict[cubeList[5][1]]; // g
  fragments[11].dataset.color = colorDict[cubeList[5][2]];
  fragments[12].dataset.color = colorDict[cubeList[5][3]];
  fragments[13].dataset.color = colorDict[cubeList[5][4]];
  fragments[14].dataset.color = colorDict[cubeList[5][5]];
  fragments[15].dataset.color = colorDict[cubeList[5][6]];
  fragments[16].dataset.color = colorDict[cubeList[5][7]];
  fragments[17].dataset.color = colorDict[cubeList[5][8]];

  fragments[18].dataset.color = colorDict[cubeList[3][0]]; //3 right_side
  fragments[19].dataset.color = colorDict[cubeList[3][1]]; // r
  fragments[20].dataset.color = colorDict[cubeList[3][2]];
  fragments[21].dataset.color = colorDict[cubeList[3][3]];
  fragments[22].dataset.color = colorDict[cubeList[3][4]];
  fragments[23].dataset.color = colorDict[cubeList[3][5]];
  fragments[24].dataset.color = colorDict[cubeList[3][6]];
  fragments[25].dataset.color = colorDict[cubeList[3][7]];
  fragments[26].dataset.color = colorDict[cubeList[3][8]];

  fragments[27].dataset.color = colorDict[cubeList[1][0]]; //1 left_side
  fragments[28].dataset.color = colorDict[cubeList[1][1]]; // o
  fragments[29].dataset.color = colorDict[cubeList[1][2]];
  fragments[30].dataset.color = colorDict[cubeList[1][3]];
  fragments[31].dataset.color = colorDict[cubeList[1][4]];
  fragments[32].dataset.color = colorDict[cubeList[1][5]];
  fragments[33].dataset.color = colorDict[cubeList[1][6]];
  fragments[34].dataset.color = colorDict[cubeList[1][7]];
  fragments[35].dataset.color = colorDict[cubeList[1][8]];

  fragments[36].dataset.color = colorDict[cubeList[0][0]]; //0 top
  fragments[37].dataset.color = colorDict[cubeList[0][1]]; // y
  fragments[38].dataset.color = colorDict[cubeList[0][2]];
  fragments[39].dataset.color = colorDict[cubeList[0][3]];
  fragments[40].dataset.color = colorDict[cubeList[0][4]];
  fragments[41].dataset.color = colorDict[cubeList[0][5]];
  fragments[42].dataset.color = colorDict[cubeList[0][6]];
  fragments[43].dataset.color = colorDict[cubeList[0][7]];
  fragments[44].dataset.color = colorDict[cubeList[0][8]];

  fragments[45].dataset.color = colorDict[cubeList[4][0]]; //4 bottom
  fragments[46].dataset.color = colorDict[cubeList[4][1]]; // w
  fragments[47].dataset.color = colorDict[cubeList[4][2]];
  fragments[48].dataset.color = colorDict[cubeList[4][3]];
  fragments[49].dataset.color = colorDict[cubeList[4][4]];
  fragments[50].dataset.color = colorDict[cubeList[4][5]];
  fragments[51].dataset.color = colorDict[cubeList[4][6]];
  fragments[52].dataset.color = colorDict[cubeList[4][7]];
  fragments[53].dataset.color = colorDict[cubeList[4][8]];
}

// B2 G5  R3  O1  Y0  W4
function one_rotation(cube, side, sign = "") {
  const sides = {
    U: up,
    F: front,
    R: right,
    D: down,
    B: back,
    L: left,
    E: equatorial, // between up и down
    S: standing, // between front и back
    M: middle, // between left и right
  };

  if (sign == "'") {
    sides[side](cube);
    sides[side](cube);
    sides[side](cube);
  } else if (sign == "2") {
    sides[side](cube);
    sides[side](cube);
  } else if (sign == "") {
    sides[side](cube);
  } else {
    console.log("sign error");
  }
}

function up(cube) {
  let t0 = cube[0][0];
  let t1 = cube[0][1];
  let t2 = cube[0][2];
  cube[0][0] = cube[0][6];
  cube[0][1] = cube[0][3];
  cube[0][2] = t0;
  cube[0][3] = cube[0][7];
  cube[0][6] = cube[0][8];
  cube[0][7] = cube[0][5];
  cube[0][8] = t2;
  cube[0][5] = t1;

  t0 = cube[5][0];
  t1 = cube[5][1];
  t2 = cube[5][2];
  cube[5][0] = cube[1][0];
  cube[5][1] = cube[1][1];
  cube[5][2] = cube[1][2];
  cube[1][0] = cube[2][0];
  cube[1][1] = cube[2][1];
  cube[1][2] = cube[2][2];
  cube[2][0] = cube[3][0];
  cube[2][1] = cube[3][1];
  cube[2][2] = cube[3][2];
  cube[3][0] = t0;
  cube[3][1] = t1;
  cube[3][2] = t2;
}

function front(cube) {
  let t0 = cube[2][0];
  let t1 = cube[2][1];
  let t2 = cube[2][2];
  cube[2][0] = cube[2][6];
  cube[2][1] = cube[2][3];
  cube[2][2] = t0;
  cube[2][3] = cube[2][7];
  cube[2][6] = cube[2][8];
  cube[2][7] = cube[2][5];
  cube[2][8] = t2;
  cube[2][5] = t1;

  t0 = cube[0][6];
  t1 = cube[0][7];
  t2 = cube[0][8];
  cube[0][6] = cube[1][8];
  cube[0][7] = cube[1][5];
  cube[0][8] = cube[1][2];
  cube[1][2] = cube[4][0];
  cube[1][5] = cube[4][1];
  cube[1][8] = cube[4][2];
  cube[4][0] = cube[3][6];
  cube[4][1] = cube[3][3];
  cube[4][2] = cube[3][0];
  cube[3][0] = t0;
  cube[3][3] = t1;
  cube[3][6] = t2;
}

function right(cube) {
  let t0 = cube[3][0];
  let t1 = cube[3][1];
  let t2 = cube[3][2];
  cube[3][0] = cube[3][6];
  cube[3][1] = cube[3][3];
  cube[3][2] = t0;
  cube[3][3] = cube[3][7];
  cube[3][6] = cube[3][8];
  cube[3][7] = cube[3][5];
  cube[3][8] = t2;
  cube[3][5] = t1;

  t0 = cube[0][2];
  t1 = cube[0][5];
  t2 = cube[0][8];

  cube[0][2] = cube[2][2];
  cube[0][5] = cube[2][5];
  cube[0][8] = cube[2][8];

  cube[2][2] = cube[4][2];
  cube[2][5] = cube[4][5];
  cube[2][8] = cube[4][8];

  cube[4][8] = cube[5][0];
  cube[4][5] = cube[5][3];
  cube[4][2] = cube[5][6];

  cube[5][0] = t2;
  cube[5][3] = t1;
  cube[5][6] = t0;
}

function down(cube) {
  let t0 = cube[4][0];
  let t1 = cube[4][1];
  let t2 = cube[4][2];
  cube[4][0] = cube[4][6];
  cube[4][1] = cube[4][3];
  cube[4][2] = t0;
  cube[4][3] = cube[4][7];
  cube[4][6] = cube[4][8];
  cube[4][7] = cube[4][5];
  cube[4][8] = t2;
  cube[4][5] = t1;

  t0 = cube[2][6];
  t1 = cube[2][7];
  t2 = cube[2][8];
  cube[2][6] = cube[1][6];
  cube[2][7] = cube[1][7];
  cube[2][8] = cube[1][8];
  cube[1][6] = cube[5][6];
  cube[1][7] = cube[5][7];
  cube[1][8] = cube[5][8];
  cube[5][6] = cube[3][6];
  cube[5][7] = cube[3][7];
  cube[5][8] = cube[3][8];
  cube[3][6] = t0;
  cube[3][7] = t1;
  cube[3][8] = t2;
}

function back(cube) {
  let t0 = cube[5][0];
  let t1 = cube[5][1];
  let t2 = cube[5][2];
  cube[5][0] = cube[5][6];
  cube[5][1] = cube[5][3];
  cube[5][2] = t0;
  cube[5][3] = cube[5][7];
  cube[5][6] = cube[5][8];
  cube[5][7] = cube[5][5];
  cube[5][8] = t2;
  cube[5][5] = t1;

  t0 = cube[0][2];
  t1 = cube[0][1];
  t2 = cube[0][0];
  cube[0][2] = cube[3][8];
  cube[0][1] = cube[3][5];
  cube[0][0] = cube[3][2];
  cube[3][8] = cube[4][6];
  cube[3][5] = cube[4][7];
  cube[3][2] = cube[4][8];
  cube[4][6] = cube[1][0];
  cube[4][7] = cube[1][3];
  cube[4][8] = cube[1][6];
  cube[1][0] = t0;
  cube[1][3] = t1;
  cube[1][6] = t2;
}

function left(cube) {
  let t0 = cube[1][0];
  let t1 = cube[1][1];
  let t2 = cube[1][2];
  cube[1][0] = cube[1][6];
  cube[1][1] = cube[1][3];
  cube[1][2] = t0;
  cube[1][3] = cube[1][7];
  cube[1][6] = cube[1][8];
  cube[1][7] = cube[1][5];
  cube[1][8] = t2;
  cube[1][5] = t1;

  t0 = cube[0][0];
  t1 = cube[0][3];
  t2 = cube[0][6];
  cube[0][0] = cube[5][8];
  cube[0][3] = cube[5][5];
  cube[0][6] = cube[5][2];
  cube[5][8] = cube[4][0];
  cube[5][5] = cube[4][3];
  cube[5][2] = cube[4][6];
  cube[4][0] = cube[2][0];
  cube[4][3] = cube[2][3];
  cube[4][6] = cube[2][6];
  cube[2][0] = t0;
  cube[2][3] = t1;
  cube[2][6] = t2;
}

// between up и down
function equatorial(cube) {
  let t0 = cube[2][3];
  let t1 = cube[2][4];
  let t2 = cube[2][5];
  cube[2][3] = cube[3][3];
  cube[2][4] = cube[3][4];
  cube[2][5] = cube[3][5];
  cube[3][3] = cube[5][3];
  cube[3][4] = cube[5][4];
  cube[3][5] = cube[5][5];
  cube[5][3] = cube[1][3];
  cube[5][4] = cube[1][4];
  cube[5][5] = cube[1][5];
  cube[1][3] = t0;
  cube[1][4] = t1;
  cube[1][5] = t2;
}

// between front и back
function standing(cube) {
  let t0 = cube[0][3];
  let t1 = cube[0][4];
  let t2 = cube[0][5];
  cube[0][3] = cube[1][7];
  cube[0][4] = cube[1][4];
  cube[0][5] = cube[1][1];
  cube[1][7] = cube[4][5];
  cube[1][4] = cube[4][4];
  cube[1][1] = cube[4][3];
  cube[4][5] = cube[3][1];
  cube[4][4] = cube[3][4];
  cube[4][3] = cube[3][7];
  cube[3][1] = t0;
  cube[3][4] = t1;
  cube[3][7] = t2;
}

// between left и right
function middle(cube) {
  let t0 = cube[0][1];
  let t1 = cube[0][4];
  let t2 = cube[0][7];
  cube[0][1] = cube[5][1];
  cube[0][4] = cube[5][4];
  cube[0][7] = cube[5][7];
  cube[5][1] = cube[4][1];
  cube[5][4] = cube[4][4];
  cube[5][7] = cube[4][7];
  cube[5][1] = cube[4][1];
  cube[5][4] = cube[4][4];
  cube[5][7] = cube[4][7];
  cube[2][1] = t0;
  cube[2][4] = t1;
  cube[2][7] = t2;
}

const turnLine = document.querySelector(".turn-line");

// typing-rotate buttons
const x2 = document.querySelector("#x2");
const stroke = document.querySelector("#stroke");
// const bra = document.querySelector("#bra");
// const ket = document.querySelector("#ket");

x2.addEventListener("click", x2Turn);
stroke.addEventListener("click", strokeTurn);
// bra.addEventListener("click", braTurn);
// ket.addEventListener("click", ketTurn);

let lastSymbol;

function x2Turn() {
  lastSymbol = turnLine.value[turnLine.value.length - 2];
  if (lastSymbol === "2" || lastSymbol === "'") {
    return;
  }
  turnLine.value = turnLine.value.slice(0, turnLine.value.length - 1) + "2 ";
  if (chosenRotationCube === "rotate-immediately") {
    "UFRDBLESM".includes(lastSymbol);

    one_rotation(cubeList, lastSymbol);
    changeCubeByTurn();
  }
}

function strokeTurn() {
  lastSymbol = turnLine.value[turnLine.value.length - 2];
  if (lastSymbol === "2" || lastSymbol === "'") {
    return;
  }
  turnLine.value = turnLine.value.slice(0, turnLine.value.length - 1) + "' ";
  if (chosenRotationCube === "rotate-immediately") {
    "UFRDBLESM".includes(lastSymbol);

    one_rotation(cubeList, lastSymbol, "2");
    changeCubeByTurn();
  }
}

// function braTurn() {
//   turnLine.value += ") ";
// }

// function ketTurn() {
//   turnLine.value += "( ";
// }

const backspace = document.querySelector("#backspace");
const enter = document.querySelector("#enter");
const clear = document.querySelector("#clear");

backspace.addEventListener("click", doBackspace);
enter.addEventListener("click", doEnter);
clear.addEventListener("click", doClear);

function doBackspace() {
  turnLine.value =
    turnLine.value
      .trim()
      .slice(0, turnLine.value.trim().length - 1)
      .trim() + " ";
}

let turns;

function doEnter() {
  if (chosenRotationCube !== "type-rotation") {
    return;
  }

  turns = turnLine.value.trim().split(" ");
  turns = turns.filter((turn) => turn !== "");

  for (const turn of turns) {
    one_rotation(cubeList, ...turn.split(""));
  }

  changeCubeByTurn();
}

function doClear() {
  turnLine.value = "";
}

const U = document.querySelector("#U");
const F = document.querySelector("#F");
const R = document.querySelector("#R");
const D = document.querySelector("#D");
const B = document.querySelector("#B");
const L = document.querySelector("#L");
const E = document.querySelector("#E");
const S = document.querySelector("#S");
const M = document.querySelector("#M");

U.addEventListener("click", UTurn);
F.addEventListener("click", FTurn);
R.addEventListener("click", RTurn);
D.addEventListener("click", DTurn);
B.addEventListener("click", BTurn);
L.addEventListener("click", LTurn);
E.addEventListener("click", ETurn);
S.addEventListener("click", STurn);
M.addEventListener("click", MTurn);

function UTurn() {
  turnLine.value += "U ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "U");
    changeCubeByTurn();
  }
}
function FTurn() {
  turnLine.value += "F ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "F");
    changeCubeByTurn();
  }
}
function RTurn() {
  turnLine.value += "R ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "R");
    changeCubeByTurn();
  }
}
function DTurn() {
  turnLine.value += "D ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "D");
    changeCubeByTurn();
  }
}
function BTurn() {
  turnLine.value += "B ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "B");
    changeCubeByTurn();
  }
}
function LTurn() {
  turnLine.value += "L ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "L");
    changeCubeByTurn();
  }
}
function ETurn() {
  turnLine.value += "E ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "E");
    changeCubeByTurn();
  }
}
function STurn() {
  turnLine.value += "S ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "S");
    changeCubeByTurn();
  }
}
function MTurn() {
  turnLine.value += "M ";
  if (chosenRotationCube === "rotate-immediately") {
    one_rotation(cubeList, "M");
    changeCubeByTurn();
  }
}

const cut = document.querySelector("#cut");
const copy = document.querySelector("#copy");
const paste = document.querySelector("#paste");

cut.addEventListener("click", doCut);
copy.addEventListener("click", doCopy);
paste.addEventListener("click", doPaste);

function doCut() {
  navigator.clipboard.writeText(turnLine.value);
  turnLine.value = "";
}
function doCopy() {
  navigator.clipboard.writeText(turnLine.value);
}
function doPaste() {
  navigator.clipboard
    .readText()
    .then((clipText) => (turnLine.value += clipText));
}

// const arrowUp = document.querySelector("#arrow-up");
// const arrowLeft = document.querySelector("#arrow-left");
// const arrowDown = document.querySelector("#arrow-down");
// const arrowRight = document.querySelector("#arrow-right");

// arrowUp.addEventListener("click", rotateUp);
// arrowLeft.addEventListener("click", rotateLeft);
// arrowDown.addEventListener("click", rotateDown);
// arrowRight.addEventListener("click", rotateRight);

// function rotateUp() {
//   document.dispatchEvent(
//     new KeyboardEvent("keydown", {
//       key: "up",
//       char: 37,
//       ctrlKey: false,
//     })
//   );
// }
// function rotateLeft() {}
// function rotateDown() {}
// function rotateRight() {}

const refresh = document.querySelector("#refresh");

refresh.addEventListener("click", doRefresh);

function doRefresh() {
  cubeList = [];
  for (let i = 0; i < startCubeList.length; i++) {
    cubeList.push([...startCubeList[i]]);
  }

  changeCubeByTurn();
}

function changeCubeByTurn() {
  createBijection();
  changeTheme();
  changeFragmentColorByTheme();
}

changeCubeByTurn();
