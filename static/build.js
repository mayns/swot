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
		var result = minify(inlinedHtml, {
			minifyJS: true,
			customAttrAssign: [/\$=/],
			keepClosingSlash: true,
			removeComments: true,
			collapseWhitespace: true,
			removeStyleLinkTypeAttributes: true,
			removeScriptTypeAttributes: true,
		  	removeAttributeQuotes: true
		});

		fs.writeFile('templates/swots/index.html', result, function (err) {
		  	if (err) {
				console.log(err);
			}
		  	console.log('Vulcanized!');
		});
	}
});


