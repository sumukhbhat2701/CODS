// const express = require('express');
// const app = express();
// const path = require('path');
// const spawn = require("child_process").spawn;
// const bodyParser = require('body-parser');
// // const Twitter = require('twitter');

// // var client = new Twitter({
// //     consumer_key: 'cFf7im7BH68xO9qh3zEsv3nFz',
// //     consumer_secret: '2QyodEVK63XYE5D9RFPAo0I53rhBOsNocQGpGB8rapmEqxDnJi',
// //     access_token_key: '1265319352795975680-EJBIU55ZHZnjn8svR420cqVuU9evRL',
// //     access_token_secret: 'i8h2utF6b2l2Uh7Vpg6c2mnPOO1CuthGdbyWtHSWdIURP'
// // });

// // var params = { screen_name: 'nodejs' };
// // client.get('statuses/user_timeline', params, function(error, tweets, response) {
// //     if (!error) {
// //         console.log(tweets);
// //     }
// // });

// app.set('view engine', 'ejs')

// app.use(bodyParser.urlencoded({ extended: false }));

// app.get('/', (req, res) => {
//     res.sendFile(path.join(__dirname, 'index.html'));
// });

// app.listen(3000, () => console.log("Listening at port 3000...."));
const express = require('express')
const { spawn } = require('child_process');
const app = express()
const port = 3000
app.get('/', (req, res) => {

    var dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['script1.py']);
    // collect data from script
    python.stdout.on('data', function(data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
    });

})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))