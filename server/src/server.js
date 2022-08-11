

const app = require("./index");

const connectDB = require("./configs/db");

app.listen(5000, async () => {
	try {
		await connectDB();
		console.log("Listening at 5000...");
	} catch (err) {
		console.log(err);
	}
});