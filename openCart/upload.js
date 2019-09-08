function createUpload() {
    var f = document.createElement("form");
    f.id = "form-upload";
    f.style.display = "block";
    f.enctype = "multipart/form-data";
    inp = document.createElement("input");
    inp.type = "file";
    inp.name = "file";
    f.appendChild(inp);
    body = document.getElementsByTagName("body")[0];
    body.insertBefore(f, body.firstChild);
}

