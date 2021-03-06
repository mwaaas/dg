/**
 * HomeController Class File
 *
 * @author rdeluca
 * @version $Id$
 * @requires require.js
 * @requires jQuery
 */

define(function(require) {
    'use strict';

    var DigitalGreenPageController = require('controllers/DigitalGreenPageController');
    var CollectionViewController = require('app/view-controllers/CollectionViewController');
    var CollectionMostFiltersViewController = require('app/view-controllers/CollectionMostFiltersViewController');
    var NewsFeedViewController = require('app/view-controllers/news/NewsFeedViewController');
    var FeaturedCollectionViewController = require('app/view-controllers/FeaturedCollectionViewController');
    var jQuery = require('jquery');

    var NCarousel = require('libs/NCarousel/NCarousel');
    
    require('libs/external/swfobject/swfobject');

    var HomeController = DigitalGreenPageController.extend({

        /**
         * Controller constructor
         * @return {HomeController} this
         */
        constructor: function(bootstrapConfig, globalHelpers) {
            this.base(bootstrapConfig, globalHelpers);

            var references = this._references;

            references.collectionViewController
                .setCollectionsPerPage(4)
                .setCollectionsPerRow(4)
                .setVideosPerDrawer(5);

            // set the active filter to be Most Liked to init the collections
            references.collectionMostFiltersViewController.setActiveFilter('-featured');
            
            this._getNewsFeed();
            this._getFeaturedCollection();

            return this;
        },

        _initReferences: function($referenceBase) {
            this.base($referenceBase);

            var references = this._references;

            var $collectionsContainer = jQuery('.js-collections-wrapper');
            var $newsFeedContainer = jQuery(".js-news-feed-wrapper");
            var $featuredCollectionContainer = jQuery(".js-featured-collection-wrapper");

            // helpers
            var $languageCookie = Util.Cookie.get('language__name');
            references.collectionViewController = new CollectionViewController($collectionsContainer, $languageCookie);
            references.collectionMostFiltersViewController = new CollectionMostFiltersViewController($collectionsContainer);
            references.newsFeedViewController = new NewsFeedViewController($newsFeedContainer);
            references.FeaturedCollectionViewController = new FeaturedCollectionViewController($featuredCollectionContainer, $languageCookie);

            // dom elements
            references.$imageCarouselWrapper = jQuery('.js-imageCarousel');

            references.imageCarousel = new NCarousel(references.$imageCarouselWrapper, {
                transition: 'fade',
                autoPlay: true,
                autoPlayDelay: 2000
            });
            
            // play button 
            references.$playButton = jQuery('.play-button');
        },

        _initEvents: function() {
            this.base();
            
            var references = this._references;
            var boundFunctions = this._boundFunctions;

            boundFunctions.onOrderChanged = this._onOrderChanged.bind(this);
            references.collectionMostFiltersViewController.on('orderChanged', boundFunctions.onOrderChanged);

            boundFunctions.onNewsFeedUpdated = this._onNewsFeedUpdated.bind(this);
            references.newsFeedViewController.on('newsFeedUpdated', boundFunctions.onNewsFeedUpdated);
            
            boundFunctions.onPlayButtonClick = this._onVideoPlayButtonClick.bind(this);
            references.$playButton.on('click', boundFunctions.onPlayButtonClick);
        },

        _onOrderChanged: function(orderCriteria) {
            this._references.collectionViewController.setInputParam('order_by', orderCriteria);
        },

        _getCollections: function() {
            this._references.collectionViewController.getCollections();
        },

        _getNewsFeed: function() {
            this._references.newsFeedViewController.getNewsItems();
        },

        _getFeaturedCollection: function() {
        	this._references.FeaturedCollectionViewController.getFeaturedCollection();
        },
        _onNewsFeedUpdated: function (broadcastData){
            this._references.newsFeedViewController.updateTotalCount(broadcastData.totalCount);
            this._references.newsFeedViewController.addToCurrentCount(broadcastData.addedCount);
            this._references.newsFeedViewController.updateNewsItemPaginationDisplay();
        },
        
        _initVideoPlayer: function() {

            var videoId = 'JYkaf4ucaSc';

            var params = { allowScriptAccess: "always" };
            var atts = { id: "player", 
            			 class: 'main-carousel-video-player'
            		    };
            
            swfobject.embedSWF(
                'http://www.youtube.com/v/' + videoId + '?enablejsapi=1&playerapiid=ytplayer&version=3',
                'player',
                '1024',
                '424',
                '8',
                null,
                null,
                params,
                atts
            );

            window.onYouTubePlayerReady = this._onYouTubePlayerReady.bind(this);
            $("#video-img > div").not("#player").each(function(index, ele){$(ele).hide();});
            $("#player").show();
        },

        _onYouTubePlayerReady: function() {
            // clean up the window
            window.onYouTubePlayerReady = undefined;

            var videoPlayer = jQuery('#player').get(0);
            this._references.videoPlayer = videoPlayer;

            // youtube seems to force us to put functions in the window
            // we'll do our best to handle that elegantly
            window.onYouTubePlayerStateChange = this._onYouTubePlayerStateChange.bind(this);

            videoPlayer.addEventListener('onStateChange', 'onYouTubePlayerStateChange');
            
            videoPlayer.playVideo();
            
        },

        _onYouTubePlayerStateChange: function(newState) {
            if (newState == 0){
            	$("#player").hide();          
				$("#video-img > div").not("#player").each(function(index, ele){$(ele).show();});
            }
        	
        },
        
        _onVideoPlayButtonClick: function(e) {
        	this._initVideoPlayer();
        },

        /**
         * Controller destructor
         * @return {void}
         */
        destroy: function() {
            this.base();
        }
    });

    return HomeController;
});
