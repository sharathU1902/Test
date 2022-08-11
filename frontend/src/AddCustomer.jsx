import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
import "./AddCustomer.css"


const AddCustomer = () => {
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    age: "",
  });

  const [formErrors, setFormErrors] = useState([]);
  const [isSubmit, setSubmit] = useState(false)

  function handleChange(e) {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    setFormErrors(validate(formData));

    setSubmit(true)

   
  }

  useEffect(() => {
    if (formErrors.length === 0 && isSubmit===true) {
      axios
        .post("http://localhost:5000/user", formData)
        .then(function (response) {
          console.log(response.data);
          alert("customer added");
        })
        .catch(function (err) {
          console.log(err);
        });
 
    } 
    // eslint-disable-next-line
  }, [formErrors]);

  const validate = (values) => {
    const errors = [];

    //validate age
    if (+values.age > 50 || +values.age < 10) {
      errors.push("Age should be in between 10 to 50 years");
    }

    if(!values.first_name){
      errors.push("first name can not be empty");
    }

  
    if(!values.last_name){
      errors.push("last name can not be empty");
    }

    if(!values.age){
      errors.push("age can not be empty");
    }

    if(!values.email){
      errors.push("email can not be empty");
    }


    return errors;
  };

  return (
    <div className="App">

   

    <form className='addstudent' onSubmit={handleSubmit}>
    <h1> Customer Information </h1>
      <div>
        Firstname:{" "}
        <input
          type='text'
          name='first_name'
          className='first_name'
          value={formData.first_name}
          placeholder='enter first name'
          pattern= "^[A-Za-z]{3,16}$"
          required
          onChange={handleChange}
        />
      </div>

      <div>
        {" "}
        Last Name:
        <input
          type='text'
          name='last_name'
          className='last_name'
          placeholder='enter last name'
          value={formData.last_name}
          pattern= "^[A-Za-z]{3,16}$"
          required
          onChange={handleChange}
        />
      </div>

      <div>
        {" "}
        Email:
        <input
          type='email'
          name='email'
          className='email'
          placeholder='enter email'
          value={formData.email}
          onChange={handleChange}
        />
      </div>

      
      <div>
        Age{" "}
        <input
          type='number'
          name='age'
          className='age'
          placeholder='enter age'
          value={formData.age}
          onChange={handleChange}
        />
      </div>
      

      

      {/* <input className='submit' type='submit' value='Submit' /> */}
      <button type='submit'> Submit</button>

      {<div className='error'> {formErrors} </div>}
    </form>
    </div> 
  );
};

export default AddCustomer;
