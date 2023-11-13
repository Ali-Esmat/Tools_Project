import logo from './logo.svg';
import './App.css';
import React, { Component }  from 'react';
import Clinc from './Clinc';
import Home from './Home';


/*<Router>
<Routes>
      <Route path='/join' element={<RoomJoinPage />}/>
      <Route path='/create' element={<CreateRoomPage />}/>
      <Route path='/room/:roomCode' element={<Room/>}/>
      <Route path='/' element={<p> This is the Home Page </p>}/>

</Routes>
</Router> */

function App() {
  return (
    <div className="container">
      <h3 className="m-3 d-flex justify-content-center">React JS Tutorial</h3>
      <Home />
      <Clinc />
    </div>
  );
}

export default App;
