const express = require('express');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(express.json()); // Middleware to parse JSON data

const PORT = process.env.PORT || 5000;

app.get('/', (req, res) => {
  res.send('Virtual Event Organizer API is running');
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

const connectDB = require('./db');
connectDB();

const userRoutes = require('./routes/userRoutes');
app.use('/api/users', userRoutes);

module.exports = connectDB;
