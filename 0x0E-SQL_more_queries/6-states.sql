-- script that creates the db hbtn_0d_usa and table states
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa.states`(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name varchar(256) NOT NULL,
	PRIMARY KEY(`id`)
);
