var Vulcanize = require('vulcanize');
var minify = require('html-minifier').minify;
var fs = require('fs');
var zlib = require('zlib');
var target = '/static/templates_dev/swots/index.html';

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

		var gzipped = zlib.gzipSync(result);

		fs.writeFile('templates/swots/index.html.gz', gzipped, function (err) {
		  	if (err) {
				console.log(err);
			}
		  	console.log('Vulcanized!');
		});
	}
});


