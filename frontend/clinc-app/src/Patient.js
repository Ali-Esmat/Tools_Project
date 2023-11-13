import React, {Component} from 'react';
import {Table} from 'react-bootstrap';

import {Button,ButtonToolbar} from 'react-bootstrap';
import  AddAppModal  from './AddAppModal';
import  EditAppModal from './EditAppModal';

export default class Department extends Component{

      constructor(props){
          super(props);
          this.state= {
            appointments:[],
            addModalShow:false,
            editModalShow:false
          }
      }

      // attempts to get patient appointments
      refreshList(){
          fetch(process.env.REACT_APP_API+'appointments')
          .then(response=>response.json())
          .then(data=>{
              this.setState({appointments:data});
          });
      }

      componentDidMount(){
          this.refreshList();
      }

      componentDidUpdate(){
          this.refreshList();
      }

      deleteDep(appid){
          if(window.confirm('Are you sure?')){
              fetch(process.env.REACT_APP_API+'appointment/'+appid,{
                  method:'DELETE',
                  header:{'Accept':'application/json',
              'Content-Type':'application/json'}
              })
          }
      }

    /*
    Example functions
    const alertName = () => {
      alert(name);
    };

    const handleNameInput = e => {
      setName(e.target.value);
    };*/
    render(){
        const {appointments, appid}=this.state;
        let addModalClose=()=>this.setState({addModalShow:false});
        let editModalClose=()=>this.setState({editModalShow:false});

      return (
        <div>
          <h2>MY Appointments</h2>
                  <Table className="mt-4" striped bordered hover size="sm">
                      <thead>
                          <tr>
                          <th>Appointment_id</th>
                          <th>Slot_Date</th>
                          <th>Slot_Time</th>
                          <th>Doctor Name</th>
                          <th>Options</th>
                          </tr>
                      </thead>
                      <tbody>
                          {appointments.map(appointment=>
                              <tr key={appointment.Appointment_id}>
                                  <td>{appointment.Appointment_id}</td>
                                  <td>Dummy Data for slot date</td>
                                  <td>Dummy Data for slot time</td>
                                  <td>Dummy Data for Doctor Name</td>
                                  <td>
                                      <ButtonToolbar>
                                        <Button className="mr-2" variant="info"
                                            onClick={()=>this.setState({editModalShow:true,
                                            appid:appointment.Appointment_id})}>
                                            Edit
                                        </Button>

                                        <Button className="mr-2" variant="danger"
                                            onClick={()=>this.deleteDep(appointment.Appointment_id)}>
                                            Delete
                                        </Button>

                                        <EditAppModal show={this.state.editModalShow}
                                            onHide={editModalClose}
                                            appid={appid}/>
                                      </ButtonToolbar>
                                  </td>
                              </tr>)}
                      </tbody>
                  </Table>
                  <ButtonToolbar>
                      <Button variant='primary'
                          onClick={()=>this.setState({addModalShow:true})}>
                          Add Appointment
                      </Button>
                      <AddAppModal show={this.state.addModalShow}
                          onHide={addModalClose}/>
                  </ButtonToolbar>
        </div>);

    };
};
