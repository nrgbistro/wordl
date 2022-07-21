const express = require("express");
const path = require("path");
const app = express();
const port = process.env.PORT || 5000;
var bodyParser = require('body-parser'); // Calling body-parser to handle req object from POST requests

// This displays message that the server running and listening to specified port
app.listen(port, () => console.log(`Listening on port ${port}`));
// Have Node serve the files for our built React app
app.use(express.static(path.resolve(__dirname, "../build")));
// Parse application/json (Parse incoming req object as a JSON Object)
app.use(bodyParser.json());

// Create a GET route
app.get("/api", (req, res) => {
	res.json({ word: "test" });
});

app.get("*", (req, res) => {
	res.sendFile(path.resolve(__dirname, "../build", "index.html"));
});