console.log("Hello World");

function validateForm(){

	var name = document.getElementById('nameInput').value;
	var author = document.getElementById('authorInput').value;
	var yearPublished = document.getElementById('yearPublishedInput').value;
	var pages = document.getElementById('pagesInput').value;

	if(!name.length){
		alert("Must enter a name");
		return false;
	}
	else if (!author.length) {
		alert("Must enter an author");
		return false;
	}
	else if (!yearPublished.length) {
		alert("Must enter a year published");
		return false;
	}
	else if (!pages.length) {
		alert("Must enter a page amount");
		return false;
	}
	else {
		console.log(name, author, yearPublished, pages);
		return true;
	}
}