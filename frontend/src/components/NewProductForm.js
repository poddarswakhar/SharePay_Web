import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL, API_URL_D } from "../constants";

// file used to create new product, and edit the product form

class NewProductForm extends React.Component {
  // state variable and state management
  state = {
    id: 0,
    user1_name: "",
    user1_wal: "",
    user2_name: "",
    user2_wal: "",
    user3_name: "",
    user3_wal: "",
    dest_wal: "",
    ind_val: "",
    serv_name: "",
    serv_acc_id: ""
  };

  // mounting the form and setting the values
  componentDidMount() {
    if (this.props.products) {
      const { user1_name, user1_wal, user2_name, user2_wal, user3_name, user3_wal, dest_wal, ind_val, serv_name, serv_acc_id} = this.props.products;
      this.setState({ user1_name, user1_wal, user2_name, user2_wal, user3_name, user3_wal, dest_wal, ind_val, serv_name, serv_acc_id });
    }
  }

  // listener, to change the state of the variables
  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  // this the function that is called when confirmed is clicked, uses axios POST request to create the new product, if the creation of product
  // fails if there is an error, an alert is shown to the user that "WARNING: Product is not Created! Check the fields again! Make sure the Date is in desired format!" 
  // and error is logged on console
  createProduct = e => {
    //this.state["Developers"] = this.state["Developers"].split(",");
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    }).catch(error => {
      alert("WARNING: Product is not Created! Check the fields again! Make sure the Date is in desired format!");
      console.error(error);
      //this.props.resetState();
    });
  };

  // this is the method for the edit option and called when it is confiemd from the edit button, uses axios to make PUT request to update the product
  // if it failes for error, an alert is shown to the user "WARNING: Product is not Updated! Check the fields again! Make sure the Date is in desired format!"
  // and error is logged on console
  editProduct = e => {
    //this.state["Developers"] = this.state["Developers"].split(",");
    e.preventDefault();
    this.state.Developers = this.state.Developers.toString().split(",");
    axios.put(API_URL_D + "?id=" + this.state.productId, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    }).catch(error => {
      alert("WARNING: Product is not Updated! Check the fields again! Make sure the Date is in desired format!");
      console.error(error);
      this.props.resetStates();
    });
  };

  // default check
  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  // Again the render part is self sufficient to understand, using elements with some inline css, with all madatoy fields
  render() {
    return (
      <Form onSubmit={this.props.products ? this.editProduct : this.createProduct}>
        <FormGroup>
          <Label for="user1_name">User 1 Name:</Label>
          <Input
            type="text"
            name="user1_name"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.productName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="user1_wal">User 1 Wallet Address:</Label>
          <Input
            type="text"
            name="user1_wal"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.productOwnerName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="user2_name">User 2 Name:</Label>
          <Input
            type="text"
            name="user2_name"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.Developers)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="user2_wal">User 2 Wallet Address:</Label>
          <Input
            type="text"
            name="user2_wal"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.scrumMasterName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="user3_name">User 3 Name:</Label>
          <Input
            type="text"
            name="user3_name"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.startDate)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="user3_wal">User 3 Wallet Address:</Label>
          <Input
            type="text"
            name="user3_wal"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="dest_wal">Service Name:</Label>
          <Input
            type="text"
            name="dest_wal"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="ind_val">Service Wallet Address:</Label>
          <Input
            type="text"
            name="ind_val"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="serv_name">Individual Amount:</Label>
          <Input
            type="text"
            name="serv_name"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="serv_acc_id">Service Account ID:</Label>
          <Input
            type="text"
            name="serv_acc_id"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>
        <Button style={{ backgroundColor: "black" }}>Confirm</Button>
      </Form>
    );
  }
}

export default NewProductForm;