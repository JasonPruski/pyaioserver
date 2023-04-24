export const login = () => {
    $("button").click(function(){
        $.ajax({url: "/user", success: function(result){
          console.log(result);
        }});
      });
}