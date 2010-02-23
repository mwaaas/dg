package com.digitalgreen.dashboardgwt.client.data;

import com.digitalgreen.dashboardgwt.client.common.RequestContext;

public class TrainingsData extends BaseData {

	final protected static String createTable = "CREATE TABLE IF NOT EXISTS `training` " +
												"(id INTEGER PRIMARY KEY  NOT NULL ," +
												"TRAINING_PURPOSE TEXT  NOT NULL ," +
												"TRAINING_OUTCOME TEXT  NOT NULL ," +
												"TRAINING_START_DATE DATE  NULL DEFAULT NULL," +
												"TRAINING_END_DATE DATE  NULL DEFAULT NULL," +
												"village_id INT  NOT NULL DEFAULT 0," +
												"dm_id INT  NOT NULL DEFAULT 0," +
												"fieldofficer_id INT  NOT NULL DEFAULT 0, " +
												"FOREIGN KEY(village_id) REFERENCES village(id), " +
												"FOREIGN KEY(dm_id) REFERENCES development_manager(id), " +
												"FOREIGN KEY(fieldofficer_id) REFERENCES field_officer(id));" ;  
	
	public TrainingsData(RequestContext requestContext) {
		super();
	}
}