// ################### togtmoluud -------------------------------

var myMesssages = {
	emptyPassword: "Хуучин нууц үгээ оруулна уу!",
	phoneNumber: "Утасны дугаар 8 оронтой байх ёстой",
	registerNumber:"Регистрийн дугаарын формат буруу байна /АА99112233/",
	
};

// ################### togtmoluud end ---------------------------

//######################## org grid and list ################################

function toggleView(e) {
	if (e.className != "fa fa-th-large grid-layout") {
		e.className = "fa fa-th-large grid-layout";
		document.querySelector(".project-container").classList.add("list");
		document.querySelector(".project-container").classList.remove("gridd");
	} else if (e.className == "fa fa-th-large grid-layout") {
		e.className = "fa fa-list list-layout";
		document.querySelector(".project-container").classList.remove("list");
		document.querySelector(".project-container").classList.add("gridd");
	}

	return false;
}

//##################### search org ##############################
$(function () {
	$("[data-search]").on("keyup", function () {
		var searchVal = $(this).val();
		console.log(searchVal);
		var filterItems = $("[data-filter-item]");

		if (searchVal != "") {
			filterItems.addClass("hidden");
			$('[data-filter-name*="' + searchVal.toUpperCase() + '"]').removeClass(
				"hidden"
			);
		} else {
			filterItems.removeClass("hidden");
		}
	});
});

//############### check register pop up ################
function checkPage() {
	window.open("checkPage", "_blank", "top=150,left=450,width=500,height=500");
}

// ############ check page register validation ##############
function checkReg() {
	userRegister = document.getElementById("userRegister");
	form = document.getElementById("form");
	error = document.getElementById("error");
	reqsuccess = document.getElementById("reqsuccess");
	reqerror = document.getElementById("reqerror");

	checkregister = new RegExp("^[а-яА-Я|Өө|Ёё|Үү]{2}[0-9]{8}$");

	form.addEventListener("submit", (e) => {
		let messages = [];
		if (checkregister.test(userRegister.value)) {
		} else {
			messages.push("Регистрийн дугаарын формат буруу байна /АА99112233/");
		}

		if (messages.length > 0) {
			e.preventDefault();
			error.innerText = messages.join("");
			error.classList.remove("hide");

			if (reqsuccess != null) {
				reqsuccess.classList.add("hide");
			} else if (reqerror != null) {
				reqerror.classList.add("hide");
			}
			setTimeout(function () {
				error.classList.add("fade-in");
				setTimeout(function () {
					error.classList.remove("fade-in");
					setTimeout(function () {
						error.classList.add("hide");
					}, 1000);
				}, 5000);
			});
		}
	});
}

//############## forget password pop up window ################
function forgotPassword() {
	window.open("forgotres", "_blank", "top=150,left=450,width=600,height=700");
}

//############## rules show and hide #######################
function toggle(el) {
	if (el.childNodes[2].className === "disappear") {
		el.childNodes[2].classList.remove("disappear");
	} else {
		el.childNodes[2].classList.add("disappear");
	}
}

//############## register page form validation  #######################
function registerCheck() {
	userRegister = document.getElementById("userregister");
	userEmail = document.getElementById("useremail");
	regform = document.getElementById("regform");
	error = document.getElementById("error");
	//reqsuccess = document.getElementById("reqsuccess");
	//reqerror = document.getElementById("reqerror");

	checkregister = new RegExp("^[а-яА-Я|Өө|Ёё|Үү]{2}[0-9]{8}$");
	checkemail = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);

	regform.addEventListener("submit", (e) => {
		let messages = [];
		if (checkregister.test(userRegister.value)) {
			if (checkemail.test(userEmail.value)) {
			} else {
				messages.push("И-мэйл формат буруу байна");
			}
		} else {
			messages.push("Регистрийн дугаарын формат буруу байна /АА99112233/");
		}

		if (messages.length > 0) {
			e.preventDefault();
			error.innerText = messages.join("");
			error.classList.remove("hide");

			// if (reqsuccess != null) {
			// 	reqsuccess.classList.add("hide");
			// } else if (reqerror != null) {
			// 	reqerror.classList.add("hide");
			// }
			setTimeout(function () {
				error.classList.add("fade-in");
				setTimeout(function () {
					error.classList.remove("fade-in");
					setTimeout(function () {
						error.classList.add("hide");
					}, 1000);
				}, 5000);
			});
		}
	});
}
//##################register page form validation end/

