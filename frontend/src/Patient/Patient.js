import React from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { useState } from "react";

  const client = axios.create({
    baseURL: process.env.REACT_APP_BE_URL,
  });

  const getAppointmentsUrl = (user_id) => {
    return `/api/appointments/${user_id}`;
  };

const Patient = () =>{

    return <h1>Patient Component</h1>

}

export default Patient;