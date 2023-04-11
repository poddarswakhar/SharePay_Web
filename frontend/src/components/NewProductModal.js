import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewProductForm from "./NewProductForm";

// file for the crate and edit product button and calling the form

class NewProductModal extends Component {
  // state track abnd management
  state = {
    modal: false
  };

  // toggle track for the viewing
  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  // Again the render part is self sufficient to understand, using elements with some inline css, Note reusing the same NewProductForm for both edit and creating new products
  render() {
    const create = this.props.create;

    var title = "Editing Product";
    var button = <Button style={{ backgroundColor: "#385a8a" }} onClick={this.toggle}>Edit</Button>;
    if (create) {
      title = "Creating New Group";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px", backgroundColor: "black" }}
        >
          Create New
        </Button>
      );
    }

    return (
      <Fragment>
      <br></br>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewProductForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              products={this.props.products}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewProductModal;