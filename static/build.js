var Vulcanize = require('vulcanize');
var minify = require('html-minifier').minify;
var fs = require('fs');
var target = '/static/elements/swot-app.html';

var vulcan = new Vulcanize({
  abspath: '../',
  stripComments: true
});

vulcan.process(target, function(err, inlinedHtml) {
	if (err) {
		console.log(err);
	}
	else {
		fs.writeFile('build.html', inlinedHtml, function (err) {
		  	if (err) {
				console.log(err);
			}
		  	console.log('Vulcanized!');
		});
	}
});


