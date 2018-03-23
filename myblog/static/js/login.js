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
                    //保存cookie
                    alert(res.userid);
                    setCookie('userid', res.userid, { expires: 7 });
                    window.location.href="/";
                }else if (res.code==4001){
                    $(".errors").text("用户名或者密码错误，请重试").css({"color":"red"});
                }else{

                }
            }

        })
    });

    $("#logout").click(function () {
        // alert("ok")
        $.ajax({
            url:"/api/logout",
            method:"POST",
            data:{"id":1},
            success:function (res) {
                console.log(res);
                if(res.code==2001){
                    window.location.href="/";
                }
            }

        })
    })

});