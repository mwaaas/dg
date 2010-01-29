package com.digitalgreen.dashboard.client;

import com.google.gwt.core.client.EntryPoint;
//import com.google.gwt.core.client.GWT;
import com.google.gwt.dom.client.Element;
import com.google.gwt.dom.client.Node;
import com.google.gwt.event.dom.client.ClickEvent;
import com.google.gwt.event.dom.client.ClickHandler;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.FormPanel;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.FormPanel.SubmitCompleteEvent;
import com.google.gwt.user.client.ui.FormPanel.SubmitEvent;
import com.google.gwt.user.client.ui.FormPanel.SubmitHandler;
import com.google.gwt.user.client.ui.HTML;
import com.google.gwt.user.client.ui.HTMLPanel;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class Dashboard implements EntryPoint {
	
	/**
	 * This is the entry point method.
	 */
	
	public void onModuleLoad() {
		
		/*
		 * Wrap the Child elements before the parent element.
		 * Button is wrapped before the form is wrapped.
		 * */

		Button b = new Button("Save");
	    b.setStyleName("button default");
	    
		//Element e_form = RootPanel.get("region_form").getElement();
		//final FormPanel f = FormPanel.wrap(e_form);
	    final FormPanel f = new FormPanel();
		f.setAction("http://174.129.13.106:8000/feeds/animators/49/");
	    f.setEncoding(FormPanel.ENCODING_MULTIPART);
	    f.setMethod(FormPanel.METHOD_POST);

	    HTMLPanel h = new HTMLPanel("<div>" +
	    					"<fieldset class='module aligned '>" +
	    					"<div class='form-row region_name  '>" +
	    					"<div>" +
	    					"<label for='id_region_name' class='required'>Region name:</label><input id='id_region_name' type='text' class='vTextField' name='region_name' maxlength='100' />" +
	    					"</div>" +
	    					"</div>" +
	    					"<div class='form-row start_date'>" +
	    					"<div><label for='id_start_date'>Start date:</label><input id='id_start_date' type='text' class='vDateField' name='start_date' size='10' /></div>" +
	    					"</div>" +
	    					"</fieldset>" +
	    					"</div>");
	    f.add(h);
	    RootPanel.get("content-main").add(f);
	    RootPanel.get("submit-button").add(b);
	    
	    b.addClickHandler(new ClickHandler() {
		      public void onClick(ClickEvent event) {
		    	   Window.alert("form submit 1");
		    	   f.submit();
			      }
	    });
	    
	    f.addSubmitHandler(new FormPanel.SubmitHandler() {	
			public void onSubmit(SubmitEvent event) {
				// TODO Auto-generated method stub				
	    		Window.alert("form submit 2");
	    	}
	    });
	    
	    f.addSubmitCompleteHandler(new FormPanel.SubmitCompleteHandler() {
	    	public void onSubmitComplete(SubmitCompleteEvent event) {
	    		Window.alert("hi");
	    	}
	    });
	    

	}	
}
