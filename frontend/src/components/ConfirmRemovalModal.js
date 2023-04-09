import React, { Component, Fragment } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";
import { API_URL_D } from "../constants";

// File and functionality of the component that pops up when Delete is clicked

class ConfirmRemovalModal extends Component {
  // state tracking and management
  state = {
    modal: false
  };

  // toggle track for the viewing
  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  // function to delete the prodyct when confirmed, takes in the primary key (productID), and use the axios DELETE request, to delete that data,
  // if there is an error, an alert is shown to the user that "ERROR: Couldn't Delete the Product! Check the Console Log" and error is logged on console
  deleteProduct = pk => {
    axios.delete(API_URL_D + "?pk=" + pk).then(() => {
      this.props.resetState();
      this.toggle();
    }).catch(error => {
      alert("ERROR: Couldn't Delete the Product! Check the Console Log");
      console.error(error);
      this.props.resetState();
    });
  };

  // Again the render part is self sufficient to understand, using elements with some inline css
  render() {
    return (
      <Fragment>
        <Button color="danger" onClick={() => this.toggle()}>
          Remove
        </Button>
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>
            Do you really want to delete this group?
          </ModalHeader>

          <ModalFooter>
            <Button type="button" onClick={() => this.toggle()} style = {{backgroundColor: "black"}}>
              Cancel
            </Button>
            <Button
              type="button"
              color="danger"
              onClick={() => this.deleteProduct(this.props.pk)}
            >
              Yes
            </Button>
          </ModalFooter>
        </Modal>
      </Fragment>
    );
  }
}

export default ConfirmRemovalModal;