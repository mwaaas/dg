package com.digitalgreen.dashboardgwt.client.servlets;

import java.util.HashMap;

import com.digitalgreen.dashboardgwt.client.common.Form;
import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.digitalgreen.dashboardgwt.client.servlets.ServletInterface;
import com.digitalgreen.dashboardgwt.client.templates.Template;
import com.google.gwt.user.client.Cookies;
import com.google.gwt.user.client.Window;

public class BaseServlet implements ServletInterface {
	
	protected RequestContext requestContext = null;	
	protected HashMap form = null;
	private static boolean isLoggedInCtx = false;

	// Slightly breaks abstraction since the RequestContext should be 
	// created in the template as a GET request, similar to how 
	// POSTs work.
	public BaseServlet() {
		this.requestContext = new RequestContext();
	}

	public BaseServlet(RequestContext requestContext) {
		this.requestContext = requestContext;
		// Most likely a POST request that has a queryString/formTemplate
		if(this.requestContext.hasQueryString()) {
			// TODO:  Enable this once the Form class is implemented.
			// Form formTemplate = this.requestContext.getFormTemplate();
			// formTemplate.parseQueryString(this.requestContext.getQueryString());
			this.form = Form.flatten(this.requestContext.getQueryString());
		}
	}

	protected String getMethodTypeCtx() {
		return this.requestContext.getMethodTypeCtx();
	}
	
	public RequestContext getRequestContext() {
		return this.requestContext;
	}
	
	public boolean isLoggedIn() {
		return isLoggedInCtx;
	}
	
	public void setIsLoggedIn(boolean loggedIn) {
		isLoggedInCtx = loggedIn;
	}
	
	public void redirectTo(BaseServlet servlet) {
		servlet.response();
	}

	public void fillTemplate(Template template) {
		template.fill();
	}
	
	// Override this
	public void response() {
		String loggedInCtx = Cookies.getCookie("username");
		// Must have a cookie
		if(loggedInCtx == null || loggedInCtx == "") {
			this.setIsLoggedIn(false);
		} else {
			this.requestContext.setDefaultLoggedInUserArg(loggedInCtx);
			this.setIsLoggedIn(true);
		}
	}
}