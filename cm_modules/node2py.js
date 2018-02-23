var { exec, spawn } = require("child_process");
//var python = spawn("python " + pyExec);

/*
python.stdout.on("data", (data) => {
  console.log('stdout: ${data}');
});

python.stderr.on("data", (data) => {
  console.log('stderr: ${data}')
});

python.on("close", (code) =>{
  console.log("child_process exited with code ${code}")
});
*/

exports.setPyExec = function(pyFile) {
  exec("python " + pyFile, (err, stdout, stderr) => {
   if (err) {
     console.error(err);
     return;
   }
   console.log(stdout);
 });
};
