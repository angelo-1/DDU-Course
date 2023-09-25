// document.getElementById('home').style.display="none";
document.getElementById('about').style.display="none";
document.getElementById('dept').style.display="none";
document.getElementById('gall').style.display="none";
function homeFun(){
    document.getElementById('home').style.display="block";
    document.getElementById('about').style.display="none";
    document.getElementById('dept').style.display="none";
    document.getElementById('gall').style.display="none";
}
function aboutFun(){
    document.getElementById('about').style.display="block";
    document.getElementById('home').style.display="none";
    document.getElementById('dept').style.display="none";  
    document.getElementById('gall').style.display="none";
}
function departFun(){
    document.getElementById('home').style.display="none";
    document.getElementById('about').style.display="none";
    document.getElementById('dept').style.display="block";
    document.getElementById('gall').style.display="none";
}
function gallFun(){
    document.getElementById('home').style.display="none";
    document.getElementById('about').style.display="none";
    document.getElementById('dept').style.display="none";
    document.getElementById('gall').style.display="block";
}