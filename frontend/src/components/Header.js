import React, { Component } from "react";

// Header file

class Header extends Component {
  // if it clicks on the logo the page reloads, for better user experience
  handleDivClick = () => {
    window.location.reload();
  };
  render() {
    return (
      <div className="text-center" >
        <div style={{backgroundColor: 'black', borderBottom: "4px solid blue" }} onClick={this.handleDivClick}>
            <img
            src="https://i.ibb.co/VJHRbjc/SHARE-PAY.png"
            width="150"
            className="img-thumbnail"
            style={{ marginTop: "20px", backgroundColor: 'black', border: "none" }}
            />
            <hr />
        </div>

        <br></br>

        <h5>
          <i>presents</i>
        </h5>
        <h1>Money Polling DApp</h1>
        <br></br>
      </div>
    );
  }
}

export default Header;