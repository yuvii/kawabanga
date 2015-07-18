var fs	     = require('fs');
var chokidar = require('chokidar');
var less 	 = require('less');

var watcher  = chokidar.watch('style.less', {persistent: true});

//  -------------------------------

var SOURCE_FILE = 'style.less',
	OUT_FILE 	= 'style.css';

// --------------------------------

function createCSS() {
	var content = fs.readFileSync(SOURCE_FILE, {'encoding': 'utf-8'});
	

	less.render(content, function(e, output) {
		if (e) {
			for (err in e) {
				console.log(err + ': ' + e[err]);
			} 
			// throw e;
		} else {
			fs.writeFileSync(OUT_FILE, output.css);

			var d = new Date(),
				stamp = d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds();

			console.log('compiled: ' + stamp);
		}
	});



};


watcher.on('change', createCSS);