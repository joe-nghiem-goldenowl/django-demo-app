import {validate} from './validate.js';
import {loadDefaultLanguage, getCookie, returnHome} from './utils.js';

$(function () {
    loadProjects();
    bindEvents();
    loadDefaultLanguage();
});

function loadProjects(){
    $.ajax({
        type: "get",
        url: "/project/",
        dataType: "json",
        success: function (response) {
            response.forEach(e => {
                let item = $(`<option value=${e.id}>${e.name}</option>`)
                $('#projects').append(item);
            });

            let projectId = $('#projects').attr('project-id');

            $('#projects').val(projectId);
        }
    });

}

function bindEvents(){
    let addBtn = $('#add-btn'),
        updateBtn = $('#update-btn');
        
    addBtn.click(() => handleAdd());
    updateBtn.click(() => handleUpdate());
}

function handleAdd(){
    if (validate()){
        let data = {
            first_name: $('#first-name').val(),
            last_name: $('#last-name').val(),
            project: $('#projects').val(),
        },
            headers = {
                'X-CSRFToken': getCookie('csrftoken'),
        };

        $.ajax({
            type: "post",
            url: "/developer/",
            headers: headers,
            data: data,
            dataType: "json",
            success: function (data, textStatus, xhr) {
                console.log(data, textStatus, xhr);
            },
            complete: function (xhr, textStatus) {
                if (xhr.status == 201){
                    returnHome();
                }
            }
        });        
    }
}

function handleUpdate(){
    if (validate()){
        window.location.href = '/';
    } else {
        $('#alert-modal').modal('show');
    }
}