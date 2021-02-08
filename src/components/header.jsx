/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/iframe-has-title */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";

function Header(params) {
  return (
    <div>
      {/* <!-- PRE LOADER --> */}
      <section class="preloader">
        <div class="spinner">
          <span class="spinner-rotate"></span>
        </div>
      </section>

      {/* <!-- HEADER --> */}

      {/* <!-- MENU --> */}
      <section
        class="navbar navbar-default navbar-static-top"
        role="navigation"
      >
        <div class="container">
          <div class="navbar-header">
            <button
              class="navbar-toggle"
              data-toggle="collapse"
              data-target=".navbar-collapse"
            >
              <span class="icon icon-bar"></span>
              <span class="icon icon-bar"></span>
              <span class="icon icon-bar"></span>
            </button>

            {/* <!-- lOGO TEXT HERE --> */}
            <a href="index.html" class="navbar-brand">
              <i class="fa fa-h-square"></i>ealth Center
            </a>
          </div>

          {/* <!-- MENU LINKS --> */}
          <div class="collapse navbar-collapse">
            <ul class="nav navbar-nav navbar-right">
              <li>
                <a href="#top" class="smoothScroll">
                  Home
                </a>
              </li>
              <li>
                <a href="#about" class="smoothScroll">
                  About Us
                </a>
              </li>
              <li>
                <a href="#team" class="smoothScroll">
                  Doctors
                </a>
              </li>
              <li>
                <a href="#news" class="smoothScroll">
                  News
                </a>
              </li>
              <li>
                <a href="#google-map" class="smoothScroll">
                  Contact
                </a>
              </li>
              <li class="appointment-btn">
                <a href="#appointment">Make an appointment</a>
              </li>
            </ul>
          </div>
        </div>
      </section>
    </div>
  );
}
export default Header;
