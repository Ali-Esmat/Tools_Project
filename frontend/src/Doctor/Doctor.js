import React from "react";
import axios from "axios";


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].toString().replace(/^([\s]*)|([\s]*)$/g, "");
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const client = axios.create({
    baseURL: "http://127.0.0.1:8000",
  });

const Doctor = () =>{

    function getDoctorSlots() {
        var csrftoken = getCookie('csrftoken');
        axios.defaults.xsrfHeaderName = csrftoken;
        client
          .post("/api/register", {
            user_name: user_name,
            user_type: user_type,
            password: password,
          })
          .then(function (res) {

            client
              .post("/api/login", {
                user_name: user_name,
                password: password,
              })
              .then(function (res) {
                setCurrentUser(true);
              });
          });
      }

    return <h1>Doctor Component</h1>
}

export default Doctor;