import React, { Component, Fragment } from "react";
import Header from "./components/Header";
import Home from "./components/Home";
import Footer from "./components/Footer";

// the top file that renders all the components

class App extends Component {
  render() {
    return (
      <div className="vh-100 d-flex flex-column">
        <Header />
        <div className="flex-grow-1">
          <Home />
          <br></br><br></br>
        </div>
        <Footer />
      </div>
    );
  }
}

export default App;