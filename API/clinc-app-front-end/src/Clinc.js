import React from 'react';
import Patient from './Patient';
import Doctor from './Doctor';

function Clinc () {
  return (
    <div className="mt-5 d-flex justify-content-left">
        <Patient/>
        <Doctor/>
    </div>
  );
};

export default Clinc;