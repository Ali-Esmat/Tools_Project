import React, { Component }  from 'react';
import {BrowserRouter as Router, Route, Link, Redirect, Routes} from "react-router-dom"

/*<Router>
        <Routes>
              <Route path='/join' element={<RoomJoinPage />}/>
              <Route path='/create' element={<CreateRoomPage />}/>
              <Route path='/room/:roomCode' element={<Room/>}/>
              <Route path='/' element={<p> This is the Home Page </p>}/>
        </Routes>
</Router>*/
function Home(){

        return(
            <div className="mt-5 d-flex justify-content-left">
                This is Home page.
            </div>
        );
}

export default Home;