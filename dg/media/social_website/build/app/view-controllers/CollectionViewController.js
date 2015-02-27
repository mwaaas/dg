define(["require","framework/controllers/Controller","framework/ViewRenderer","framework/Util","jquery","libs/NCarousel/NCarousel","app/libs/CollectionsDataFeed","text!app/views/collection.html","text!app/views/collection-video-drawer.html","text!app/views/collection-pagination.html"],function(e){var t=e("framework/controllers/Controller"),n=e("framework/ViewRenderer"),r=e("framework/Util"),i=e("jquery"),s=e("libs/NCarousel/NCarousel"),o=e("app/libs/CollectionsDataFeed"),u=e("text!app/views/collection.html"),a=e("text!app/views/collection-video-drawer.html"),f=e("text!app/views/collection-pagination.html"),l=t.extend({constructor:function(e,t){return this.base(e,t),this},_initConfig:function(){this.base();var e=this._config;e.filterChangeRefreshDelay=1e3,e.containerOpenHeight=213},_initReferences:function(e,t){this.base();var n=this._references;n.dataFeed=new o(t),n.$collectionsWrapper=e,n.$loadingIndicator=e.find(".js-loading-indicator"),n.$collectionsContainer=e.find(".js-collections-container"),n.$paginationContainers=e.find(".js-pagination")},_initState:function(){this.base();var e=this._state;e.currentPageNumber=0,e.collectionsPerPage=12,e.collectionsPerRow=4,e.videoDrawerClasses="",e.videosPerDrawer=5},_initEvents:function(){this.base();var e=this._boundFunctions,t=this._references;e.onDataProcessed=this._onDataProcessed.bind(this),t.dataFeed.on("dataProcessed",e.onDataProcessed),e.onInputParamChanged=this._onInputParamChanged.bind(this),t.dataFeed.on("inputParamChanged",e.onInputParamChanged),e.onCollectionItemClick=this._onCollectionItemClick.bind(this),t.$collectionsContainer.on("click",".js-collection-item",e.onCollectionItemClick),e.onPaginationItemClick=this._onPaginationItemClick.bind(this),t.$collectionsWrapper.find(".js-pagination").on("click",".js-pagination-item",e.onPaginationItemClick)},setCollectionsPerPage:function(e){return this._state.collectionsPerPage=e,this},setCollectionsPerRow:function(e){return this._state.collectionsPerRow=e,this},setVideoDrawerClasses:function(e){return this._state.videoDrawerClasses=e,this},setVideosPerDrawer:function(e){return this._state.videosPerDrawer=e,this},getCollections:function(e,t){e==undefined?e=this._state.currentPageNumber:this._state.currentPageNumber=e,t==undefined?t=this._state.collectionsPerPage:this._state.collectionsPerPage=t;var n=this._references.dataFeed;n.setInputParam("offset",e,!0),n.setInputParam("limit",t,!0),$(".js-collections-wrapper").attr("data-searchstring")!=""&&n.setInputParam("searchString",$(".js-collections-wrapper").attr("data-searchstring"));var r=n.getCollections(),i=n.getTotalCount();if(r==0)return!1;this._updateCollectionsDisplay(r,i)},_onDataProcessed:function(){$(".js-collections-wrapper-outer").show(),this.getCollections()},_updateCollectionsDisplay:function(e,t){this._renderCollections(e),this._renderPagination(t),this._initVideoCarousels(),this._references.$loadingIndicator.hide();var n={totalCount:t};this.trigger("collectionsUpdated",n)},_initVideoCarousels:function(){var e=this._references.$collectionsContainer.find(".js-carousel-wrapper"),t=0,n=e.length;for(;t<n;t++)new s(e.eq(t),{autoPlay:!1,allowWrapping:!1})},_renderCollections:function(e,t){var i=this._state,s=i.collectionsPerRow,o=i.videoDrawerClasses,f="",l=[],c=0,h,p=e.length;for(;c<p;c++){var d=r.Object.clone(e[c],!0);d._index=c,d._collectionStats=this._getCollectionStats(d),d._plural=d.videos.length!=1,f+=n.render(u,d);for(h=0;h<d.videos.length;h++)d.videos[h]._time=r.secondsToHMSFormat(d.videos[h].duration);var v=this._prepareVideoDrawerData(d.videos);v._index=c,l.push(v);if((c+1)%s==0||c==p-1)f+=n.render(a,{_videoDrawerClasses:o,_videoDrawers:l}),l.splice(0)}this._references.$collectionsContainer.html(f)},_getCollectionStats:function(e){var t=0,n=e.videos;if(!n)throw new Error("CollectionViewController._getCollectionStats(): trying to get collection stats on an object with no videos array");var i=0,s=n.length;for(;i<s;i++){var o=n[i];t+=o.duration}var u="";e.adoptions<1e4?u=r.integerCommaFormat(e.adoptions):u=r.integerAbbreviatedFormat(e.adoptions);var a="";e.views<1e4?a=r.integerCommaFormat(e.views):a=r.integerAbbreviatedFormat(e.views);var f="";return e.likes<1e4?f=r.integerCommaFormat(e.likes):f=r.integerAbbreviatedFormat(e.likes),{time:r.secondsToHMSFormat(t),adoptions:u,views:a,likes:f}},_prepareVideoDrawerData:function(e){var t=this._state.videosPerDrawer,n=[],r=0,i=e.length,s,o;for(;r<i;r+=t){o=[];for(s=0;s<t&&s+r<i;s++){var u=e[r+s];u._videoIndex=s+r+1,o.push(u)}n.push({videos:o})}return{carouselSlides:n}},_renderPagination:function(e){var t=this._state.collectionsPerPage,r=Math.ceil(e/t),i=[],s=10,o=this._state.currentPageNumber;if(r<s)var u=0,a=r,l=!1,c=!1;else if(o<s-1)var u=0,a=s,l=!1,c=!0;else if(o+s>r)var u=r-s,a=u+s,l=!0,c=!1;else var u=o-1,a=u+s,l=!0,c=!0;for(;u<a;u++){var h={pageIndex:u,pageNumber:u+1};u==this._state.currentPageNumber&&(h.classes="selected"),i.push(h)}var p=n.render(f,{pages:i,first:l,last:c,lastPage:r,lastIndex:r-1});this._references.$paginationContainers.html(p)},_onPaginationItemClick:function(e){e.preventDefault();var t=i(e.currentTarget),n=t.data("pageIndex");if(n==this._state.currentPageNumber)return;var r=this._references.$paginationContainers.find(".js-pagination-item");r.removeClass("selected");var s=r.filter("[data-page-index="+n+"]");s.addClass("selected"),this._references.$loadingIndicator.show(),this.getCollections(n)},_onCollectionItemClick:function(e){var t=i(e.currentTarget),n=t.data("collectionItemIndex"),r=this._references.$collectionsContainer.find(".js-video-container"),s=r.find(".js-video-drawer"),o,u=0,a=s.length;for(;u<a;u++){var f=s.eq(u);if(f.data("parentCollectionItemIndex")==n){o=f;break}}var l=o.closest(".js-video-container"),c=l.find(".js-video-drawer").not(o),h=l.hasClass("open");h||(this._openVideoDrawerContainers(l),this._closeVideoDrawerContainers(r.not(l)));var p;this._references.$collectionsContainer.find(".js-video-container").each(function(){$(this).hasClass("open")&&(p=$(this).find(".js-video-drawer").filter(function(){return $(this).css("visibility")=="visible"}))});if(n==p.data("parentCollectionItemIndex"))this._hideDrawers(o),this._closeVideoDrawerContainers(l);else{this._showDrawers(o),this._hideDrawers(c);var d=l.find(".js-pointer"),v=t.offset().left,m=t.width(),g=o.offset().left,y=d.width(),b=20,w=v-g+m/2-y/2+b;h?d.animate({left:w+"px"}):d.css("left",w)}},_openVideoDrawerContainers:function(e){e.stop(!0).animate({height:this._config.containerOpenHeight+"px"}).addClass("open")},_closeVideoDrawerContainers:function(e){e.stop(!0).animate({height:"0px"}).removeClass("open")},_showDrawers:function(e){e.css({position:"relative",visibility:"visible"})},_hideDrawers:function(e){e.css({position:"",visibility:""})},setInputParam:function(e,t,n){this._references.dataFeed.setInputParam(e,t,n)},setFilterStatus:function(e,t,n){this._references.dataFeed.setFilterStatus(e,t,n)},clearFilters:function(){if(!this._references.dataFeed.clearFilters())return;this._onSearchCriteriaChanged()},_onInputParamChanged:function(){this._onSearchCriteriaChanged()},_onSearchCriteriaChanged:function(){this._references.$loadingIndicator.show(),this.getCollections(0)},destroy:function(){this.base()}});return l});