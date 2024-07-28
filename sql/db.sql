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

CREATE TABLE Customers (
               CustomerId INT64 NOT NULL,
               CustomerName STRING(62) NOT NULL,
               ) PRIMARY KEY (CustomerId)
;

 CREATE TABLE ShoppingCarts (
               CartId INT64 NOT NULL,
               CustomerId INT64 NOT NULL,
               CustomerName STRING(62) NOT NULL,
               CONSTRAINT FKShoppingCartsCustomerId FOREIGN KEY (CustomerId)
               REFERENCES Customers (CustomerId) ON DELETE CASCADE
               ) PRIMARY KEY (CartId)
;