var { exec, spawn } = require("child_process");

exports.setPyExec = function(pyFile) {
  exec("python python/" + pyFile, (err, stdout, stderr) => {
   if (err) {
     console.error(err);
     return;
   }
   console.log(stdout);
 });
};
