CREATE TABLE Singers (
    SingerId     INT64 NOT NULL,
    FirstName    STRING(1024),
    LastName     STRING(1024),
    SingerInfo   BYTES(MAX),
    FullName     STRING(2048) AS (
        ARRAY_TO_STRING([FirstName, LastName], " ")
    ) STORED
) PRIMARY KEY (SingerId)
;

CREATE TABLE Albums (
    SingerId     INT64 NOT NULL,
    AlbumId      INT64 NOT NULL,
    AlbumTitle   STRING(MAX)
) PRIMARY KEY (SingerId, AlbumId)
;

CREATE TABLE Singers1 (
    SingerId     INT64 NOT NULL,
    FirstName    STRING(1024),
    LastName     STRING(1024),
    SingerInfo   BYTES(MAX),
    FullName     STRING(2048) AS (
        ARRAY_TO_STRING([FirstName, LastName], " ")
    ) STORED
) PRIMARY KEY (SingerId)
;

CREATE TABLE Albums1 (
    SingerId     INT64 NOT NULL,
    AlbumId      INT64 NOT NULL,
    AlbumTitle   STRING(MAX)
) PRIMARY KEY (SingerId, AlbumId)
;

CREATE TABLE Singers2 (
    SingerId     INT64 NOT NULL,
    FirstName    STRING(1024),
    LastName     STRING(1024),
    SingerInfo   BYTES(MAX),
    FullName     STRING(2048) AS (
        ARRAY_TO_STRING([FirstName, LastName], " ")
    ) STORED
) PRIMARY KEY (SingerId)
;

CREATE TABLE Albums2 (
    SingerId     INT64 NOT NULL,
    AlbumId      INT64 NOT NULL,
    AlbumTitle   STRING(MAX)
) PRIMARY KEY (SingerId, AlbumId)
;

CREATE TABLE Singers3 (
    SingerId     INT64 NOT NULL,
    FirstName    STRING(1024),
    LastName     STRING(1024),
    SingerInfo   BYTES(MAX),
    FullName     STRING(2048) AS (
        ARRAY_TO_STRING([FirstName, LastName], " ")
    ) STORED
) PRIMARY KEY (SingerId)
;

CREATE TABLE Albums3 (
    SingerId     INT64 NOT NULL,
    AlbumId      INT64 NOT NULL,
    AlbumTitle   STRING(MAX)
) PRIMARY KEY (SingerId, AlbumId)
;


CREATE TABLE Singers4 (
    SingerId     INT64 NOT NULL,
    FirstName    STRING(1024),
    LastName     STRING(1024),
    SingerInfo   BYTES(MAX),
    FullName     STRING(2048) AS (
        ARRAY_TO_STRING([FirstName, LastName], " ")
    ) STORED
) PRIMARY KEY (SingerId)
;

CREATE TABLE Albums4 (
    SingerId     INT64 NOT NULL,
    AlbumId      INT64 NOT NULL,
    AlbumTitle   STRING(MAX)
) PRIMARY KEY (SingerId, AlbumId)
;

CREATE TABLE Venues (
        VenueId         INT64 NOT NULL,
        VenueName       STRING(100),
        VenueInfo       BYTES(MAX),
        Capacity        INT64,
        AvailableDates  ARRAY<DATE>,
        LastContactDate DATE,
        OutdoorVenue    BOOL,
        PopularityScore FLOAT64,
        LastUpdateTime  TIMESTAMP NOT NULL
        OPTIONS(allow_commit_timestamp=true)
    ) PRIMARY KEY (VenueId)
;

CREATE TABLE Venues1 (
        VenueId         INT64 NOT NULL,
        VenueName       STRING(100),
        VenueInfo       BYTES(MAX),
        Capacity        INT64,
        AvailableDates  ARRAY<DATE>,
        LastContactDate DATE,
        OutdoorVenue    BOOL,
        PopularityScore FLOAT64,
        LastUpdateTime  TIMESTAMP NOT NULL
        OPTIONS(allow_commit_timestamp=true)
    ) PRIMARY KEY (VenueId)
;