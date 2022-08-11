

const express = require("express");
const router = express.Router();
const User = require("../models/usermodel");



router.get("/", async (req, res) => {
  try {
    const users = await User.find().lean().exec();
    return res.send(users);
  } catch (error) {
    console.log(error);
  }
});


router.post("/", async (req, res) => {

    try {
    const users = await User.create(req.body);
    
    return res.send(users);
  } catch (error) {
    console.log(error);
  }
});


router.get("/:id", async (req, res) => {
  try {
    const users = await User.findById(req.params.id).lean().exec();
    return res.send(users);
  } catch (error) {
    console.log(error);
  }
});

module.exports = router;
