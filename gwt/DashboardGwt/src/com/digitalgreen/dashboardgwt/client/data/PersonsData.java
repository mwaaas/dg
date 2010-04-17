package com.digitalgreen.dashboardgwt.client.data;

import java.util.ArrayList;
import java.util.List;

import com.digitalgreen.dashboardgwt.client.common.Form;
import com.digitalgreen.dashboardgwt.client.common.OnlineOfflineCallbacks;
import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.digitalgreen.dashboardgwt.client.data.PersonsData.Type;
import com.digitalgreen.dashboardgwt.client.data.PersonsData.Data;
import com.digitalgreen.dashboardgwt.client.data.validation.IntegerValidator;
import com.digitalgreen.dashboardgwt.client.data.validation.StringValidator;
import com.google.gwt.core.client.JsArray;
import com.google.gwt.gears.client.database.DatabaseException;
import com.google.gwt.user.client.Window;

public class PersonsData extends BaseData {
	
	public static class Type extends BaseData.Type{
		protected Type() {}
		public final native String getPersonName() /*-{ return $wnd.checkForNullValues(this.fields.person_name); }-*/;
		public final native String getFatherName() /*-{ return $wnd.checkForNullValues(this.fields.father_name); }-*/;
		public final native String getAge() /*-{ return $wnd.checkForNullValues(this.fields.age); }-*/;
		public final native String getGender() /*-{ return $wnd.checkForNullValues(this.fields.gender); }-*/;
		public final native String getPhoneNo() /*-{ return $wnd.checkForNullValues(this.fields.phone_no); }-*/;
		public final native String getAddress() /*-{ return $wnd.checkForNullValues(this.fields.address); }-*/;
		public final native String getLandHoldings() /*-{ return $wnd.checkForNullValues(this.fields.land_holdings); }-*/;
		public final native VillagesData.Type getVillage() /*-{ return this.fields.village;}-*/;
		public final native PersonGroupsData.Type getPersonGroup() /*-{ return this.fields.group;}-*/;
		public final native String getEquipmentHolderId() /*-{ return $wnd.checkForNullValues(this.fields.equipmentholder_id); }-*/;
		
	}
	
	public class Data extends BaseData.Data {
		
		final private static String COLLECTION_PREFIX = "person";
		
		private String person_name;
		private String father_name;
		private String age;
		private String gender;
		private String phone_no;
		private String address;
		private String land_holdings;
		private VillagesData.Data village;
		private PersonGroupsData.Data group;
		private String equipmentholder_id;		
		
		public Data() {
			super();
		}
		
		public Data(String id) {
			super();
			this.id = id;
		}
		
		public Data(String id, String person_name,String father_name,String age,String gender,String phone_no,String address,String land_holdings,
				VillagesData.Data village,PersonGroupsData.Data group, String equipmentholder_id) {
			super();
			this.id = id;
			this.person_name = person_name;
			this.father_name = father_name;
			this.age = age;
			this.gender = gender;
			this.phone_no = phone_no;
			this.address = address;
			this.land_holdings = land_holdings;
			this.village = village;
			this.group = group;
			this.equipmentholder_id = equipmentholder_id;
		}
		

		public Data(String id, String person_name, VillagesData.Data village) {
			super();
			this.id = id;
			this.person_name = person_name;
			this.village = village;
		}
		
		public Data(String id, String person_name,VillagesData.Data village,PersonGroupsData.Data group) {
			super();
			this.id = id;
			this.person_name = person_name;
			this.village = village;
			this.group = group;
		}
		
		public Data(String id, String person_name){
			super();
			this.id = id;
			this.person_name = person_name;
		}
				
		public String getPersonName(){
			return this.person_name;
		}
		
		public String getAge(){
			return this.age;
		}
		
		public String getGender(){
			return this.gender;
		}
				
		public String getPhoneNo(){
			return this.phone_no;
		}
		
		public String getAddress(){
			return this.address;
		}
		
		public String getLandHoldings(){
			return this.land_holdings;
		}
		
		public VillagesData.Data getVillage(){
			return this.village;
		}
		
		public PersonGroupsData.Data getGroup(){
			return this.group;
		}
						
		public String getEquipmentHolderId(){
			return this.equipmentholder_id;
		}
		
