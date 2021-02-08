/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/iframe-has-title */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";

function News(params) {
  return (
    <div>
      {/* <!-- NEWS --> */}
      <section id="news" data-stellar-background-ratio="2.5">
        <div class="container">
          <div class="row">
            <div class="col-md-12 col-sm-12">
              {/* <!-- SECTION TITLE --> */}
              <div class="section-title wow fadeInUp" data-wow-delay="0.1s">
                <h2>Latest News</h2>
              </div>
            </div>

            <div class="col-md-4 col-sm-6">
              {/* <!-- NEWS THUMB --> */}
              <div class="news-thumb wow fadeInUp" data-wow-delay="0.4s">
                <a href="news-detail.html">
                  <img
                    src="images/news-image1.jpg"
                    class="img-responsive"
                    alt=""
                  />
                </a>
                <div class="news-info">
                  <span>March 08, 2018</span>
                  <h3>
                    <a href="news-detail.html">About Amazing Technology</a>
                  </h3>
                  <p>
                    Maecenas risus neque, placerat volutpat tempor ut, vehicula
                    et felis.
                  </p>
                  <div class="author">
                    <img
                      src="images/author-image.jpg"
                      class="img-responsive"
                      alt=""
                    />
                    <div class="author-info">
                      <h5>Jeremie Carlson</h5>
                      <p>CEO / Founder</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-4 col-sm-6">
              {/* <!-- NEWS THUMB --> */}
              <div class="news-thumb wow fadeInUp" data-wow-delay="0.6s">
                <a href="news-detail.html">
                  <img
                    src="images/news-image2.jpg"
                    class="img-responsive"
                    alt=""
                  />
                </a>
                <div class="news-info">
                  <span>February 20, 2018</span>
                  <h3>
                    <a href="news-detail.html">
                      Introducing a new healing process
                    </a>
                  </h3>
                  <p>
                    Fusce vel sem finibus, rhoncus massa non, aliquam velit. Nam
                    et est ligula.
                  </p>
                  <div class="author">
                    <img
                      src="images/author-image.jpg"
                      class="img-responsive"
                      alt=""
                    />
                    <div class="author-info">
                      <h5>Jason Stewart</h5>
                      <p>General Director</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-4 col-sm-6">
              {/* <!-- NEWS THUMB --> */}
              <div class="news-thumb wow fadeInUp" data-wow-delay="0.8s">
                <a href="news-detail.html">
                  <img
                    src="images/news-image3.jpg"
                    class="img-responsive"
                    alt=""
                  />
                </a>
                <div class="news-info">
                  <span>January 27, 2018</span>
                  <h3>
                    <a href="news-detail.html">
                      Review Annual Medical Research
                    </a>
                  </h3>
                  <p>
                    Vivamus non nulla semper diam cursus maximus. Pellentesque
                    dignissim.
                  </p>
                  <div class="author">
                    <img
                      src="images/author-image.jpg"
                      class="img-responsive"
                      alt=""
                    />
                    <div class="author-info">
                      <h5>Andrio Abero</h5>
                      <p>Online Advertising</p>
                    </div>
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
export default News;
