const csv = require('csv-parser');
const express = require('express');
const bodyParser = require("body-parser");
const ejs = require("ejs");
const fs = require('fs');
const results = [];

const app = express();
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));


app.get("/", function(req, res) {
    fs.createReadStream('./Tweets/All-Tweets.csv')
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', () => {
            console.log(results);
            res.render("index", { tweets: results })
        });
});

app.listen(3001, function() {
    console.log("Server started on port 3001");
});