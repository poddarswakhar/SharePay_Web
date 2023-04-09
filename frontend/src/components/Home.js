import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ProductList from "./ProductList";
import NewProductModal from "./NewProductModal";

import axios from "axios";
import { API_URL } from "../constants";

// This is the top heirarchy JS file

class Home extends Component {
  // the variable we have to keep track
  state = {
    products: [], // queryset
  };

  // states management
  componentDidMount() {
    this.resetState();
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



  // rendering the feont end, if the state is not healthy show not healthy message, in the meantime of the request to be made and the state to be updated, show Loading message
  // The other render part is self sufficient to understand, using elements with some inline css
  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
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