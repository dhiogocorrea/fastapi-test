CREATE TABLE master.dbo.nfs (
	id varchar(36) NOT NULL PRIMARY KEY,
	description text NOT NULL,
	state varchar(2) NOT NULL,
	value float NOT NULL
)