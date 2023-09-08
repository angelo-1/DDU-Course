
document.getElementById("7").addEventListener("click", function() {
    addToDisplay("7");
});

document.getElementById("8").addEventListener("click", function() {
    addToDisplay("8");
});

document.getElementById("9").addEventListener("click", function() {
    addToDisplay("9");
});

document.getElementById("ac").addEventListener("click", function() {
    clearDisplay();
});

document.getElementById("4").addEventListener("click", function() {
    addToDisplay("4");
});

document.getElementById("5").addEventListener("click", function() {
    addToDisplay("5");
});

document.getElementById("6").addEventListener("click", function() {
    addToDisplay("6");
});

document.getElementById("add").addEventListener("click", function() {
    addToDisplay("+");
});

document.getElementById("1").addEventListener("click", function() {
    addToDisplay("1");
});

document.getElementById("2").addEventListener("click", function() {
    addToDisplay("2");
});

document.getElementById("3").addEventListener("click", function() {
    addToDisplay("3");
});

document.getElementById("sub").addEventListener("click", function() {
    addToDisplay("-");
});

document.getElementById("0").addEventListener("click", function() {
    addToDisplay("0");
});

document.getElementById("dot").addEventListener("click", function() {
    addToDisplay(".");
});

document.getElementById("equal").addEventListener("click", function() {
    calculate();
});

document.getElementById("mult").addEventListener("click", function() {
    addToDisplay("*");
});

document.getElementById("divid").addEventListener("click", function() {
    addToDisplay("/");
});

document.getElementById("perc").addEventListener("click", function() {
    addToDisplay("%");
});

document.getElementById("del").addEventListener("click", function() {
    backspace();
});

document.getElementById("00").addEventListener("click", function() {
    addToDisplay("00");
});

function addToDisplay(value) {
    document.getElementById("expression").value += value;
}

function calculate(){
    try{
        const expression = document.getElementById("expression").value;
        const result = eval(expression.replaceAll('%','*0.01'));
        document.getElementById("result").value = result;
    }
    catch (error) {
        document.getElementById("result").value = 'ERROR,NOT FOUND!';
        if(error){
            document.getElementById("result").style.color="red";
        }
    }
    return result;
}
function clearDisplay() {
    document.getElementById("expression").value = '';
    document.getElementById("result").value = '';
}

function backspace(){
    const currentDisplay = document.getElementById("expression").value;
            document.getElementById("expression").value = currentDisplay.slice(0, -1);
}

// var b=document.getElementById("result");
// var c=document.getElementById("expression");
// var a=document.getElementById('equal');
// addEventListener('keydown',function(event){
//     if(event.key === 'Enter'){
//         b.value=a.value;
//         a.value='';
//     }
// });
// let lastExpression='';
// a.addEventListener('click',function(){
//     var currentExpression=b.value;
//     if(currentExpression!==lastExpression){
//         let results=calculate(currentExpression);
//         c.value=results;
//         lastExpression=currentExpression;
//     }else{
//         c.value=c.value;
//     }
// });