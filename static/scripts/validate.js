export function validate(){
    let valid = true;
    $('.required').each(function () {
        let value = $(this).val();
        if (!value){
            valid = false;
            $(this).addClass('input-error');
            alert("Error occurs: Empty field(s)");
        } else {
            $(this).removeClass('input-error');
        }
    });

    return valid;
}

export function dateValidate(){
    let startDate = $('#id_date_start'),
        endDate = $('#id_date_end');

    if (!(startDate.val() && endDate.val())){
        autoSetWarn(() => alert("Date must not be empty!"), startDate, endDate);
        return false;
    } else {
        removeWarn(startDate, endDate);
    }
    // start date must be earlier than end date
    if ((startDate.val() > endDate.val())){
        setWarn(startDate, endDate);
        alert("Start date must be earlier than end date");
        return false;
    } else {
        removeWarn(startDate, endDate);
    }

    return true;
}

export function setWarn(...args){
    args.forEach(e => {
        e.addClass('input-error');
    })
};

export function removeWarn(...args){
    args.forEach(e => {
        e.removeClass('input-error');
    })
};

export function autoSetWarn(func, ...args){
    args.forEach(e => {
        if (e.val()){
            removeWarn(e);
        } else {
            setWarn(e);
        }
    })

    func();
}