import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ProductList from "./ProductList";
import NewProductModal from "./NewProductModal";

import axios from "axios";
import { API_URL, API_URL_A } from "../constants";
import SignModal from "./SignModal";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";

// This is the top heirarchy JS file

class Home extends Component {
  // the variable we have to keep track
  state = {
    products: [], // queryset
    isModalOpen: false // new state property for modal
  };

  toggleModal = () => {
    this.setState({ isModalOpen: !this.state.isModalOpen });
  };

  // states management
  componentDidMount() {
    this.resetState();
    setInterval(this.sendDate, 60000);
  }

  // using axios to do the GET request for all the product
  getProducts = () => {
    axios.get(API_URL).then(res => this.setState({ products: res.data, isHealthy: true }))
    .catch(error => {
    });
  }

  // reset state method for state management
  resetState = () => {
    this.setState({ isHealthy: null }, () => {
      // reset products and searchTerm after resetting health status
      this.getProducts();
    });
  };

  sendDate = () => {
    const currentDateTime = new Date().toISOString();
    axios
      .post(API_URL_A + "?date=" +  currentDateTime)
      .then((res) => {
        console.log(currentDateTime);
      })
      .catch((error) => {
        console.error("Error Sending Date:", error);
      });
  };


  // rendering the feont end, if the state is not healthy show not healthy message, in the meantime of the request to be made and the state to be updated, show Loading message
  // The other render part is self sufficient to understand, using elements with some inline css
  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <div className="text-center">
          <Button
            color="primary"
            className="text-center"
            onClick={this.toggleModal}
            style={{ minWidth: "200px", backgroundColor: "black" }}
          >
            SIGN CONTRACT
          </Button>
        </div>
        <br></br>

      
      {this.state.isModalOpen && (
        <SignModal
          create={true}
          resetState={this.resetState}
          isOpen={this.state.isModalOpen} // new prop for modal
          toggle={this.toggleModal} // new prop for modal
        />
      )}
        <br></br><br></br>
        <Row>
          <Col>
            <ProductList
              products={this.state.products}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewProductModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;