		public BaseData.Data clone() {
			Data obj = new Data();
			obj.village = (new VillagesData()).new Data();
			obj.group = (new PersonGroupsData()).new Data();
			return obj;
		}
		
		@Override
		public String getPrefixName() {
			return Data.COLLECTION_PREFIX;
		}
		
		@Override
		public void setObjValueFromString(String key, String val) {
			super.setObjValueFromString(key, val);
			if(key.equals("person_name")) {
				this.person_name = (String)val;
			} else if(key.equals("father_name")) {
				this.father_name = (String)val;
			} else if(key.equals("age")) {
				this.age = (String)val;
			} else if(key.equals("gender")) {
				this.gender = (String)val;
			} else if(key.equals("phone_no")) {
				this.phone_no = (String)val;
			} else if(key.equals("address")) {
				this.address = (String)val;
			} else if(key.equals("land_holdings")) {
				this.land_holdings = (String)val;
			} else if(key.equals("village")) {
				VillagesData village = new VillagesData();
				this.village = village.getNewData();
				this.village.id = val;
			}  else if(key.equals("group")) {
				PersonGroupsData group = new PersonGroupsData();
				this.group = group.getNewData();
				this.group.id = val;
			}  else if(key.equals("equipmentholder")) {
				this.equipmentholder_id = val;
			}  else {
				return;
			}
			this.addNameValueToQueryString(key, val);
		}
		
		@Override
		public boolean validate(){
			StringValidator personName = new StringValidator(this.person_name,false,false,0,100);
			StringValidator fatherName = new StringValidator(this.father_name,true,true,0,100);
			IntegerValidator age = new IntegerValidator(this.age,true,true,0,100);
			StringValidator phoneNo = new StringValidator(this.phone_no,true,true,0,100);
			StringValidator address = new StringValidator(this.address,true,true,0,500);
			IntegerValidator landHoldings = new IntegerValidator(this.land_holdings,true,true,0,200);
			
			return personName.validate() && fatherName.validate() && age.validate() && phoneNo.validate()
				&& address.validate() && landHoldings.validate() ;
		}
		
		@Override
		public boolean validate(BaseData.Data foreignKey){
			StringValidator personName = new StringValidator(this.person_name,false,false,0,100);
			StringValidator fatherName = new StringValidator(this.father_name,true,true,0,100);
			IntegerValidator age = new IntegerValidator(this.age,true,true,0,100);
			StringValidator phoneNo = new StringValidator(this.phone_no,true,true,0,100);
			StringValidator address = new StringValidator(this.address,true,true,0,500);
			IntegerValidator landHoldings = new IntegerValidator(this.land_holdings,true,true,0,200);
			
			return personName.validate() && fatherName.validate() && age.validate() && phoneNo.validate()
				&& address.validate() && landHoldings.validate() ;
		}
		
		@Override		
		public void save() {
			PersonsData personsDataDbApis = new PersonsData();
			this.id = personsDataDbApis.autoInsert(this.id,
						this.person_name,
						this.father_name,
						this.age,
						this.gender,
						this.phone_no,
						this.address,
						this.land_holdings,
						this.village.getId(),
						this.group.getId(),
						this.equipmentholder_id);
			this.addNameValueToQueryString("id", this.id);
		}
		
		@Override
		public void save(BaseData.Data foreignKey) {
			PersonsData personsDataDbApis = new PersonsData();
			this.id = personsDataDbApis.autoInsert(this.id,
					this.person_name,
					this.father_name,
					this.age,
					this.gender,
					this.phone_no,
					this.address,
					this.land_holdings,
					this.village.getId(),
					foreignKey.getId(),
					this.equipmentholder_id);
			this.addNameValueToQueryString("id", this.id);
			this.addNameValueToQueryString("persongroup", foreignKey.getId());
		}
		

		@Override
		public String getTableId() {
			PersonsData personsDataDbApis = new PersonsData();
			return personsDataDbApis.tableID;
		}
	}
	
