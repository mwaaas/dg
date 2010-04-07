package com.digitalgreen.dashboardgwt.client.data;

import java.util.ArrayList;
import java.util.List;

import com.digitalgreen.dashboardgwt.client.common.Form;
import com.digitalgreen.dashboardgwt.client.common.OnlineOfflineCallbacks;
import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.digitalgreen.dashboardgwt.client.data.RegionsData.Data;
import com.digitalgreen.dashboardgwt.client.data.RegionsData.Type;
import com.google.gwt.core.client.JsArray;
import com.google.gwt.gears.client.database.DatabaseException;
import com.google.gwt.user.client.Window;

public class VillagesData extends BaseData {

	public static class Type extends BaseData.Type{
		protected Type() {}
		public final native String getVillageName() /*-{ return this.fields.village_name; }-*/;
		public final native BlocksData.Type getBlock() /*-{ return this.fields.block }-*/;
		public final native int getNoOfHouseholds() /*-{ return this.fields.no_of_households }-*/;
		public final native int getPopulation() /*-{ return this.fields.population }-*/;
		public final native int getRoadConnectivity() /*-{ return this.fields.road_connectivity }-*/;
		public final native String getControl() /*-{ return this.fields.control }-*/;
		public final native String getStartDate() /*-{ return this.fields.start_date}-*/;
	}
	
	public class Data extends BaseData.Data {
		
		final private static String COLLECTION_PREFIX = "village";
		
		private String village_name;
	    private BlocksData.Data block; 
	    private int no_of_households;
	    private int population;
	    private String road_connectivity;
	    private String control; 
	    private String start_date; 
		
		public Data() {
			super();
		}

		public Data(int id, String village_name) {
			super();
			this.id = id;
			this.village_name = village_name;
		}

		public Data(int id, String village_name, BlocksData.Data block) {
			super();
			this.id = id;
			this.village_name = village_name;
			this.block = block;
		}
		
		public Data(int id, String village_name , BlocksData.Data block, int no_of_households,
				int population, String road_connectivity, String control, String start_date) {
			super();
			this.id = id;
			this.village_name = village_name;
			this.block = block;
			this.no_of_households = no_of_households;
			this.population = population;
			this.road_connectivity = road_connectivity;
			this.control = control;
			this.start_date = start_date;
		}
		
		public String getVillageName(){
			return this.village_name;
		}
		
		public BlocksData.Data getBlock(){
			return this.block;
		}
		
		@Override
		public BaseData.Data clone() {
			Data obj = new Data();
			obj.id = this.id;
			obj.village_name = this.village_name;
			obj.block = (BlocksData.Data)this.block.clone();
			obj.no_of_households = this.no_of_households;
			obj.population = this.population;
			obj.road_connectivity = this.road_connectivity;
			obj.control = this.control;
			obj.start_date = this.start_date;
			return obj;
		}
		
		@Override
		public String getPrefixName() {
			return Data.COLLECTION_PREFIX;
		}
		
		@Override
		public void setObjValueFromString(String key, Object val) {
			if(key.equals("id")) {
				this.id = Integer.parseInt((String)val);
			} else if(key.equals("village_name")) {
				this.village_name = (String)val;
			} else if(key.equals("block_id")) {
				BlocksData block = new BlocksData();
				this.block = block.getNewData();
				this.block.id = Integer.parseInt((String)val);;
			} else if(key.equals("no_of_households")) {
				this.no_of_households = Integer.parseInt((String)val);
			} else if(key.equals("population")) {
				this.population = Integer.parseInt((String)val);
			} else if(key.equals("road_connectivity")) {
				this.road_connectivity = (String)val;
			} else if(key.equals("control")) {
				this.control = (String)val;
			} else if(key.equals("start_date")) {
				this.start_date = (String)val;
			}
		}
		
		@Override
		public void save() {
			VillagesData villagesDataDbApis = new VillagesData();
			this.id = villagesDataDbApis.autoInsert(this.village_name, Integer.valueOf(this.block.getId()).toString(),  Integer.valueOf(this.no_of_households).toString(),  Integer.valueOf(this.population).toString(), this.road_connectivity, this.control, this.start_date);
		}
		
		public void saveWithID() {
			VillagesData villagesDataDbApis = new VillagesData();
			this.id = villagesDataDbApis.autoInsertWithID(Integer.valueOf(this.id).toString(), this.village_name, Integer.valueOf(this.block.getId()).toString(),  Integer.valueOf(this.no_of_households).toString(),  Integer.valueOf(this.population).toString(), this.road_connectivity, this.control, this.start_date);
		}
	}

	
	protected static String tableID = "10";
	protected static String createTable = "CREATE TABLE IF NOT EXISTS `village` " +
												"(id INTEGER PRIMARY KEY  NOT NULL ," +
												"VILLAGE_NAME VARCHAR(100)  NOT NULL ," +
												"block_id INT  NOT NULL DEFAULT 0," +
												"NO_OF_HOUSEHOLDS INT  NULL DEFAULT NULL," +
												"POPULATION INT  NULL DEFAULT NULL," +
												"ROAD_CONNECTIVITY VARCHAR(100)  NOT NULL ," +
												"CONTROL SMALLINT  NULL DEFAULT NULL," +
												"START_DATE DATE  NULL DEFAULT NULL, " +
												"FOREIGN KEY(block_id) REFERENCES block(id)); ";  
	
