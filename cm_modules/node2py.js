var { exec, spawn } = require("child_process");

exports.setPyExec = function(pyFile, pyPhrase) {
  exec("python python/" + pyFile + " '" + pyPhrase + "' ", (err, stdout, stderr) => {
   if (err) {
     console.error(err);
     return;
   }
   console.log(stdout);
 });
};
