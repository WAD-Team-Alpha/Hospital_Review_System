/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/iframe-has-title */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";

function Home(params) {
  return (
    <div>
      {/* <!-- HOME --> */}
      <section id="home" class="slider" data-stellar-background-ratio="0.5">
        <div class="container">
          <div class="row">
            <div class="owl-carousel owl-theme">
              <div class="item item-first">
                <div class="caption">
                  <div class="col-md-offset-1 col-md-10">
                    <h3>Let's make your life happier</h3>
                    <h1>Healthy Living</h1>
                    <a
                      href="#team"
                      class="section-btn btn btn-default smoothScroll"
                    >
                      Meet Our Doctors
                    </a>
                  </div>
                </div>
              </div>

              <div class="item item-second">
                <div class="caption">
                  <div class="col-md-offset-1 col-md-10">
                    <h3>Aenean luctus lobortis tellus</h3>
                    <h1>New Lifestyle</h1>
                    <a
                      href="#about"
                      class="section-btn btn btn-default btn-gray smoothScroll"
                    >
                      More About Us
                    </a>
                  </div>
                </div>
              </div>

              <div class="item item-third">
                <div class="caption">
                  <div class="col-md-offset-1 col-md-10">
                    <h3>Pellentesque nec libero nisi</h3>
                    <h1>Your Health Benefits</h1>
                    <a
                      href="#news"
                      class="section-btn btn btn-default btn-blue smoothScroll"
                    >
                      Read Stories
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
export default Home;
