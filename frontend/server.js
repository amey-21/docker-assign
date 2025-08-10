const express = require('express');
const path = require('path');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static HTML form
app.use(express.static(path.join(__dirname, 'public')));

// Handle form submission and forward to Flask backend
app.post('/submit', async (req, res) => {
    try {
        const response = await axios.post('http://backend:5000/calculate', req.body);
        res.send(`<h2>${response.data.message}</h2>`);
    } catch (error) {
        console.error(error);
        res.status(500).send('Error submitting data');
    }
});

app.listen(3000, () => {
    console.log('Frontend running on http://localhost:3000');
});
