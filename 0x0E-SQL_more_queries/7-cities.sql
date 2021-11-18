-- creates the db htbn_0d_usa and table cities
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa.cities`(
	`id` int unique auto_increment not null,
	`state_id` int not null,
	`name` varchar(256) not null,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`state_id`) REFERENCES hbtn_0d_usa.states(id)
);
