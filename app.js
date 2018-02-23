var express = require("express");
var app     = express();
var path    = require("path");
var n2p     = require("./cm_modules/node2py");
var bodyParser = require("body-parser")

app.use(express.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/index.html'));
  //__dirname : It will resolve to your project folder.
});

app.post("/python", function(req, res){
  //console.log("Post Anfrage: " + JSON.stringify(req.body));
  let pyScript = req.body.script;
  n2p.setPyExec(pyScript);
  res.sendFile(path.join(__dirname + "/index.html"));
});

app.listen(3000);

console.log("Running at Port 3000");
