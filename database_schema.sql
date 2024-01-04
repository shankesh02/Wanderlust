CREATE TABLE `flight` (
  `Name` varchar(25) DEFAULT NULL,
  `Flight` varchar(20) DEFAULT NULL,
  `Departure` varchar(20) DEFAULT NULL,
  `Destination` varchar(20) DEFAULT NULL,
  `Number` varchar(5) DEFAULT NULL,
  `Class` varchar(25) DEFAULT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Amount` varchar(30) DEFAULT NULL
);

CREATE TABLE `hotel` (
  `Name` varchar(20) DEFAULT NULL,
  `Hotel` varchar(75) DEFAULT NULL,
  `Nights` varchar(5) DEFAULT NULL,
  `Room` varchar(25) DEFAULT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Amount` varchar(30) DEFAULT NULL
);

CREATE TABLE `holidaypackage` (
  `Name` varchar(20) DEFAULT NULL,
  `Package` varchar(30) DEFAULT NULL,
  `Place` varchar(20) DEFAULT NULL,
  `Days` varchar(20) DEFAULT NULL,
  `Person` varchar(10) DEFAULT NULL,
  `Cuisine` varchar(30) DEFAULT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Amount` varchar(30) DEFAULT NULL
);

CREATE TABLE `train` (
  `Name` varchar(20) DEFAULT NULL,
  `Departure` varchar(20) DEFAULT NULL,
  `Destination` varchar(20) DEFAULT NULL,
  `Number` varchar(5) DEFAULT NULL,
  `Class` varchar(25) DEFAULT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Amount` varchar(30) DEFAULT NULL
);

CREATE TABLE `activity` (
  `Name` varchar(20) DEFAULT NULL,
  `Activity` varchar(75) DEFAULT NULL,
  `Hours` varchar(10) DEFAULT NULL,
  `Person` varchar(10) DEFAULT NULL,
  `Time` varchar(20) DEFAULT NULL,
  `Date` varchar(20) DEFAULT NULL,
  `Amount` varchar(30) DEFAULT NULL
);
