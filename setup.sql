BEGIN TRANSACTION;

CREATE TABLE URLs(
	videoId INTEGER PRIMARY KEY NOT NULL,
	url text
	);
	
CREATE TABLE Keywords(
	videoId INTEGER PRIMARY KEY NOT NULL,
	keyword text,
	FOREIGN KEY(videoId) REFERENCES URLs(videoId)
	);

CREATE TABLE Channels(
	channelId INTEGER PRIMARY KEY NOT NULL,
	channelName text
	);
	
CREATE TABLE Categories(
	categoryId INTEGER PRIMARY KEY NOT NULL,
	categoryName text
	);
	
CREATE TABLE Videos(
	videoId INTEGER PRIMARY KEY NOT NULL,
	channelId INTEGER,
	title text,
	description text,
	duration INTEGER,
	categoryId INTEGER,
	thumbnail bytea,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	FOREIGN KEY(videoId) REFERENCES URLs(videoId),
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(categoryId) REFERENCES Categories(categoryId)
	);
	
CREATE TABLE Comments(
	commentId INTEGER PRIMARY KEY NOT NULL,
	channelId INTEGER,
	videoId INTEGER,
	content text,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(videoId) REFERENCES Videos(videoId)
	);
	
CREATE TABLE Subscriptions(
	channelId INTEGER,
	subscribedChannel INTEGER,
	PRIMARY KEY(channelId, subscribedChannel),
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(subscribedChannel) REFERENCES Channels(channelId)
	);
	
CREATE TABLE Playlists(
	playlistId INTEGER PRIMARY KEY NOT NULL,
	playlistName text,
	channelId INTEGER,
	FOREIGN KEY(channelId) REFERENCES Channels(channelId)
	);

CREATE TABLE PlaylistVideos(
	playlistId INTEGER,
	videoId INTEGER,
	PRIMARY KEY(playlistId, videoId),
	FOREIGN KEY(playlistId) REFERENCES Playlists(playlistId),
	FOREIGN KEY(videoId) REFERENCES Videos(videoId)
	);

CREATE TABLE LikedVideos(
	channelId INTEGER,
	videoId INTEGER,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	PRIMARY KEY(channelId, videoId),
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(videoId) REFERENCES Videos(videoId)
	);
	
CREATE TABLE DislikedVideos(
	channelId INTEGER,
	videoId INTEGER,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	PRIMARY KEY(channelId, videoId),
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(videoId) REFERENCES Videos(videoId)
	);
	
CREATE TABLE LikedComments(
	channelId INTEGER,
	commentId INTEGER,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	PRIMARY KEY(channelId, commentId),
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(commentId) REFERENCES Comments(commentId)
	);
	
CREATE TABLE DislikedComments(
	channelId INTEGER,
	commentId INTEGER,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	PRIMARY KEY(channelId, commentId),
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(commentId) REFERENCES Comments(commentId)
	);

CREATE TABLE Views(
	channelId INTEGER,
	videoId INTEGER,
	year INTEGER,
	month INTEGER,
	day INTEGER,
	PRIMARY KEY(channelId, videoId),
	FOREIGN KEY(channelId) REFERENCES Channels(channelId),
	FOREIGN KEY(videoId) REFERENCES Videos(videoId)
	);

COMMIT;