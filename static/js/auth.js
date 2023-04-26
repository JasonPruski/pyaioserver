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

export const authentication = (data) => {
    if (data.loggedin) {
        data.loggedin = false;
        let authText = $("#auth-text")
        authText.text("login");
        authText.css({ "color": "black"});
        // to do, remove cookie, handle on backed?
    } else {
        $("main").html(authForm);
        $("#login").click(() => {
            const login = validate();
            $.ajax({
                type: "POST",
                url: "/auth/login",
                data: login,
                success: (authenticated) => {
                    console.log(authenticated);
                    data.loggedin = authenticated;
                    if (authenticated) {
                        let authText = $("#auth-text")
                        authText.text("logout");
                        authText.css({ "color": "red"});
                    }
                },
                failure: console.log // remove in production
            });
        });
        $("#register").click(() => {
            const login = validate();
            $.ajax({
                type: "POST",
                url: "/auth/register", 
                data: login,
                success: function(authenticated){
                    console.log(authenticated);
                    data.loggedin = authenticated;
                    if (authenticated) {
                        let authText = $("#auth-text")
                        authText.text("logout");
                        authText.css({ "color": "red"});
                    }
                },
                failure: console.log  // remove in production
            });
        });
    }
    
}