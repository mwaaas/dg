<?php
$jsController = "Collections";
include("includes/header.php");
?>
    <?php include("includes/partials/search.php"); ?>
    
    <!-- Main page content -->
    
    <section id="main" role="main" class="wrapper">
        <div class="inner-wrapper js-collections-wrapper">
            <header class="clearfix layout-vr-lg">
                <div class="grid-col">
                    <h1 class="hdg-a hdg-source-lt">Collections</h1>
                </div>
                <div class="grid-rt">
                    <?php include("includes/partials/mostFilters.php"); ?>
                </div>
            </header> <!-- End .grid -->
            <div class="clearfix">

                <!-- Filter bar -->
                <?php include("includes/partials/filterBar.php"); ?>
                
                <div class="grid-col grid-size3of4">
                    <div class="layout-vr-md borderBottom">
                        <ul class="results-info h-list h-list-sm js-filter-breadcrumbs">
                            
                            <!-- Dynamic filter breadcrumbs content here -->

                        </ul>
                    </div>
                    <div class="grid">
                        <div class="grid-lt">
                            <span class="loading-indicator js-loading-indicator">Loading...</span>
                        </div>
                        <div class="grid-rt js-pagination">

                            <!-- Dynamic Pagination Here -->

                        </div>
                    </div>
                    <ul class="blocks blocks-3-up clearfix js-collections-container">
                        
                        <!-- Dynamic Collections Content Here -->

                    </ul>
                     <div class="grid layout-vr-lg">
                        <div class="grid-rt js-pagination">

                            <!-- Dynamic Pagination Here -->

                        </div>
                    </div>
                </div> <!-- End .grid-size3of4 -->
            </div>
        </div> <!-- End .inner-wrapper -->
    </section> <!-- End .wrapper -->

<?php
include ("includes/footer.php");
?>