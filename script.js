//marche parfaitement//
var modal = document.getElementById("leadModal");
var btn = document.getElementById("btnNo");
console.log('console log de modal')
window.onscroll=function(){modalHomePage()}//active la fonction//
function modalHomePage(){
	if (document.body.scrollTop <= 100 || document.documentElement.scrollTop <= 100){//si on 
		//est a moins ou egal a 350px du bas de la page
		modal.style.display="block";
		window.onscroll="null";
	}else{//sinon//
		modal.style.display="none";
	}
}
btn.onclick= function(){//fait disparaitre la div si non merci je ne pref pas savoir
	modal.style.display="none";
}



















































































