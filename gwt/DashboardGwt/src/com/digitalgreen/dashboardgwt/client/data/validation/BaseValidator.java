package com.digitalgreen.dashboardgwt.client.data.validation;

public class BaseValidator {
	private boolean nullable = true;
	private boolean blank = true;
	private String value = null;
	
	public BaseValidator(String value) {
		this.value = value;
	}
	
	public BaseValidator(String value, boolean nullable, boolean blank) {
		this.value = value;
		this.nullable = nullable;
		this.blank = blank;
	}

	public String getValue() {
		return this.value;
	}
	
	// Override this
	public boolean validate() {
		return !(!nullable && value == null || !blank && value.equals(""));
	}
}