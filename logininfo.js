window.addEventListener("load",Initcontrols);
window.addEventListner("load",addListener);

function InitControls()
{
document.getElementById("txtusername").textContent = "";
document.getElementById("txtpassword").textContent = "";
document.getElementById("txtusername").focus();
}

function addListener()
{
document.getElementbyId("btnsubmit").addeventListener("click",Checkinfo);
}

function Checkinfo()
{
var username,passwd;
username = document.getElementById("txtusername").value;
password = document.getElementById("txtpassword").value;

if(username == "" || passwd == "")
{
alert("information is missing")
Initcontrols();
}

}