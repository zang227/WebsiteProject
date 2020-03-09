var interestList = document.querySelector("#interestList");
var newInterest = document.querySelector("#newInterest");
var btnAddInterest = document.querySelector("#addInterest");

btnAddInterest.addEventListener("click",addInterest);

function addInterest(){
    if (newInterest.value != ""){
        var li = document.createElement("li");
        li.textContent = newInterest.value;
        var span = document.createElement("span");
        span.classList.add("remove");
        span.textContent = "remove interest";
        span.addEventListener("click", removeInterest);
        li.appendChild(li);
        interestList.appendChild(span);
        newInterest.value="";
    }
}

function removeInterest(){
    interestList.removeChild(this.closest("li"));
}

// var interestList = "";
// var i = 0;
// function addInterest(){
//     var interests = document.getElementById("addInterest");
//     if (interests != ""){
//         interestList += "<li><span name = 'interestItem' id = 'interestItem'"+ i + ">" + interests + "</span>"+
//         "<a onclick = 'removeInterest()'>remove</a></li>"
//         i++;
//         document.getElementById("interest").innerHTML = interestList;
//         document.getElementById("addInterest").value ="";

//     }
// }

// function removeInterest(){
//     interestList = "";
//     var items = document.querySelectorAll("#interest li"),index, tab =[];
//     for (var j =0; j < items.length; j++){
//         tab.push(items[j].innerHTML);
//     }
//     for (var j = 0; j< items.length; j++){
//         items[j].onclick=function(){
//             index = tab.indexOf(this.innerHTML);
//             items[index].parentNode.removeChild(items[index]);
//             tab.splice(j,1);
//         }
//     }
//     console.log(tab);
//     for(var j=0; j<tab.length; j++){
//         interestList += "<li>" +tab[j] + "</li>";
//     }
// }