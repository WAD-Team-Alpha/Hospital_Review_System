/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/iframe-has-title */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";

function About(params) {
  return (
    <div>
      {/* <!-- ABOUT --> */}
      <section id="about">
        <div class="container">
          <div class="row">
            <div class="col-md-6 col-sm-6">
              <div class="about-info">
                <h2 class="wow fadeInUp" data-wow-delay="0.6s">
                  Welcome to Your <i class="fa fa-h-square"></i>ealth Center
                </h2>
                <div class="wow fadeInUp" data-wow-delay="0.8s">
                  <p>
                    Aenean luctus lobortis tellus, vel ornare enim molestie
                    condimentum. Curabitur lacinia nisi vitae velit volutpat
                    venenatis.
                  </p>
                  <p>
                    Sed a dignissim lacus. Quisque fermentum est non orci
                    commodo, a luctus urna mattis. Ut placerat, diam a tempus
                    vehicula.
                  </p>
                </div>
                <figure class="profile wow fadeInUp" data-wow-delay="1s">
                  <img
                    src="images/author-image.jpg"
                    class="img-responsive"
                    alt=""
                  />
                  <figcaption>
                    <h3>Dr. Neil Jackson</h3>
                    <p>General Principal</p>
                  </figcaption>
                </figure>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default About;
