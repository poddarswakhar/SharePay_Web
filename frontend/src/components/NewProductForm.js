import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL, API_URL_D } from "../constants";

// file used to create new product, and edit the product form

class NewProductForm extends React.Component {
  // state variable and state management
  state = {
    productId: 0,
    productName: "",
    productOwnerName: "",
    Developers: "",
    scrumMasterName: "",
    startDate: "",
    methodology: ""
  };

  // mounting the form and setting the values
  componentDidMount() {
    if (this.props.products) {
      const { productId, productName, productOwnerName, Developers, scrumMasterName, startDate, methodology} = this.props.products;
      this.setState({ productId, productName, productOwnerName, Developers, scrumMasterName, startDate, methodology });
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
    this.state.Developers = this.state.Developers.toString().split(",");
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
          <Label for="productName">User 1 Name:</Label>
          <Input
            type="text"
            name="productName"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.productName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="productOwnerName">User 1 Wallet Address:</Label>
          <Input
            type="text"
            name="productOwnerName"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.productOwnerName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Developers">User 2 Name:</Label>
          <Input
            type="text"
            name="Developers"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.Developers)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="scrumMasterName">User 2 Wallet Address:</Label>
          <Input
            type="text"
            name="scrumMasterName"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.scrumMasterName)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="startDate">User 3 Name:</Label>
          <Input
            type="date-input"
            name="startDate"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.startDate)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="methodology">User 3 Wallet Address:</Label>
          <Input
            type="text"
            name="methodology"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="methodology">Service Name:</Label>
          <Input
            type="text"
            name="methodology"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="methodology">Service Wallet Address:</Label>
          <Input
            type="text"
            name="methodology"
            onChange={this.onChange}
            required
            value={this.defaultIfEmpty(this.state.methodology)}
          />
        </FormGroup>

        <FormGroup>
          <Label for="methodology">Individual Amount:</Label>
          <Input
            type="text"
            name="methodology"
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