/**
 * Created by Administrator on 2018/3/20.
 */


$(document).ready(function () {


    $("#login").click(function () {
        var username = $("#username").val();
        var password = $("#password").val();
        console.log(username,password);
        $.ajax({
            url:"/api/login_check",
            method:"POST",
            data:{"password":password,"username":username},
            success:function (res) {
                console.log(res);
                if(res.code==2001){
                    window.location.href="/";
                }
            }

        })
    })

    $("#logout").click(function () {
        // alert("ok")
        $.ajax({
            url:"/api/logout",
            method:"POST",
            data:{},
            success:function (res) {
                console.log(res);
                if(res.code==2001){
                    window.location.href="/";
                }
            }

        })
    })

})