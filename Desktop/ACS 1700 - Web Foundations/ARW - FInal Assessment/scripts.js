//Input Variables
const widthInput = document.querySelector('#width-input');
const heightInput = document.querySelector('#height-input');
const colorInput = document.querySelector('#color-input');
//Display Variables
const widthDisplay = document.querySelector('#display-width');
const heightDisplay = document.querySelector('#display-height');
const colorDisplay = document.querySelector('#display-color-hex');
const colorBox = document.querySelector('#box');



//Function to Update Display
const updateDisplay = (e) => {
    widthDisplay.innerHTML = `${widthInput.value}px`;
    heightDisplay.innerHTML = `${heightInput.value}px`;
    colorDisplay.innerHTML = colorInput.value;
    colorBox.style.height = `${heightInput.value}px`;
    colorBox.style.width = `${widthInput.value}px`;
    colorBox.style.backgroundColor = colorInput.value;
}

//Event Listeners
widthInput.addEventListener('input', updateDisplay);
heightInput.addEventListener('input', updateDisplay);
colorInput.addEventListener('input', updateDisplay);
colorBox.addEventListener('input', updateDisplay);



