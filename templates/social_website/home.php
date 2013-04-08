<?php
$jsController = "Home";
include("includes/header.php");
?>
    <?php include("includes/partials/mainCarousel.php"); ?>
    
    <?php include("includes/partials/search.php"); ?>
    
    <section id="main" role="main" class="wrapper">
        <div class="inner-wrapper">
            <header class="grid">
                <div class="grid-col">
                    <h2 class="hdg-a hdg-source-lt layout-vr-sm">Featured Collection</h2>
                </div>
                <div class="grid-rt">
                    <div class="language-select custom-select js-custom-select">
                        <select>
                            <!-- TODO: populate this dynamically -->
                            <option value="all">All Languages</option>
                            <option value="en">English</option>
                            <option value="es">Spanish</option>
                            <option value="fr">French</option>
                        </select>
                        <div class="custom-select-container">
                            <div class="icon"></div>
                            <div class="selected-item-label js-selected-item-label"></div>
                            <ul class="options js-options">
                                <!-- Dynamic content filled by select box -->
                            </ul>
                        </div>
                    </div>
                </div>
            </header>
            <div class="featured layout-vr-xlg">
                <div class="grid">
                    <div class="grid-col grid-size3of4">
                        Image mosaic here
                    </div>
                    <div class="grid-col grid-size1of4">
                        <div class="grid-pad-lt-sm">
                            <h3 class="hdg-green hdg-c layout-vr-sm">Collection Title</h3>
                            <h4 class="copy hdg-bold"> State, Country</h4>
                            <h5 class="copy layout-vr-sm">Language</h5>
                            <p class="layout-vr-md">Lorem ipsum dolor sit amet, cons ectetur adipiscing elit. Praesent ac tortor purus. Cras sed velit leo, nec tristique risus. </p>
                            <div class="featured-logo copy layout-vr-md">
                                <img class="" src="http://placehold.it/41x39" alt="" /> 
                                SERP
                            </div>
                            <div class="featured-ft">
                                <div class="featured-ft-videoDetails">
                                   <ul class="h-list h-list-sm h-list-divided copy copy-white">
                                       <li>6 Videos</li>
                                       <li>23:15</li>
                                   </ul>
                                </div>
                                <ul class="h-list h-list-sm copy-sm copy-dk vid-cat-list-dk">
                                    <li class="like"><span class="text-hide">Likes</span> 10,000</li>
                                    <li class="view"><span class="text-hide">Viewed</span> 6,018</li>
                                    <li class="check"><span class="text-hide">Adopted</span> 4, 020</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div> <!-- End .featured -->
        </div> <!-- End .inner-wrapper -->
    </section> <!-- End .wrapper -->
    
    <section class="gradientBg">
        <div class="wrapper">
            <div class="inner-wrapper js-collections-wrapper">
                <header class="clearfix layout-vr-lg">
                    <div class="grid-col">
                        <h1 class="hdg-a hdg-source-lt">Collections</h1>
                    </div>
                    <div class="grid-rt">
                        <?php include("includes/partials/mostFilters.php"); ?>
                    </div>
                </header> <!-- End .clearfix -->
                <ul class="blocks blocks-4-up clearfix js-collections-container">

                        <!-- Dynamic Collections Content Here -->

                </ul>
                <div class="gradientBg-ft">
                    <div class="pagination-wrapper js-pagination">

                            <!-- Dynamic Pagination Here -->

                    </div>
                    <div class="gradientBg-ft-btn">
                        <a href="#" class="btn">See All Collections</a>
                    </div>
                </div>
            </div> <!-- End .inner-wrapper -->
        </div> <!-- End .wrapper -->
    </section>
    
    <section class="wrapper layout-vr-xlg">
        <div class="inner-wrapper js-news-feed-wrapper">
            <h2 class="hdg-a hdg-source-lt layout-vr-md">News Feed</h2>
            <ul class="v-list-lg v-list-divided v-list-divided-dk js-news-feed-container">
                <!-- Dynamic News Feed Content Here -->
            </ul>
            <div class="news-ft">
                <a href="#" class="btn js-news-feed-show-more-btn">Show More</a>
            </div>
        </div> <!-- End .inner-wrapper -->
    </section>

<?php
include ("includes/footer.php");
?>