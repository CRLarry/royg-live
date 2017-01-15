$(document).ready(function() {
	console.log("ready");
});

var allColors = ["rgb(231, 76, 60)", "rgb(211, 84, 0)", "rgb(243, 156, 18)", "rgb(46, 204, 113)", "rgb(52, 152, 219)", "rgb(155, 89, 182)"];


$(".backdrop").on("click", function() {
	var color = allColors[Math.floor(Math.random() * allColors.length)];

	$(this).css({"background-color": color});
	$(".submit").css({"background-color": color});

});
