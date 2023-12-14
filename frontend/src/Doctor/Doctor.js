import React, { useEffect } from "react";
import axios from "axios";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { useState } from "react";


// this is to retrieve the csrf token
/*
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].toString().replace(/^([\s]*)|([\s]*)$/g, "");
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
*/

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;

const client = axios.create({
  baseURL: process.env.REACT_APP_BE_URL,
});

const getDoctorSlotsUrl = (user_id) => {
  return `/api/doctor_slots/${user_id}`;
};

const Doctor = (props) => {
  //maintaining the state of the elements in the display:
    // 1- The logged in doctor slots
    // 2- All the slots for all the doctors
    // 3- The details of the slot to be created by the doctor
  const [slots, setSlots] = useState([]);
  const [all_slots, set_all_slots] = useState([]);
  const [date, setDate] = useState("");
  const [start_hour, setHour] = useState("");



  // used to force a re-render
  const [, forceRender] = useState(undefined);
  const Rerender = () => {
    forceRender((prev) => !prev);
  };

  // function to fetch all the logged in doctor slots from the database
  function getDoctorSlots() {
    //var csrftoken = getCookie("csrftoken");
    //axios.defaults.xsrfHeaderName = props.csrftoken;
    var user_id = props.user_id;
    var url = getDoctorSlotsUrl(user_id);
    client.get(url).then(function (res) {
      console.log(res.data);
      setSlots(res.data);
    });
  }
  // function to fetch all the doctor slots in the database
  function getAllSlots() {
    //var csrftoken = getCookie("csrftoken");
    //console.log(props.csrftoken)
    //axios.defaults.xsrfHeaderName = props.csrftoken;
    //console.log(csrftoken)
    client.get("/api/doctor_slots/").then(function (res) {
      console.log(res.data);
      set_all_slots(res.data);
    });
  }

  // update the display by calling the functions at the start and whenever a change happens in the states.
  useEffect(() => {
    getDoctorSlots();
    getAllSlots();
  }, [slots, all_slots]);

  // function to handle slot creation after the doctor entered the details of the slot
  function submitSlotDetails(e) {
    e.preventDefault();
    //var csrftoken = getCookie("csrftoken");
    //axios.defaults.xsrfHeaderName = props.csrftoken;
    //console.log(props.csrftoken)
    client
      .post("api/doctor_slots/", {
        date: date,
        start_hour: start_hour,
        doctor: props.user_id,
        status: "AVALIABLE",
      })
      .then(function (res) {
        Rerender();
      });
  }

  return (
    <div>
      <h1>Doctor Component</h1>
      <div>
        my slots
      </div>
      <ul>
        {slots.map((slot) => (
          <li key={slot.slot_id}>
            <h3>{slot.slot_id}</h3>
            <h3>{slot.date}</h3>
            <h3>{slot.start_hour}</h3>
            <h3>{slot.doctor}</h3>
            <h3>{slot.status}</h3>
          </li>
        ))}
      </ul>
      <div>
        all slots
      </div>
      <ul>
        {all_slots.map((slot) => (
          <li key={slot.slot_id}>
            <h3>{slot.slot_id}</h3>
            <h3>{slot.date}</h3>
            <h3>{slot.start_hour}</h3>
            <h3>{slot.doctor}</h3>
            <h3>{slot.status}</h3>
          </li>
        ))}
      </ul>
      <div className="center">
        <Form onSubmit={(e) => submitSlotDetails(e)}>
          <Form.Group className="mb-3" controlId="formBasicUsername">
            <Form.Label>Date</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter Date"
              value={date}
              onChange={(e) => {
                setDate(e.target.value);
              }}
            />
          </Form.Group>
          <Form.Group className="mb-3" controlId="formBasicUsername">
            <Form.Label>Start Hour</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter Hour"
              value={start_hour}
              onChange={(e) => {
                setHour(e.target.value);
              }}
            />
          </Form.Group>
          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </div>
    </div>
  );
};

export default Doctor;


/*
    put inside the use effect
    const getDoctorSlots = async () => {
      //var csrftoken = getCookie("csrftoken");
      //axios.defaults.xsrfHeaderName = props.csrftoken;
      var user_id = props.user_id;
      var url = getDoctorSlotsUrl(user_id);
      await client.get(url).then(function (res) {
        console.log(res.data);
        currentSlots = res.data;
        setSlots(res.data);
        //return slots;
      });
    } */