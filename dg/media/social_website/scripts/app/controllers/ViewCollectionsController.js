/**
 * ViewCollectionsController Class File
 *
 * @author rdeluca
 * @version $Id$
 * @requires require.js
 * @requires jQuery
 */

define(function(require) {
    'use strict';

    var DigitalGreenPageController = require('controllers/DigitalGreenPageController');
    var Util = require('framework/Util');
    var jQuery = require('jquery');

    require('libs/external/buttons');

    var VideoLikeDataFeed = require('app/libs/VideoLikeDataFeed');
    //var CommentLikeDataFeed = require('app/libs/CommentLikeDataFeed');
    //var TimeWatchedDataFeed = require('app/libs/TimeWatchedDataFeed');

    var CommentsFeedViewController = require('app/view-controllers/CommentsFeedViewController');

    var NCarousel = require('libs/NCarousel/NCarousel');
    
    var ViewCollectionsController = DigitalGreenPageController.extend({

        /**
         * Controller constructor
         * @return {ViewCollectionsController} this
         */
        constructor: function(bootstrapConfig, globalHelpers) {
            this.base(bootstrapConfig, globalHelpers);

            this._initVideoPlayer();
            
            stLight.options({
            	publisher: "5e0ffe84-d022-4b7d-88e1-a273f081e67e", 
            	doNotHash: false, 
            	doNotCopy: false, 
            	hashAddressBar: false
            });
            
            this._initVideoStats();

            this._getComments();
        },

        _initConfig: function() {
            // how often we should update the server with video watched info in ms
    //        this._config.updateVideoWatchedTimeDelay = 5000;
        },

        _initReferences: function() {
            this.base();

            var references = this._references;

            references.$commentsAreaWrapper = jQuery('.js-comments-feed-wrapper');
            references.commentsFeedViewController = new CommentsFeedViewController(references.$commentsAreaWrapper);

            references.videoLikeDataFeed = new VideoLikeDataFeed();
      // 	uncomment when comment-like and user time watched functionality is updated  
      //      references.commentLikeDataFeed = new CommentLikeDataFeed();
      //      references.timeWatchedDataFeed = new TimeWatchedDataFeed();

            references.$likeButton = jQuery('.js-like-button');
            references.$commentBox = jQuery('#comment');
            references.$commentButton = jQuery('.js-comment-btn');

            references.$videoTarget = jQuery('#video-target');
            references.$showMoreButton = jQuery('.js-show-more');
            references.$vidDesc = jQuery('.js-vid-desc');

            var $videosCarouselWrapper = jQuery('#collection-videos-carousel');
            references.videosCarousel = new NCarousel($videosCarouselWrapper, {
                autoPlay: false,
                allowWrapping: false
            });
        },

        _initEvents: function() {
            this.base();

            var references = this._references;
            var boundFunctions = this._boundFunctions;
            
            boundFunctions.onDataProcessed = this._onDataProcessed.bind(this);
            references.videoLikeDataFeed.on('dataProcessed', boundFunctions.onDataProcessed);

            boundFunctions.onLikeButtonClick = this._onVideoLikeButtonClick.bind(this);
            references.$likeButton.on('click', boundFunctions.onLikeButtonClick);

            boundFunctions.onCommentButtonClick = this._onCommentButtonClick.bind(this);
            references.$commentButton.on('click', boundFunctions.onCommentButtonClick);

            boundFunctions.onShowMoreButtonClick = this._onShowMoreButtonClick.bind(this);
            references.$showMoreButton.on('click', boundFunctions.onShowMoreButtonClick);
            
            boundFunctions.onCommentLikeButtonClick = this._onCommentLikeButtonClick.bind(this);
            references.$commentsAreaWrapper.on('click', '.js-comment-like-button', boundFunctions.onCommentLikeButtonClick);
        },

        _initState: function() {
            this.base();
            
            var state = this._state;

            state.videoLiked = false;

            // get user id
            // get video id
            state.userID = jQuery('body').data('userId');
            state.videoUID = this._references.$videoTarget.data('video-uid');

            this._references.videoLikeDataFeed.fetch(state.videoUID, state.userID);
            
            state.updateVideoWatchedTimeInterval = undefined;
            try{
                this._references.videosCarousel.moveToSlide(parseInt(($('.js-video-wrapper').attr('data-slide')-1)/5),{stopAutoPlay: false});
            }
            catch(err){
                //Todo
            }
        },

        _initVideoStats: function() {
            
            var $statBarWrappers = jQuery('.js-stat-bar-wrapper');
            var $statBar;
            var $leftValue;
            var $rightValue;
            var $statIndicator;

            var i = 0;
            var len = $statBarWrappers.length;
            for (; i < len; i++) {
                var $currentStatBarWrapper = $statBarWrappers.eq(i);

                $statBar = $currentStatBarWrapper.find('.js-stat-bar');
                var leftValue = $statBar.data('leftValue');
                var rightValue = $statBar.data('rightValue');

                $leftValue = $currentStatBarWrapper.find('.js-left-value');
                $rightValue = $currentStatBarWrapper.find('.js-right-value');
                $leftValue.html(Util.integerCommaFormat(leftValue));
                $rightValue.html(Util.integerCommaFormat(rightValue));

                $statIndicator = $currentStatBarWrapper.find('.js-stat-indicator');

                // for basic width setting, use this line instead
                // $statIndicator.css('width', ((leftValue * 100) / (leftValue + rightValue)) + '%');

                // otherwise, this can be used to animate the effect
                $statIndicator.animate({
                    width: ((leftValue * 100) / (leftValue + rightValue)) + '%'
                }, 2000);

            }
        },

        _initVideoPlayer: function() {
            var videoId = this._references.$videoTarget.data('videoId');
            var videoPlayerWidth = this._references.$videoTarget.width();
            var that = this;
            if (typeof(YT) == 'undefined' || typeof(YT.Player) == 'undefined') {
                window.onYouTubeIframeAPIReady = function() {
                    that.loadPlayer(videoId,videoPlayerWidth);
                };
                $.getScript('//www.youtube.com/iframe_api');
            } 
            else {
                  that.loadPlayer(videoId,videoPlayerWidth);
            }
        },
        
        loadPlayer: function(videoId, videoPlayerWidth){
            var that = this;
            var player = new YT.Player('video-target', {
                videoId: videoId,
                width: videoPlayerWidth,
                events: {
                    'onReady': that._onYouTubePlayerReady,
                    'onStateChange': function(newState){
                    switch (newState.data) {
                          // playback completed/stopped
                          case 0:
                                var now_playing_video = jQuery('.now-playing');
                                var next_video;
                                if (now_playing_video.hasClass('js-featured-collection-li')) {
                                    next_video = now_playing_video.next('li');
                                    if (next_video.length == 0) {
                                        next_video = now_playing_video.closest('ul').find('li:first');
                                    }
                                    window.location.href = next_video.find('a').attr('href');
                                }
                                else {
                                    now_playing_video = now_playing_video.closest('li');
                                    next_video = now_playing_video.next();
                                    if (next_video.length == 0) {
                                        /* End of current slide or this is the last video altogether */
                                        var next_slide = now_playing_video.closest('ul').closest('li').next();
                                        if (next_slide.length == 0) {
                                            /* Last video - go back to the first video */
                                            next_slide = now_playing_video.closest('ul').closest('li').closest('ul').find('li:first');
                                        }
                                        next_video = next_slide.find('ul > li:first-child');
                                    }
                                    window.location.href = next_video.find('.vidDrawer-image a').attr('href');
                                }
                          // stop the interval and manually send an update
                          case 2:
                              that._stopUpdateInterval();
                              that._updateVideoWatchedTime();
                              break;
                          // playback started
                          case 1:
                              that._startUpdateInterval();
                              break;
                      }
                  }
                }
              });
        },

        _onYouTubePlayerReady: function(event) {
            // Below functionality will autoplay the youtube video on all video pages for Non-Mobile Devices
            if (!navigator.userAgent.match(/Mobi/)) {
                event.target.playVideo();
            }
            
        },

        _startUpdateInterval: function() {
            // ensure we don't orphan an interval
            this._stopUpdateInterval();

            this._state.updateVideoWatchedTimeInterval = setInterval(this._updateVideoWatchedTime.bind(this), this._config.updateVideoWatchedTimeDelay);
        },

        _stopUpdateInterval: function() {
            clearInterval(this._state.updateVideoWatchedTimeInterval);
            this._state.updateVideoWatchedTimeInterval = null;
        },

        _updateVideoWatchedTime: function() {
            var videoUID = this._state.videoUID;
            var userID = this._state.userID;
            // we use the current time as our indicator of how much of the video has been watched
            // NOTE: this will not account for seeking; if the user seeks to the end, it will appear
            // as if they watched the entire video
            
            //uncomment when functionality is available
            //var timeWatched = this._references.videoPlayer.getCurrentTime();
            //this._references.timeWatchedDataFeed.fetch(videoUID, userID, Math.floor(timeWatched));
        },

        _getComments: function() {
            this._references.commentsFeedViewController.getComments();
        },
        
        

        _onDataProcessed: function(likedEntries) {
            this._state.videoLiked = likedEntries[0].liked;
            if (this._state.videoLiked) {
                this._references.$likeButton.addClass('liked');
            }
        },
        
        _onVideoLikeButtonClick: function(e) {
            e.preventDefault();

            if (this._state.videoLiked) {
                return;
            }

            var $currentTarget = jQuery(e.currentTarget);

            var videoUID = this._state.videoUID;
            var userID = this._state.userID;

            if (videoUID == undefined || userID == undefined) {
                throw new Error('ViewCollectionsController._onVideoLikeButtonClick: videoUID and userID are required parameters');
            }

            this._references.videoLikeDataFeed.fetch(videoUID, userID, function(){}, 'POST');
        },

        _onShowMoreButtonClick: function(e){
            e.preventDefault();
            var references = this._references;
            if ($(references.$vidDesc).hasClass("featured-line-clamp")){
                $(references.$vidDesc).removeClass("featured-line-clamp");
                $(references.$showMoreButton).text("Show Less");
            }
            else{
                $(references.$vidDesc).addClass("featured-line-clamp");
                $(references.$showMoreButton).text("Show More")
            }

        },

        _onCommentButtonClick: function(e) {
            e.preventDefault();

            var $currentTarget = jQuery(e.currentTarget);

            var videoUID = this._state.videoUID;
            var userID = this._state.userID;
            var text = this._references.$commentBox.val();

            if (videoUID == undefined || userID == undefined || text == undefined) {
                throw new Error('ViewCollectionsController._onCommentButtonClick: videoUID ,userID, text are required parameters');
            }
            
            this._references.commentsFeedViewController.addNewComment(videoUID, userID, text);
            this._references.$commentBox.val('');
        },
        
        _onCommentLikeButtonClick: function(e) {
            e.preventDefault();

            if (this._state.videoLiked) {
                return;
            }

            var $currentTarget = jQuery(e.currentTarget);

            var commentUID = $currentTarget.data('commentUid');
            var commentLiked = $currentTarget.data('commentLiked');
            var userID = this._state.userID;

            if (commentUID == undefined || userID == undefined || commentLiked == undefined) {
                throw new Error('ViewCollectionsController._onVideoLikeButtonClick: commentUID, userID, and commentLiked are required parameters');
            }

            var newCommentLikedStatus = !(commentLiked == '1');

            this._references.commentLikeDataFeed.fetch(commentUID, userID, newCommentLikedStatus, this._onCommentLikedCallback.bind(this, $currentTarget, newCommentLikedStatus));
        },

        _onVideoLikedCallback: function() {
            var responseStatus = this._references.videoLikeDataFeed.getResponseStatus();

            if (responseStatus.success) {
                this._references.$likeButton.addClass('liked');
                this._state.videoLiked = true;
            } else {
                // NOTE: any desired error handling would go here
            }
        },

        _onCommentLikedCallback: function($commentLikeButton, newCommentLikedStatus, data) {
            var responseStatus = this._references.commentLikeDataFeed.getResponseStatus();

            if (responseStatus.success) {

                if (newCommentLikedStatus) {
                    $commentLikeButton
                        .addClass('liked')
                        .data('commentLiked', (newCommentLikedStatus) ? '1' : '0');

                    var likedCount = data.likedCount || 0;

                    $commentLikeButton.find('.js-like-count').html(Util.integerCommaFormat(likedCount));
                    $commentLikeButton.find('.js-like-label').html((likedCount != 1) ? 'Likes' : 'Like');
                } else {
                    $commentLikeButton
                        .removeClass('liked')
                        .data('commentLiked', (newCommentLikedStatus) ? '1' : '0');
                }
                
            } else {
                // NOTE: any desired error handling would go here
            }
        },

        /**
         * Controller destructor
         * @return {void}
         */
        destroy: function() {
            this.base();
        }
    });

    return ViewCollectionsController;
});
