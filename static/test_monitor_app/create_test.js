var type = $("#test")
var has_essay = $(".has-essay")
var has_accomodation = $(".has-accommodations")
var sat = $(".sat")
var sat_acc = $(".sat_acc")
var act = $(".act")
var essay = $(".essay")
var essay_break = $(".before_essay_break")

$(document).ready(function(){
    has_essay.on("change", function(){
        if ($(this).is(":checked")) {
            $(this).val('true')
        } else {
            $(this).val('false')
        }
    })

    has_accomodation.on("change", function(){
        if ($(this).is(":checked")) {
            $(this).val('true')
        } else {
            $(this).val('false')
        }
    })
    sat.css('display', 'block') ;
    $(".test-type").on("change", function(){
        // sat with no accommodations/essay
        if (type.val() == 'SAT') {
            act.css('display', 'none') ;
            if (has_accomodation.val() == 'false') {
                sat.css('display', 'block') ;
                sat_acc.css('display', 'none') ;
                if (has_essay.val() == 'false') {
                    essay_break.css('display', 'none')
                    essay.css('display', 'none');
                } else {
                    essay_break.css('display', 'block')
                    essay.css('display', 'block');
                }
            } else {
                sat.css('display', 'none') ;
                sat_acc.css('display', 'block') ;
                if (has_essay.val() == 'false') {
                    essay_break.css('display', 'none')
                    essay.css('display', 'none');
                } else {
                    essay_break.css('display', 'block')
                    essay.css('display', 'block');
                }
            }

        } else {
            sat.css('display', 'none')
            sat_acc.css('display', 'none')
            act.css('display', 'block')
                if (has_essay.val() == 'false') {
                    essay_break.css('display', 'none')
                    essay.css('display', 'none');
                } else {
                    essay_break.css('display', 'block')
                    essay.css('display', 'block');
                }
                if (has_essay.val() == 'false') {
                    essay_break.css('display', 'none')
                    essay.css('display', 'none');
                } else {
                    essay_break.css('display', 'block')
                    essay.css('display', 'block');
                }
        }
    })
})