$(function (){
    $("#captcha-btn").click(function (e){
        e.preventDefault()
        var email = $("input[name='email']").val()
        var errorMsg = $("input[name='email']").next(".invalid-feedback")
        if (email) {
            errorMsg.hide()
            btnTime(this)
            getVerificationCode(email, errorMsg)
        } else {
            errorMsg.show().text("请输入邮箱地址！")
        }
    })


    function getVerificationCode(email, errMsg) {
        $.ajax({
            url: "captcha/email?email=" + email,
            method: "GET",
            success: function (res) {
                errMsg.show().text(res.message)
            },
            fail: function (err) {
                errMsg.show().text(err)
            }
        })
    }
})



var time = 120
function btnTime(btn) {
    btn.disabled = true
    $("#captcha-btn").addClass('disabled')
    var timer = setInterval(function () {
        if (time == 0) {
            clearInterval(timer)
            btn.disabled = false
            $("#captcha-btn").removeClass('disabled')
            $("#captcha-btn").text("获取验证码")
            time = 120
        } else {
            $("#captcha-btn").text("还剩下" + time + "秒")
            time --
        }
    }, 1000)
}