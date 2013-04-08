define(function(require) {
    'use strict';
    
    var DigitalGreenDataFeed = require('app/libs/DigitalGreenDataFeed');
    var DataModel = require('app/libs/DataModel');
    var Util = require('framework/Util');

    var CollectionsDataFeed = DigitalGreenDataFeed.extend({

        _filters: undefined,

        /*
        Input params:

        searchString {string}
        filters {Object}
        orderBy {string}
        page {Number}
        count {Number}
        relativeUserId {string} (optional) -- is this still needed?

        Output params:
        collections {Collection[]}
        totalCount {Number}
        */

        constructor: function() {
            this.base('api/collectionsSearch.php');

            this._filters = {};

            var dataModel = this._dataModel;

            // prepare data model
            var collectionsSubModel = dataModel.addSubModel('collections', true);

            // set up input params
            this.addInputParam('page', true, 0, true);
            this.addInputParam('count', true, 12, true);
            this.addInputParam('filters', false, null, true, collectionsSubModel);
            this.addInputParam('orderBy', false, null, true, collectionsSubModel);
            this.addInputParamCacheClear('language', collectionsSubModel);
        },

        fetch: function(page, countPerPage) {
            if (page == undefined) {
                page = 0;
            }

            if (countPerPage == undefined) {
                countPerPage = 12;
            }

            this.setInputParam('page', page, true);
            this.setInputParam('count', countPerPage, true);

            // perform the fetch
            this.base();
        },

        _processData: function(unprocessedData) {
            this.base(unprocessedData);
            
            // local references
            var dataModel = this._dataModel;
            var collectionsModel = dataModel.get('collections');

            // gather count and page for caching and saving purposes
            var countPerPage = unprocessedData.requestParameters.count;
            var page = unprocessedData.requestParameters.page;

            // store total count
            dataModel.set('totalCount', unprocessedData.totalCount);

            // import collections from data
            var collectionsToAdd = unprocessedData.collections;
            var startingCacheId = page * countPerPage;

            collectionsModel.addSubset(collectionsToAdd, startingCacheId);
        },

        /**
         * Sets the status and value of a filter
         * @param {Boolean} filterParam The filter parameter
         * @param {Boolean} filterValue The filter value
         * @param {Boolean} active Whether or not the filter is active
         * @return {boolean} true if a filter was changed, else false
         */
        setFilterStatus: function(filterParam, filterValue, active) {

            var filters = this._filters;
            if (filters[filterParam] == undefined) {
                filters[filterParam] = [];
            }

            var filterIndex = filters[filterParam].indexOf(filterValue);
            var filterPresent = (filterIndex != -1);

            if ((active && filterPresent) || !active && !filterPresent) {
                return false;
            }

            // if we get here, a filter has changed
            // update accordingly

            if (active) {
                filters[filterParam].push(filterValue);
            } else {
                filters[filterParam].splice(filterIndex, 1);
            }

            // we now clone our filters object to not only reduce cross class
            // referencing to this object, but also to trigger the datafeed
            // to clear the cache since the reference will be changing

            var newFilters = Util.Object.clone(filters);
            this.setInputParam('filters', newFilters);

            return true;
        },

        /**
         * Clears the search filters
         * @return {boolean} true if a filter was changed, else false
         */
        clearFilters: function() {

            var filterExisted = false;

            var filters = this._filters;
            var filterKey;
            for (filterKey in filters) {
                var currentFilter = filters[filterKey];
                var len = currentFilter.length;
                if (len > 0) {
                    filterExisted = true;
                    break;
                }
            }

            this._filters = {};

            return filterExisted;
        },

        getTotalCount: function() {
            return this._dataModel.get('totalCount');
        },

        getCollections: function() {

            var page = this.getInputParam('page');
            var countPerPage = this.getInputParam('count');

            var collections = this._dataModel.get('collections').getSubset(page * countPerPage, countPerPage);

            if (!collections) {
                this.fetch(page, countPerPage);
                return false;
            }

            return collections;
        }

    });

    return CollectionsDataFeed;

});