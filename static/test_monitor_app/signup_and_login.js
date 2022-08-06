var pswd = $('.password')
var conf = $('.conf-password')
var signup_btn = $('.signup-btn')

pswd.on('input', function(){
    console.log(pswd.val());
})

conf.on('input', function(){
    if (conf.val().length == 0) {
        conf.css('background', '#e0dede');
        console.log('asdf')
        signup_btn.attr('disabled', '');
    } else if (pswd.val() != conf.val()) {
        console.log("Pls Match");
        conf.css('background', 'red')
        signup_btn.attr('disabled', '');
    } else {
        console.log("matched");
        conf.css('background', '#e0dede');
        signup_btn.removeAttr('disabled');
    }
})

