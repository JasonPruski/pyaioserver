import { authentication } from "/js/auth.js";

const data = {
    loggedin: false
};

$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "/auth/authenticated",
        success: (authenticated) => {
            console.log(authenticated);
            if (authenticated){
                loggedin = true;
                $("#auth-text").text("logout");
            }
        },
        failure: console.log // remove in production
    });
    $("#auth").click(() => authentication(data));
});