//############## forgotpassword page form validation  #######################
function checkRegandEmail() {
	radioId = document.getElementById("mytext");
	forgotRandE = document.getElementById("forgotRandE");
	regform = document.getElementById("forgotPass");
	// error = document.getElementById("error");
	//reqsuccess = document.getElementById("reqsuccess");
	//reqerror = document.getElementById("reqerror");

	checkregister = new RegExp("^[а-яА-Я|Өө|Ёё|Үү]{2}[0-9]{8}$");
	checkemail = new RegExp(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);

	regform.addEventListener("submit", (e) => {
		let messages = [];
		if(radioId.value == "Регистрийн дугаар" && checkregister.test(forgotRandE.value))
		{
			
		}
		else if(radioId.value == "Бүртгэлтэй цахим шуудан" && checkregister.test(forgotRandE.value))
		{

		}
		else
		{ messages.push("Регистрийн дугаар эсвэл цахим шууданнийн формат буруу байна.");}


		// if (checkregister.test(userRegister.value)) {
		// 	if (checkemail.test(userEmail.value)) {
		// 	} else {
		// 		messages.push("И-мэйл формат буруу байна");
		// 	}
		// } else {
		// 	messages.push("Регистрийн дугаарын формат буруу байна /АА99112233/");
		// }

		if (messages.length > 0) {
			e.preventDefault();
			error.innerText = messages.join("");
			error.classList.remove("hide");

			// if (reqsuccess != null) {
			// 	reqsuccess.classList.add("hide");
			// } else if (reqerror != null) {
			// 	reqerror.classList.add("hide");
			// }
			setTimeout(function () {
				error.classList.add("fade-in");
				setTimeout(function () {
					error.classList.remove("fade-in");
					setTimeout(function () {
						error.classList.add("hide");
					}, 1000);
				}, 5000);
			});
		}
	});
}
//##################forgotpassword page form validation end/

function proCheck(evt, PName) {
	var i, content, link;
	content = document.getElementsByClassName("PPContent");
	for (i = 0; i < content.length; i++) {
		content[i].style.display = "none";
	}
	link = document.getElementsByClassName("PPlink");
	for (i = 0; i < link.length; i++) {
		link[i].className = link[i].className.replace("regcolor", " ");
	}
	document.getElementById(PName).style.display = "block";
	evt.currentTarget.className += " regcolor";
}

//############################Profile edit end/

function myfunc() {
	document.getElementById("demo").innerHTML = "Hello World";
	const updateButton = document.getElementById("updateDetails");
	const favDialog = document.getElementById("favDialog");
	const outputBox = document.querySelector("output");
	const selectEl = favDialog.querySelector("select");
	const confirmBtn = favDialog.querySelector("#confirmBtn");
	if (typeof favDialog.showModal !== "function") {
		favDialog.hidden = true;
	} else {
		favDialog.hidden = false;
	}
	updateButton.addEventListener("click", function onOpen() {
		if (typeof favDialog.showModal === "function") {
			favDialog.showModal();
		}
	});
	selectEl.addEventListener("change", function onSelect(e) {
		confirmBtn.value = selectEl.value;
	});
}

//adminDashboardEnd/

function checkpass() {
	newPassword = document.getElementById("newPassword");
	confirmPassword = document.getElementById("confirmPassword");
	form = document.getElementById("myForm2");
	error = document.getElementById("error");

	checkPass = new RegExp(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/);

	form.addEventListener("submit", (e) => {
		let messages = [];
		if (newPassword.value == confirmPassword.value) {
			if (newPassword.value.length > 5) {
				if (checkPass.test(newPassword.value)) {
				} else {
					messages.push("Нууц үгийн формат буруу байна /A-Z,a-z,0-9/");
				}
			} else {
				messages.push("Хамгийн багадаа 6 тэмдэгт байна");
			}
		} else {
			messages.push(
				"Шинэ нууц үг баталгаажуулах нууц үгтэй таарахгүй байна !!!"
			);
		}

		if (messages.length > 0) {
			e.preventDefault();
			error.innerText = messages.join("");
			error.classList.remove("hide");
			setTimeout(function () {
				error.classList.add("fade-in");
				setTimeout(function () {
					error.classList.remove("fade-in");
					setTimeout(function () {
						error.classList.add("hide");
					}, 1000);
				}, 5000);
			});
		}
	});
}

function popupClose() {
	document.getElementById("popup").style.display = "none";
} //choosepayer popup

function openDiv(evt, divName) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("Rshow");

	let cc = document.getElementById(divName).style.display;

	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("borders");

	if (cc != "block") document.getElementById(divName).style.display = "block";
}

