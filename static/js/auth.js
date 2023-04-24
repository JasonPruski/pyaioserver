const authForm = `
<input id="username" type="text" placeholder="email" value="" autofocus/><br/>
<input id="password" type="password" placeholder="password" value=""/><br/>
<button id="login">login</button>
<button id="register">register</button>`;

const validate = () => {
  const username = $("#username").val();
  const password = $("#password").val();
  return { username:username, password:password }
}

export const auth = () => {
    $("main").html(authForm);
    $("#login").click(() => {
        const data = validate();
        $.ajax({
            type: "POST",
            url: "/auth/login",
            data: data,
            success: (result) => {
                console.log(result);
            },
            failure: console.log
        });
      });
    $("#register").click(() => {
        const data = validate();
        $.ajax({
            type: "POST",
            url: "/auth/register", 
            data: data,
            success: function(result){
                console.log(result);
            },
            failure: console.log
        });
      });
}