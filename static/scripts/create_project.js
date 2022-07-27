import {dateValidate, validate} from './validate.js';
import {loadDefaultLanguage, getCookie, returnHome} from './utils.js';

$(function () {
    bindEvents();
    loadDefaultLanguage();
});

function bindEvents(){
    let createBtn = $('#create-btn'),
        updateBtn = $('#update-btn');
    
    createBtn.click(() => handleCreateProject());
    updateBtn.click(() => handleUpdateProject());
}

function handleCreateProject(project){
    if (validate()){
        if (dateValidate()){
            let data = {
                name: $('#name').val(),
                description: $('#description').val(),
                date_start: $('#start-date').val(),
                date_end: $('#end-date').val(),
                developer: $('#developers').val(),
            }, headers = {
                'X-CSRFToken': getCookie('csrftoken'),
            };

            $.ajax({
                type: "post",
                url: "/project/",
                headers: headers,
                data: data,
                dataType: "json",
                success: function (response) {
                }
            });

            console.log(data);
        }
    }
}

function handleUpdateProject(project){
    if (validate()){
        if (dateValidate()){
            window.location.href = '/';
        }
    }
}