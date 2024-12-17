const mongoose = require('mongoose');
const dotenv = require('dotenv');

process.env.MONGO_URI = "mongodb+srv://elm:FoundationOMEN05-1@virtualeventorganizer.wmum2.mongodb.net/?retryWrites=true&w=majority&appName=VirtualEventOrganizer";
dotenv.config();

const connectDB = async () => {
  try {
    // Remove deprecated options (no longer needed)
    await mongoose.connect(process.env.MONGO_URI);
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    process.exit(1);
  }
};

module.exports = connectDB;
