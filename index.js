const debug     = false;


const path      = require("path");
const input     = path.join(__dirname, "_input.txt");
const output    = path.join(__dirname, "_output.txt");
const fs        = require("fs");

const regexp    = /\[([0-9]|0[0-9]|1[0-9]):[0-5][0-9]\s((AM)|(PM))\]/g;

fs.readFile(input, 'utf8', (error, data) => {
    if(error) {
        return console.error(error);
    }
    let lines = data.split('\r\n');
    if (debug) {
        console.log(data);
        console.log(lines);
    }
    let match;
    let finalData = '';
    for(i = 0; i < lines.length; i++) {
        match = lines[i].match(regexp);
        if (debug) {
            console.log(lines[i])
            console.log(match);
        }
        if(match != null) {
            lines[i] = lines[i].replace(match[0],'');
        }
        finalData = finalData + lines[i] + '\r\n';
    }
    fs.writeFile(output, finalData, error => {
        if (error) console.error(error)
        else console.log("Success!");
    });
})