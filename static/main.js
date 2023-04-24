import { auth } from "./js/auth.js";

$(document).ready(function() {
    $("#auth").click(() => auth());
});