	public static String tableID = "20";
	protected static String createTable = "CREATE TABLE IF NOT EXISTS `person` " +
												"(id INTEGER PRIMARY KEY  NOT NULL ," +
												"PERSON_NAME VARCHAR(100)  NOT NULL ," +
												"FATHER_NAME VARCHAR(100)  NULL DEFAULT NULL ," +
												"AGE INT  NULL DEFAULT NULL," +
												"GENDER VARCHAR(1) NOT NULL," +
												"PHONE_NO VARCHAR(100) NULL DEFAULT NULL," +
												"ADDRESS VARCHAR(500) NULL DEFAULT NULL," +
												"LAND_HOLDINGS INT  NULL DEFAULT NULL," +
												"village_id INT NOT NULL DEFAULT 0," +
												"group_id INT  NULL DEFAULT NULL," +
												"equipmentholder_id INT  NULL DEFAULT NULL, " +
												"FOREIGN KEY(village_id) REFERENCES village(id), " +
												"FOREIGN KEY(group_id) REFERENCES person_groups(id), " +
												"FOREIGN KEY(equipmentholder_id) REFERENCES equipment_holder(id) ); " ; 
	
	protected static String selectPersons = "SELECT person.id, person.PERSON_NAME, village.id, village.village_name " +
											"FROM person JOIN village on person.village_id = village.id ORDER BY (PERSON_NAME);";
	protected static String listPersons = "SELECT p.id, p.PERSON_NAME, p.village_id, vil.VILLAGE_NAME, p.group_id, pg.GROUP_NAME " +
			"FROM person p LEFT JOIN village vil on p.village_id = vil.id " +
			"LEFT JOIN person_groups pg on p.group_id = pg.id ORDER BY (-p.id);";
	protected static String savePersonOfflineURL = "/dashboard/savepersonoffline/";
	protected static String savePersonOnlineURL = "/dashboard/savepersononline/";
	protected static String getPersonOnlineURL = "/dashboard/getpersonsonline/";
	protected String table_name = "person";
	protected String[] fields = {"id", "person_name","father_name", "age", "gender", "phone_no", "address", "land_holder",
			"village_id", "group_id", "equipmentholder_id"};
	
	
	public PersonsData() {
		super();
	}
	public PersonsData(OnlineOfflineCallbacks callbacks) {
		super(callbacks);
	}
	
	public PersonsData(OnlineOfflineCallbacks callbacks, Form form) {
		super(callbacks, form);
	}
	@Override
	public Data getNewData() {
		return new Data();
	}
	
	@Override
	protected String getTableId() {
		return PersonsData.tableID;
	}
	
	@Override
	protected String getTableName() {
		return this.table_name;
	}
	
	@Override
	protected String[] getFields() {
		return this.fields;
	}
	
	@Override
	public String getListingOnlineURL(){
		return PersonsData.getPersonOnlineURL;
	}
	
	@Override
	public String getSaveOfflineURL(){
		return PersonsData.savePersonOfflineURL;
	}
		
	public final native JsArray<Type> asArrayOfData(String json) /*-{
		return eval(json);
	}-*/;
	
	public List serialize(JsArray<Type> personObjects){
		List persons = new ArrayList();
		VillagesData village = new VillagesData();
		PersonGroupsData group = new PersonGroupsData();
		VillagesData.Data vil = null;
		PersonGroupsData.Data pg = group.new Data();
		for(int i = 0; i < personObjects.length(); i++){
			vil = village.new Data(personObjects.get(i).getVillage().getPk(),
					personObjects.get(i).getVillage().getVillageName());
			
			if(personObjects.get(i).getPersonGroup() != null){
				pg = group.new Data(personObjects.get(i).getPersonGroup().getPk(),
					personObjects.get(i).getPersonGroup().getPersonGroupName());
			}
			
			Data person = new Data(personObjects.get(i).getPk(),
						personObjects.get(i).getPersonName(),
						personObjects.get(i).getFatherName(),
						personObjects.get(i).getAge(),
						personObjects.get(i).getGender(),
						personObjects.get(i).getPhoneNo(),
						personObjects.get(i).getAddress(),
						personObjects.get(i).getLandHoldings(),
						vil,
						pg,
						personObjects.get(i).getEquipmentHolderId());
			
			persons.add(person);
		}
		return persons;
	}
	
	@Override
	public List getListingOnline(String json){
		return this.serialize(this.asArrayOfData(json));		
	}
	
