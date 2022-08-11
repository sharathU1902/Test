const mongoose = require("mongoose");

const connectDB = () => {
	return mongoose.connect(
		"mongodb+srv://Mohak:mohak1234@cluster0.gkeimsu.mongodb.net/?retryWrites=true&w=majority"
	);
};

module.exports = connectDB;

