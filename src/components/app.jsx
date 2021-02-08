/* eslint-disable jsx-a11y/img-redundant-alt */

import React from "react";
import About from "./about";
import Team from "./team";
import Header from "./header";
import News from "./news";
import Home from "./home";
import Appointment from "./appointment";
import Map from "./map";
import Footer from "./footer";
function App(params) {
  return (
    <div>
      <Header />
      <Home />
      <About />
      <Team />
      <News />
      <Appointment />
      <Map />
      <Footer/>
    </div>
  );
}

export default App;
