var express = require("express");
var app     = express();
var path    = require("path");
var n2p     = require("./cm_modules/node2py");

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/index.html'));
  //__dirname : It will resolve to your project folder.
});

app.get("/python", function(reg, res){
  n2p.setPyExec("test.py");
  res.sendFile(path.join(__dirname + "/index.html"));
});

app.listen(3000);

console.log("Running at Port 3000");
