function submitNotice(){
let title=document.getElementById("title").value;
let content=document.getElementById("content").value;
fetch("add_notice",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
title:title,
content:content
})
})
.then(response=>response.json())
.then(data=>{
alert(data.message);
window.location="/";
});
}
function loadNotices(){
fetch("/notices")
.then(response=>response.json())
.then(data=>{
let html="";
data.forEach(n=>{
html+=`
<div class="notice ${n.priority.toLowerCase()}">
<h3>${n.title}</h3>
<p><b>Category:</b> ${n.category}</p>
<p><b>Priority:</b> ${n.priority}</p>
<p>${n.summary}</p>
</div>
`;
});
let list=document.getElementById("noticeList");
if(list){
list.innerHTML=html;
}
});
}
loadNotices();

