define([
  'jquery',
  'underscore',
  'backbone',
  'views/header',
  'views/dashboard',
  'views/list',
  'views/form_controller',
'views/status',
'layoutmanager'      
  ], function($, underscore, Session, HeaderView, DashboardView, ListView, FormControllerView, StatusView){
                  
    var AppLayout = Backbone.View.extend({
      template: "#page_layout",
      manage : true,
      
      initialize: function() {
          console.log("initilizing app layout");
          curr_list_view = null;
          current_add_edit_view = null;
          this.setView("#side_panel", new DashboardView());
                
      },
          
      render_dashboard: function() {
          // $(this.el)
          //     .html('');
          // $(this.el)
          //     .append(header.render("<li class='active' >Dashboard</li>")
          //     .el);
          // this.setView("#header", new HeaderView({serialize: { breadcrumb: $('#dashboard_breadcrumb').html() }}));
          this.setView("#content", new StatusView());
          this.render();
          //         
          // $(this.el)
          //               .append(dashboard.render()
          //               .el);
          return this;
                   
      },
      render_list_view: function(params) {
          // var bcrumb_template = _.template($('#list_breadcrumb').html());
          // this.setView("#header", new HeaderView({serialize: { breadcrumb: bcrumb_template({bread:params.view_configs.page_header}) }}));
          this.setView("#content", new ListView({initialize:params}));
          this.render();
          
          return this;
      },
      render_add_edit_view: function(params, data) {
          // var add_or_edit = "add";
//           if (data) add_or_edit = "edit";
          // var bcrumb_template = _.template($('#add_edit_breadcrumb').html());
//           this.setView("#header", new HeaderView({serialize: { breadcrumb: bcrumb_template({bread1:params.view_configs.page_header.toLowerCase(),bread2:params.view_configs.page_header,add_or_edit:add_or_edit}) }}));
          
          
          if(!this.formcontroller_v)
          {
              this.formcontroller_v = new FormControllerView({
                            serialize: {
                                button1: "Save",
                                button2: "Save and Add Another"
                            },
                            initialize: params,
                            model_id: data,
                            model_json: null
          
                        });
          }
          else
          {
              this.formcontroller_v.params = {
                            serialize: {
                                button1: "Save",
                                button2: "Save and Add Another"
                            },
                            initialize: params,
                            model_id: data,
                            model_json: null
          
                        };
            this.formcontroller_v.options = {
                          serialize: {
                              button1: "Save",
                              button2: "Save and Add Another"
                          },
                          initialize: params,
                          model_id: data,
                          model_json: null
          
                      };            
          }
          this.setView("#content", this.formcontroller_v);
              
          this.render();
          
          return this;
      }
   
    });
  return new AppLayout;
});