var express = require("express");
var router  = express.Router();
var n2p     = require("../cm_modules/node2py");

router.post("/", function(req, res){
  let pyScript = req.body.script;
  let pyPhrase = req.body.phrase;
  n2p.setPyExec(pyScript, pyPhrase);
});


module.exports = router;