	public List getPersonsListingOffline(){
		BaseData.dbOpen();
		List persons = new ArrayList();
		VillagesData village = new VillagesData();
		PersonGroupsData group = new PersonGroupsData();
		this.select(listPersons);
		if (this.getResultSet().isValidRow()){
			
			try {
				int i;
				for (i = 0; this.getResultSet().isValidRow(); ++i, this.getResultSet().next()) {
					PersonGroupsData.Data pg;
					if(this.getResultSet().getFieldAsString(4) == null){
						pg = null;
					}
					else{
						pg = group.new Data(this.getResultSet().getFieldAsString(4),  this.getResultSet().getFieldAsString(5));
					}
					
					VillagesData.Data v = village.new Data(this.getResultSet().getFieldAsString(2),  this.getResultSet().getFieldAsString(3)) ;
					
					Data person = new Data(this.getResultSet().getFieldAsString(0), this.getResultSet().getFieldAsString(1),v,pg);
					persons.add(person);
	    	      }
				
			} catch (DatabaseException e) {
				Window.alert("Database Exception : " + e.toString());
				BaseData.dbClose();
			}
			
		}
		BaseData.dbClose();
		return persons;
	}
	
	public List getAllPersonsOffline(){
		BaseData.dbOpen();
		List persons = new ArrayList();
		this.select(selectPersons);
		if (this.getResultSet().isValidRow()){
			try {
				VillagesData villagesData = new VillagesData();
				VillagesData.Data village;
				for (int i = 0; this.getResultSet().isValidRow(); ++i, this.getResultSet().next()) {
					village = villagesData.new Data(this.getResultSet().getFieldAsString(2), this.getResultSet().getFieldAsString(3));
					Data person = new Data(this.getResultSet().getFieldAsString(0), this.getResultSet().getFieldAsString(1), village);
					persons.add(person);
	    	      }				
			} catch (DatabaseException e) {
				Window.alert("Database Exception : " + e.toString());
				BaseData.dbClose();
			}
			
		}
		BaseData.dbClose();
		return persons;
	}
	
	public Object postPageData() {
		if(BaseData.isOnline()){
			this.post(RequestContext.SERVER_HOST + PersonsData.savePersonOnlineURL, this.form.getQueryString());
		}
		else{
			if(this.validate()) {
				this.save();
				return true;
			}
		}
		
		return false;
	}
	
	public Object getListPageData(){
		if(BaseData.isOnline()){
			this.get(RequestContext.SERVER_HOST + PersonsData.getPersonOnlineURL);
		}
		else{
			return true;
		}
		return false;
	}	
	
	public String retrieveDataAndConvertResultIntoHtml(){
		VillagesData villageData = new VillagesData();
		List villages = villageData.getAllVillagesOffline();
		VillagesData.Data village;
		String html = "<select name=\"village\" id=\"id_village\">" + 
					"<option value='' selected='selected'>---------</option>";
		for(int i=0; i< villages.size(); i++){
			village = (VillagesData.Data)villages.get(i);
			html = html + "<option value = \"" + village.getId() +"\">" + village.getVillageName() + "</option>";
		}
		html = html + "</select>";
		
		PersonGroupsData personGroupData = new PersonGroupsData();
		List groups = personGroupData.getAllPersonGroupsOffline();
		PersonGroupsData.Data group;
		html = html + "<select name=\"group\" id=\"id_group\">" + 
			"<option value='' selected='selected'>---------</option>";
		for(int i=0; i< groups.size(); i++){
			group = (PersonGroupsData.Data)groups.get(i);
			html = html + "<option value = \"" + group.getId() +"\">" + group.getPersonGroupName() + "</option>";
		}
		html = html + "</select>";
		
		PracticesData practiceData = new PracticesData();
		List practices = practiceData.getAllPracticesOffline();
		PracticesData.Data practice;
		for(int inline = 0; inline < 3; inline++){
			html += "<select name=\"personadoptpractice_set-" + inline + "-practice\" id=\"id_personadoptpractice_set-" + inline +"-practice\">"
			+ "<option selected='selected' value=''>---------</option>";
			for(int i=0; i< practices.size(); i++){
				practice = (PracticesData.Data)practices.get(i);
				html = html + "<option value = \"" + practice.getId() +"\">" + practice.getPracticeName() + "</option>";
			}
			html = html + "</select>";
		}
						
		return html;
	}
	
	public Object getAddPageData(){
		if(BaseData.isOnline()){
			this.get(RequestContext.SERVER_HOST + PersonsData.savePersonOnlineURL);
		}
		else{
			return retrieveDataAndConvertResultIntoHtml();
		}
		return false;
	}
		
}