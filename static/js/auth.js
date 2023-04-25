import { loggedin } from '/js/data.js';

const authForm = `
    <input id="username" type="email" placeholder="email" value="" autofocus/><br/>
    <input id="password" type="password" placeholder="password" value=""/><br/>
    <button id="login"> login </button>
    <button id="register"> register </button>
`;

const validate = () => {
  const username = $("#username").val();
  const password = $("#password").val();
  return { username:username, password:password }
}

export const authentication = () => {
    if (loggedin) {
        loggedin = false;
        $("#auth-text").text("login");
        // to do, remove cookie, handle on backed?
    } else {
        $("main").html(authForm);
        $("#login").click(() => {
            const data = validate();
            $.ajax({
                type: "POST",
                url: "/auth/login",
                data: data,
                success: (authenticated) => {
                    console.log(authenticated);
                    loggedin = authenticated;
                    $("#auth-text").text("logout");
                },
                failure: console.log // remove in production
            });
        });
        $("#register").click(() => {
            const data = validate();
            $.ajax({
                type: "POST",
                url: "/auth/register", 
                data: data,
                success: function(authenticated){
                    console.log(authenticated);
                    loggedin = authenticated;
                    $("#auth-text").text("logout");
                },
                failure: console.log  // remove in production
            });
        });
    }
    
}