import React, { Component } from "react";
import { Table } from "reactstrap";
import NewProductModal from "./NewProductModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

// This file is the file that displays all the list of the products after doing the query in the Home.js
// also renders the remove confirmation when delete is pressed
// Again the render part is self sufficient to understand, using elements with some inline css

class ProductList extends Component {
  render() {
    const products = this.props.products;
    return (
      <div>
        <Table striped>
          <thead>
            <tr>
              <th>Group ID</th>
              <th>User 1 Name</th>
              <th>User 1 Wallet Address</th>
              <th>User 2 Name</th>
              <th>User 2 Wallet Address</th>
              <th>User 3 Name</th>
              <th>User 3 Wallet Address</th>
              <th>Service Name</th>
              <th>Service Wallet Address</th>
              <th>Individual Amount</th>
              <th>Service Acc ID</th>
              <th>Renewal Date & Time</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {!products || products.length <= 0 ? (
              <tr>
                <td colSpan="9" align="center">
                  <b>No Products!</b>
                </td>
              </tr>
            ) : (
              products.map(prod => (
                <tr key={prod.id}>
                  <td>{prod.id}</td>
                  <td>{prod.user1_name}</td>
                  <td>{prod.user1_wal}</td>
                  <td>{prod.user2_name}</td>
                  <td>{prod.user2_wal}</td>
                  <td>{prod.user3_name}</td>
                  <td>{prod.user3_wal}</td>
                  <td>{prod.serv_name}</td>
                  <td>{prod.dest_wal}</td>
                  <td>{prod.ind_val}</td>
                  <td>{prod.serv_acc_id}</td>
                  <td>{prod.ren}</td>
                  <td align="center">
                    {/* <NewProductModal
                      create={false}
                      products={prod}
                      resetState={this.props.resetState}
                    /> */}
                    &nbsp;&nbsp;
                    <ConfirmRemovalModal
                      pk={prod.id}
                      resetState={this.props.resetState}
                    />
                  </td>
                </tr>
              ))
            )}
          </tbody>
          <br></br>
        </Table>
        <div className="text-center">
          <b>Total Groups: {products.length}</b>
        </div>
      </div>
    );
  }
}

export default ProductList;