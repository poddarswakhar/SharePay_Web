import React, { Component } from "react";
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";
import { Form, FormGroup, Input, Label } from "reactstrap";
import { API_URL_S } from "../constants";

class SignModal extends Component {
  state = {
    contractAdd: "",
    privateKey: "",
    publicKey: ""
  };

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createProduct = e => {
    e.preventDefault();
    const data = {
      contractAdd: this.state.contractAdd,
      privateKey: this.state.privateKey,
      publicKey: this.state.publicKey
    };
    axios.post(API_URL_S + "?pub=" + data.publicKey +"&pri=" + data.privateKey + "&con=" + data.contractAdd).then(res => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  render() {
    return (
      <Modal isOpen={this.props.isOpen} toggle={this.props.toggle}>
        <ModalHeader toggle={this.props.toggle}>Sign Contract</ModalHeader>
        <ModalBody>
          <form onSubmit={this.createProduct}>
            <label>Contract Address:</label>
            <br></br>
            <input type="text" name="contractAdd" value={this.state.contractAdd} onChange={this.onChange} style={{borderRadius: "5px", width: "100%"}} required/>
            <br></br><br></br>
            <label>Private Key (0x...):</label>
            <br></br>
            <input type="text" name="privateKey" value={this.state.privateKey} onChange={this.onChange} style={{borderRadius: "5px", width: "100%"}} required />
            <br></br><br></br>
            <label>Public Key (0x...):</label>
            <br></br>
            <input type="text" name="publicKey" value={this.state.publicKey} onChange={this.onChange} style={{borderRadius: "5px", width: "100%"}} required />
          </form>
        </ModalBody>
        <ModalFooter>
          <Button style={{ backgroundColor: "black" }} onClick={this.createProduct}>
            Sign
          </Button>{" "}
          <Button type="submit" color="secondary" onClick={this.props.toggle}>
            Cancel
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}

export default SignModal;