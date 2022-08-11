const cors = require("cors")

const express= require("express")
const app = express()

app.use(cors())
app.use(express.json())
const userController = require("./controllers/usercontroller")


app.use("/user", userController)


module.exports = app; 