	protected static String selectVillages = "SELECT id, village_name FROM village ORDER BY(village_name)";
	protected static String listVillages = "SELECT village.id, village.village_name, block.id, block.block_name FROM village JOIN block ON village.block_id = block.id ORDER BY(-village.id)";
	protected static String saveVillageOnlineURL = "/dashboard/savevillageonline/";
	protected static String getVillageOnlineURL = "/dashboard/getvillagesonline/";
	protected static String saveVillageOfflineURL = "/dashboard/savevillageoffline/";
	protected String[] fields = {"id", "village_name", "block_id", "no_of_households", "population",
			"road_connectivty", "control", "start_date"};
	protected String table_name = "village";
	
	public VillagesData() {
		super();
	}
	
	public VillagesData(OnlineOfflineCallbacks callbacks) {
		super(callbacks);
	}
	
	public VillagesData(OnlineOfflineCallbacks callbacks, Form form, String queryString) {
		super(callbacks, form, queryString);
	}

	@Override
	public Data getNewData() {
		return new Data();
	}
	
	@Override
	protected String getTableId() {
		return VillagesData.tableID;
	}
	
	protected String getTableName() {
		return this.table_name;
	}
	
	protected String[] getFields() {
		return this.fields;
	}
	
		
	@Override
	public String getListingOnlineURL(){
		return StatesData.getStateOnlineURL;
	}
	
	protected static String getSaveOfflineURL(){
		return VillagesData.saveVillageOfflineURL;
	}
	
	public final native JsArray<Type> asArrayOfData(String json) /*-{
		return eval(json);
	}-*/;

	public List serialize(JsArray<Type> villageObjects){
		List villages = new ArrayList();
		BlocksData block = new BlocksData();
		for(int i = 0; i < villageObjects.length(); i++){
			BlocksData.Data b = block.new Data(Integer.parseInt(villageObjects.get(i).getBlock().getPk()), 
					villageObjects.get(i).getBlock().getBlockName()); 
			VillagesData.Data village = new Data(Integer.parseInt(villageObjects.get(i).getPk()), 
					villageObjects.get(i).getVillageName(), b);
			villages.add(village);
		}
		return villages;
	}

	@Override
	public List getListingOnline(String json){
		return this.serialize(this.asArrayOfData(json));		
	}

	public List getVillagesListingOffline(){
		BaseData.dbOpen();
		List villages = new ArrayList();
		BlocksData block = new BlocksData();
		this.select(listVillages);
		if (this.getResultSet().isValidRow()){
			try {
				for (int i = 0; this.getResultSet().isValidRow(); ++i, this.getResultSet().next()) {
					BlocksData.Data b = block.new Data(this.getResultSet().getFieldAsInt(2), this.getResultSet().getFieldAsString(3));
					Data village = new Data(this.getResultSet().getFieldAsInt(0), this.getResultSet().getFieldAsString(1), b);
					villages.add(village);
				}				
			} catch (DatabaseException e) {
				Window.alert("Database Exception : " + e.toString());
				// TODO Auto-generated catch block
				BaseData.dbClose();
			}
		}
		BaseData.dbClose();
		return villages;
	}
	
	public List getAllVillagesOffline(){
		BaseData.dbOpen();
		List villages = new ArrayList();
		this.select(selectVillages);
		if (this.getResultSet().isValidRow()){
			try {
				for (int i = 0; this.getResultSet().isValidRow(); ++i, this.getResultSet().next()) {
					Data village = new Data(this.getResultSet().getFieldAsInt(0), this.getResultSet().getFieldAsString(1));
					villages.add(village);
				}				
			} catch (DatabaseException e) {
				Window.alert("Database Exception : " + e.toString());
				// TODO Auto-generated catch block
				BaseData.dbClose();
			}
		}
		BaseData.dbClose();
		return villages;
	}

	public Object postPageData() {
		if(BaseData.isOnline()){
			this.post(RequestContext.SERVER_HOST + this.saveVillageOnlineURL, this.queryString);
		}
		else{
			this.save();
			return true;
		}
		return false;
	}
	
	public Object getListPageData(){
		if(BaseData.isOnline()){
			this.get(RequestContext.SERVER_HOST + this.getVillageOnlineURL);
		}
		else{
			return true;
		}
		return false;
	}

	public String retrieveDataAndConvertResultIntoHtml(){
		BlocksData blockData = new BlocksData();
		List blocks = blockData.getAllBlocksOffline();
		BlocksData.Data block;
		String html = "<select name=\"block\" id=\"id_block\">";
		for(int i=0; i< blocks.size(); i++){
			block = (BlocksData.Data)blocks.get(i);
			html = html + "<option value = \"" + block.getId() +"\">" + block.getBlockName() + "</option>";
		}
		html = html + "</select>";
		
		PartnersData partnerData = new PartnersData();
		List partners = partnerData.getAllPartnersOffline();
		PartnersData.Data partner;
		for(int inline = 0; inline < 5; inline++){
			html += "<select name=\"home_village-" + inline + "-partner\" id=\"id_home_village-" + inline +"-partner\">";
			for(int i=0; i< partners.size(); i++){
				partner = (PartnersData.Data)partners.get(i);
				html = html + "<option value = \"" + partner.getId() +"\">" + partner.getPartnerName() + "</option>";
			}
			html = html + "</select>";
		}
		return html;
	}
	
	public Object getAddPageData(){
		if(BaseData.isOnline()){
			this.get(RequestContext.SERVER_HOST + this.saveVillageOnlineURL);
		}
		else{
			return retrieveDataAndConvertResultIntoHtml();
		}
		return false;
	}
}