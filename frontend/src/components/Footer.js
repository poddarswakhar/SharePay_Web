import React, { Component } from "react";

// Footer file

class Footer extends Component {
  render() {
    return (
      <div className="text-center" >
        <div style={{backgroundColor: 'black', borderTop: "4px solid blue", height: '200px' }}>
            <img 
            src="https://i.ibb.co/VJHRbjc/SHARE-PAY.png"
            width="100"
            className="img-thumbnail"
            style={{ marginTop: "80px", backgroundColor: 'black', border: "none"}}
            />
        </div>
      </div>
    );
  }
}

export default Footer;