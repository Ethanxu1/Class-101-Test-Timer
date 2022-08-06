$(document).ready(function() {
    function getTableData(table) {
        var data = [];
        table.find('tr').each(function (rowIndex, r) {
            var cols = [];
            $(this).find('th,td').each(function (colIndex, c) {
                var a = c.textContent.trim().split(' ')
                data.push(a[a.length - 1]);
            });
        });
        return data;
    }
    
    var times = getTableData($('.section-times'))
    var time = $('.time')
    var start = $('.start')
    var stop = $('.stop')
    var rtimer = $('.restart-test')
    var rsection = $('.restart-section')
    
    console.log(times)
    
    // start.on('click', function(){
    //     times.val() = "hello"
    // })
    //[21:32, 12, 12:15]
    console.log(time.val())
    var min = 10
    var sec = 5
    var total = min * 60 + sec
    time.html(min + ":" + sec)
    var a = undefined
    start.on('click', function(){
        start.attr('disabled', '')
        stop.removeAttr('disabled')
        a = setInterval(function(){
            if (total <= 0) {
                console.log('stop')
                clearInterval(a)
            } else {
                total--
                minutes = Math.floor(total / 60)
                seconds = total % 60
                time.html(minutes + ':' + seconds)
                console.log(total)
            }
        }, 1000)
    })
    stop.on('click', function(){
        start.removeAttr('disabled')
        stop.attr('disabled', '')
        clearInterval(a)
    })
    rsection.on('click', function(){
        start.removeAttr('disabled')
        stop.attr('disabled', '')
        time.html(min + ":" + sec)
        total = min * 60 + sec
        clearInterval(a)

    })
})
