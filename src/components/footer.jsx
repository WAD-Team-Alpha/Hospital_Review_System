/* eslint-disable jsx-a11y/anchor-has-content */
/* eslint-disable jsx-a11y/iframe-has-title */
/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react";

function Footer(params) {
  return (
    <div>
      {/* <!-- FOOTER --> */}
      <footer data-stellar-background-ratio="5">
        <div class="container">
          <div class="row">
            <div class="col-md-4 col-sm-4">
              <div class="footer-thumb">
                <h4 class="wow fadeInUp" data-wow-delay="0.4s">
                  Contact Info
                </h4>
                <p>
                  Fusce at libero iaculis, venenatis augue quis, pharetra lorem.
                  Curabitur ut dolor eu elit consequat ultricies.
                </p>

                <div class="contact-info">
                  <p>
                    <i class="fa fa-phone"></i> 010-070-0170
                  </p>
                  <p>
                    <i class="fa fa-envelope-o"></i>{" "}
                    <a href="#">info@company.com</a>
                  </p>
                </div>
              </div>
            </div>

            <div class="col-md-4 col-sm-4">
              <div class="footer-thumb">
                <h4 class="wow fadeInUp" data-wow-delay="0.4s">
                  Latest News
                </h4>
                <div class="latest-stories">
                  <div class="stories-image">
                    <a href="#">
                      <img
                        src="images/news-image.jpg"
                        class="img-responsive"
                        alt=""
                      />
                    </a>
                  </div>
                  <div class="stories-info">
                    <a href="#">
                      <h5>Amazing Technology</h5>
                    </a>
                    <span>March 08, 2018</span>
                  </div>
                </div>

                <div class="latest-stories">
                  <div class="stories-image">
                    <a href="#">
                      <img
                        src="images/news-image.jpg"
                        class="img-responsive"
                        alt=""
                      />
                    </a>
                  </div>
                  <div class="stories-info">
                    <a href="#">
                      <h5>New Healing Process</h5>
                    </a>
                    <span>February 20, 2018</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-4 col-sm-4">
              <div class="footer-thumb">
                <div class="opening-hours">
                  <h4 class="wow fadeInUp" data-wow-delay="0.4s">
                    Opening Hours
                  </h4>
                  <p>
                    Monday - Friday <span>06:00 AM - 10:00 PM</span>
                  </p>
                  <p>
                    Saturday <span>09:00 AM - 08:00 PM</span>
                  </p>
                  <p>
                    Sunday <span>Closed</span>
                  </p>
                </div>

                <ul class="social-icon">
                  <li>
                    <a
                      href="#"
                      class="fa fa-facebook-square"
                      attr="facebook icon"
                    ></a>
                  </li>
                  <li>
                    <a href="#" class="fa fa-twitter"></a>
                  </li>
                  <li>
                    <a href="#" class="fa fa-instagram"></a>
                  </li>
                </ul>
              </div>
            </div>

            <div class="col-md-12 col-sm-12 border-top">
              <div class="col-md-4 col-sm-6">
                <div class="copyright-text">
                  <p>Copyright &copy; 2018 Your Company | Design: Tooplate</p>
                </div>
              </div>
              <div class="col-md-6 col-sm-6">
                <div class="footer-link">
                  <a href="#">Laboratory Tests</a>
                  <a href="#">Departments</a>
                  <a href="#">Insurance Policy</a>
                  <a href="#">Careers</a>
                </div>
              </div>
              <div class="col-md-2 col-sm-2 text-align-center">
                <div class="angle-up-btn">
                  <a
                    href="#top"
                    class="smoothScroll wow fadeInUp"
                    data-wow-delay="1.2s"
                  >
                    <i class="fa fa-angle-up"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Footer;