//userRequestCreate

function openTT(evt, TTName) {
	var i, TTcontent, TTlink;
	TTcontent = document.getElementsByClassName("TTcontent");
	medee = document.getElementById("medee");
	TT11 = document.getElementById("TT11");
	xm1 = document.getElementById("xm1");
	xm2 = document.getElementById("xm2");
	xm3 = document.getElementById("xm3");
	xm4 = document.getElementById("xm4");

	for (i = 0; i < TTcontent.length; i++) {
		TTcontent[i].className = TTcontent[i].className.replace(" active", " ");
	}
	TTlink = document.getElementsByClassName("TTlink");
	for (i = 0; i < TTlink.length; i++) {
		TTlink[i].className = TTlink[i].className.replace("active", " ");
	}
	document.getElementById(TTName).classList.add("active");
	evt.currentTarget.className += " active";
	if (medee.classList.contains("active")) {
		xm1.classList.remove("d-none");
		xm2.classList.remove("d-none");
		xm3.classList.remove("d-none");
		xm4.classList.remove("d-none");
	} else if (TT11.classList.contains("active")) {
		xm1.classList.add("d-none");
		xm2.classList.add("d-none");
		xm3.classList.add("d-none");
		xm4.classList.add("d-none");
	}
} //TT11 end

function saveTT11() {
	document.getElementById("ctuluvtt11").value = "1";
} // save tt11 tuluv

function sendTT11() {
	document.getElementById("ctuluvtt11").value = "2";
} // send tt11 tuluv

function acceptedTT11() {
	document.getElementById("ctuluvtt11").value = "3";
} // accepted tt11 tuluv

function canceledTT11() {
	document.getElementById("ctuluvtt11").value = "4";
} // canceled tt11 tuluv

function adminFilter1() {
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("myInput1");
	filter = input.value.toUpperCase();
	table = document.getElementById("myTable");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[0];
		if (td) {
			txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}
function adminFilter3() {
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("myInput3");
	filter = input.value.toUpperCase();
	table = document.getElementById("myTable");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[2];
		if (td) {
			txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}
function adminFilter4() {
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("myInput4");
	filter = input.value.toUpperCase();
	table = document.getElementById("myTable");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[3];
		if (td) {
			txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}
function adminFilter5() {
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("myInput5");
	filter = input.value.toUpperCase();
	table = document.getElementById("myTable");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[4];
		if (td) {
			txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}
function adminFilter() {
	var input, filter, table, tr, td, i, txtValue;
	input = document.getElementById("myInput");
	filter = input.value.toUpperCase();
	table = document.getElementById("myTable");
	tr = table.getElementsByTagName("tr");
	for (i = 0; i < tr.length; i++) {
		td = tr[i].getElementsByTagName("td")[2];
		if (td) {
			txtValue = td.textContent || td.innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}
//admin search

//Ene hesegt tuslamjiin hesegtee holboogotoi jsuud baina
function helpFunction() {
	var x = document.getElementById("showbtn");
	if (x.style.transform === "translateY(-50%)") {
		x.style.transform = "translate(280px,-50%)";
	} else {
		x.style.transform = "translateY(-50%)";
	}
}
function taxTab(evt, taxName) {
	var i, tabcontent, tablinks, tName;
	tabcontent = document.getElementsByClassName("tabcontent");
	tName = document.getElementById(taxName).style.display;
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
	if (tName != "block")
		document.getElementById(taxName).style.display = "block";
	evt.currentTarget.className += " active";
}
function taxTab2(evt2, taxName2) {
	var i2, tabcontent2, tablinks2, tName2;
	tabcontent2 = document.getElementsByClassName("tb2");
	tName2 = document.getElementById(taxName2).style.display;
	for (i2 = 0; i2 < tabcontent2.length; i2++) {
		tabcontent2[i2].style.display = "none";
	}
	tablinks2 = document.getElementsByClassName("tl2");
	for (i2 = 0; i2 < tablinks2.length; i2++) {
		tablinks2[i2].className = tablinks2[i2].className.replace(" active", "");
	}
	if (tName2 != "block")
		document.getElementById(taxName2).style.display = "block";
	evt2.currentTarget.className += " active";
}
//  tuslamjiin heseg end duuslaaaaa

const myTimeout = setTimeout(alertOut, 5000);

function alertOut() {
	var change = document.getElementById("alertMsg");
	change.classList.add("alertOut");
} //  alert message fadeout
