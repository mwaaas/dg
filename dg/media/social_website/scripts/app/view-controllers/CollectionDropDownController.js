/**
 * CollectionAddEditController Class File
 *
 * @author aadish
 * @version $Id$
 * @requires require.js
 * @requires jQuery
 */

define(function(require) {
    'use strict';
    var DigitalGreenPageController = require('app/controllers/DigitalGreenPageController');
    var Controller = require('framework/controllers/Controller');
    var viewRenderer = require('framework/ViewRenderer');
    var jQuery = require('jquery');
    var CollectionDropDownDataFeed = require('app/libs/CollectionDropDownDataFeed');
    var collectionDropDownTemplate = require('text!app/views/collection-add-dropdown.html');
    var Chosen = require('libs/external/chosen.jquery.min');
    
    var CollectionDropDownController = Controller.extend({

        /**
         * Controller constructor
         * @return {Controller} this
         */
        constructor: function($referenceBase) {
            //this.base(bootstrapConfig, globalHelpers); //what does this do ask from nikita
            this.base($referenceBase);
            this.getCollectionDropDown();
            
            return this;
        },

        _initReferences: function($referenceBase) {
            this.base();
            var references = this._references;
            references.dataFeed = new CollectionDropDownDataFeed();
            references.$collectionAddWrapper = $referenceBase;
            references.$collectionDropDownContainer = $referenceBase.find('.js-collection-dropdown-container');
          //references.$videoAddMoreButton = $referenceBase.find('.js-add-more-videos-btn');
        },

        _initEvents: function() {
            this.base();
            
            var boundFunctions = this._boundFunctions;
            var references = this._references;
            
            boundFunctions.onDataProcessed = this._onDataProcessed.bind(this);
            references.dataFeed.on('dataProcessed', boundFunctions.onDataProcessed);
            
            /*// input param changed alert from data feed
            boundFunctions.onInputParamChanged = this._onInputParamChanged.bind(this);
            references.dataFeed.on('inputParamChanged', boundFunctions.onInputParamChanged)*/
            
            //adding another video form
            //boundFunctions.onAddMoreVideoFormClick = this._onAddMoreVideoFormClick.bind(this);
            //references.$videoAddMoreButton.on("click", boundFunctions.onAddMoreVideoFormClick);
        },
        
        getCollectionDropDown: function() {
            var collectiondropdownData = this._references.dataFeed.getCollectionDropDown();
            if (collectiondropdownData == false) {
                return false;
            }
            this._renderCollectionDropDown(collectiondropdownData);
        },

        _onDataProcessed: function() {
            this.getCollectionDropDown();
        },

        _renderCollectionDropDown: function(collectiondropdownData) {
            var renderedCollectionDropDown = viewRenderer.render(collectionDropDownTemplate, collectiondropdownData);
            this._references.$collectionDropDownContainer.html(renderedCollectionDropDown);
            this._dropdownChosen();
        },

        _dropdownChosen: function(){
            $(".chosen-select").chosen({no_results_text: "No results match", width: "90%"});
            $("#vidlist").attr('disabled', true).trigger("chosen:updated")
            $('#partnerlist').on('change', function(evt, params) {
               // $("#statelist").attr('disabled', false).trigger("chosen:updated")
              });
        },


        /*_renderVideoFormItems: function() {

            viewRenderer.renderAppend(this._references.$collectionDropDownContainer, collectionDropDownTemplate);

        },*/

        /*_onAddMoreVideoFormClick: function(event){
            event.preventDefault();
            event.stopPropagation();
            this._renderVideoFormItems();
            this._dropdownChosen();
        },*/
        
        setInputParam: function(key, value, disableCacheClearing) {
            this._references.dataFeed.setInputParam(key, value, disableCacheClearing);
        },

        _onInputParamChanged: function() {
            this.getCollectionDropDown();
        },
        /**
         * Controller destructor
         * @return {void}
         */
        destroy: function() {
            this.base();

            // TODO: clean up
        }
    });

    return CollectionDropDownController;
});
