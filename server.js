var express = require('express');
var app = express();
var router = express.Router();
var path = __dirname ;

router.use( function ( req, res, next ) {
        res.header('Access-Control-Allow-Origin' , '*' );
  	res.header('Access-Control-Allow-Credentials', true);
	next();
});

router.get( '/memory_action', function ( req, res ) {
	res.sendFile(path+'/file_b.csv');
});

router.get( '/memory_transformation', function ( req, res ) {
	res.sendFile(path+'/file_m.csv');
});

app.use( '/', router );
app.listen(10050,function(){
	console.log("Running 10050");
});
