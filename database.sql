create table user (userId int AUTO_INCREMENT NOT NULL, lname varchar(30)
NOT NULL, fname varchar(30) NOT NULL, email varchar(100) NOT NULL, CONSTRAINT PK_PERSON PRIMARY KEY(userId,email));


create table comment (commentId int NOT NULL, userId int NOT NULL, bpcomm
ent varchar(140), apcomment varchar(140), commentlanguage varchar(50) NOT NULL,
PRIMARY KEY(commentId), CONSTRAINT FK_UserComment FOREIGN KEY (userId) REFERENC
S user(userId));
