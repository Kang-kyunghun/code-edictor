let editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/mono_industrial");
    editor.session.setMode("ace/mode/python");
}

function changeLanguage() {

    let language = $("#languages").val();

    if(language == 'python')editor.session.setMode("ace/mode/python");
    else if(language == 'javascript')editor.session.setMode("ace/mode/javascript");
}

function executeCode() {
    console.log("hello")
    $.ajax({

        url: "http://127.0.0.1:8000/ide",

        method: "POST",
        
        contentType: "apllication/json",

        data: JSON.stringify({
            language: $("#languages").val(),
            code: editor.getSession().getValue()
        }),

        success: function(response) {
            console.log(response)
            $(".output").text(response.message)
        }
    })
}
