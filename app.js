var express = require("express");
var app     = express();
var path    = require("path");
var bodyParser = require("body-parser")
var py      = require("./routes/python.js");

app.use(express.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/index.html'));
});

app.use("/python", function(req, res, next){
  res.sendFile(path.join(__dirname + "/index.html"));
  next();
});

app.use("/python", py);

app.listen(3000);

console.log("Running at Port 3000");
