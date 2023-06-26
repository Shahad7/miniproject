const username = document.getElementById('username');
const library = document.getElementById('library');
const duplicate = document.getElementById('duplicate');
const submitButton = document.getElementById('singup-submit');
let usernameDuplicate = false;
let libraryDuplicate = false;
const singupForm = document.getElementById('user-signup');

const checkDuplicate = (element, type) => {
	if (
		element != undefined &&
		element != null &&
		element != '' &&
		element.length != 0
	) {
		fetch(`http://127.0.0.1:8000/duplicate/${type}/${element}`)
			.then((response) => response.json())
			.then((data) => {
				if (data['result'] == 'duplicate') {
					duplicate.style.visibility = 'visible';
					if (type == 'library') {
						duplicate.textContent = 'library name already exists!';
						libraryDuplicate = true;
					} else {
						duplicate.textContent = 'username already exists!';
						usernameDuplicate = true;
					}
					submitButton.disabled = true;
					submitButton.style.backgroundColor = '#cd000073';
				} else {
					if (type == 'library') libraryDuplicate = false;
					else usernameDuplicate = false;
					if (usernameDuplicate) {
						duplicate.textContent = 'username already exists!';
						submitButton.disabled = true;
						submitButton.style.backgroundColor = '#cd000073';
					} else if (libraryDuplicate) {
						duplicate.textContent = 'library name already exists!';
						submitButton.disabled = true;
						submitButton.style.backgroundColor = '#cd000073';
					} else {
						duplicate.style.visibility = 'hidden';
						submitButton.disabled = false;
						submitButton.style.backgroundColor = '#cd0000';
					}
				}
			});
	}
};

username.addEventListener('input', () => {
	checkDuplicate(username.value, 'username');
});
library.addEventListener('input', () => {
	checkDuplicate(library.value, 'library');
});

const validateForm = (event) => {
	let emptyFields = false;
	['username', 'name', 'email', 'password', 'library'].forEach((element) => {
		item = document.getElementById(element);
		if (item != undefined) {
			item.value = item.value.trim();
			if (item.value == '' || item.value.length == 0) emptyFields = true;
		}
	});
	if (emptyFields == true) {
		duplicate.textContent = "fields can't be empty";
		duplicate.style.visibility = 'visible';
		event.preventDefault();
	} else {
		duplicate.textContent = '';
		duplicate.style.visibility = 'hidden';
		singupForm.submit();
	}
};

singupForm.addEventListener('submit', (event) => {
	validateForm(event);
});
