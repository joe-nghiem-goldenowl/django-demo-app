import { dateValidate } from "./validate.js";
import { getCookie, returnHome } from "./utils.js";

$(async function () {
    bindEvents(); 
});

function bindEvents(){
    $('#filter-btn').click(() => handleFilter());
    $('#search-btn').click(() => handleSearch());
    $('#search-input').keypress(function (e) { 
        if (e.which == 13){
            handleSearch();
        }
    });

    $('.currency-btn').click(function(){
        handleChangeCurrency($(this).first().text().trim());
    });


    $('.delete-project-btn').click(function(){
        handleDeleteProject($(this).attr('project-id'));
    });
}

function handleChangeCurrency(currencyUnit){
    $('#currency').val(currencyUnit);

    queryData();
}

function handleDeleteProject(projectId){
    $.ajax({
        type: "post",
        url: `./project/delete/${projectId}/`,
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        dataType: "json",
        complete: () => {
            returnHome();
        }
    });
}

function handleFilter(){
    let dateConvert = (date) => {
        let day = date.getDate(),
            month = date.getMonth() + 1,
            year = date.getFullYear();
        let getPrefix0 = (number) => {
            if (number < 10) return '0' + number;
            return number;
        }

        return `${year}-${getPrefix0(month)}-${getPrefix0(day)}`;
    };

    if (dateValidate()){
        queryData();
    }
}


function queryData(){
    window.location.href = '/?' + jQuery.param({
        from: $('#id_date_start').val(),
        to: $('#id_date_end').val(),
        name: $('#search-input').val(),
        currency: $('#currency').val(),
    });
}

function handleSearch(){
    let pattern = $('#search-input');

    if (!pattern.val()){
        pattern.addClass('input-error');
        alert("Error: Empty search data");
    } else {
        pattern.removeClass('input-error');
        queryData();
    }
}